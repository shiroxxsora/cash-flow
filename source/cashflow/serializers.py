from rest_framework import serializers
from .models import Cashflow, Status, Type, Category, Undercat, UndercatList


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UndercatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Undercat
        fields = '__all__'


class CashflowSerializer(serializers.ModelSerializer):
    # Поля ID только для записи
    status_id = serializers.IntegerField(write_only=True, required=True)
    type_id = serializers.IntegerField(write_only=True, required=True)
    category_id = serializers.IntegerField(write_only=True, required=True)

    # Поля для возвращаемых объектов
    status = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    # Список подкатегорий для записи (ID)
    undercats = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=True
    )

    # Список подкатегорий для чтения
    undercats_data = serializers.SerializerMethodField()
    class Meta:
        model = Cashflow
        fields = [
            'id',
            'creation_time',
            'status_id',
            'status',
            'type_id',
            'type',
            'category_id',
            'category',
            'summ',
            'comment',
            'undercats',
            'undercats_data'
        ]

    def get_undercats_data(self, obj):
        undercat_list = UndercatList.objects.filter(cashflow_id=obj.id)
        undercats = [undercat_list_item.undercat_id for undercat_list_item in undercat_list]
        return UndercatSerializer(undercats, many=True).data

    def get_status(self, obj):
        status = Status.objects.get(id=obj.status_id.id)
        return StatusSerializer(status).data

    def get_type(self, obj):
        type = Type.objects.get(id=obj.type_id.id)
        return TypeSerializer(type).data

    def get_category(self, obj):
        category = Category.objects.get(id=obj.category_id.id)
        return CategorySerializer(category).data

    # Переопределяем метод create для обработки связанных подкатегорий
    def create(self, validated_data):
        status_id = validated_data.pop('status_id')
        type_id = validated_data.pop('type_id')
        category_id = validated_data.pop('category_id')
        undercats = validated_data.pop('undercats', [])  # Извлекаем список подкатегорий

        # Добавляем записи в UndercatList

        undercat_instances = []
        for undercat_id in undercats:
            try:
                undercat_instance = Undercat.objects.get(id=undercat_id)
                # Проверяем, относится ли подкатегория к указанной категории
                if undercat_instance.category_id.id != category_id:
                    raise serializers.ValidationError(
                        f"Подкатегория с id {undercat_id} не относится к категории с id {category_id}."
                    )

                undercat_instances.append(undercat_instance)

            except Undercat.DoesNotExist:
                raise serializers.ValidationError(f"Подкатегория с id {undercat_id} не существует.")

        # Возвращаем и проверяем наличие Status, Type, и Category
        try:
            validated_data['status_id'] = Status.objects.get(id=status_id)
        except Status.DoesNotExist:
            raise serializers.ValidationError(f"Статус с id {status_id} не существует.")

        try:
            validated_data['type_id'] = Type.objects.get(id=type_id)
        except Type.DoesNotExist:
            raise serializers.ValidationError(f"Тип с id {type_id} не существует.")

        try:
            validated_data['category_id'] = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError(f"Категория с id {category_id} не существует.")

        cashflow = super().create(validated_data)

        for undercat_instance in undercat_instances:
            UndercatList.objects.create(cashflow_id=cashflow, undercat_id=undercat_instance)

        return cashflow

    # Переопределяем метод update, если необходимо обновление подкатегорий
    def update(self, instance, validated_data):
        # Извлекаем переданные данные
        status_id = validated_data.pop('status_id', None)
        type_id = validated_data.pop('type_id', None)
        category_id = validated_data.pop('category_id', None)
        undercats = validated_data.pop('undercats', [])  # Список подкатегорий

        # Обновляем статус, тип, категорию, если переданы новые значения
        if status_id:
            try:
                instance.status_id = Status.objects.get(id=status_id)
            except Status.DoesNotExist:
                raise serializers.ValidationError(f"Статус с id {status_id} не существует.")

        if type_id:
            try:
                instance.type_id = Type.objects.get(id=type_id)
            except Type.DoesNotExist:
                raise serializers.ValidationError(f"Тип с id {type_id} не существует.")

        if category_id:
            try:
                instance.category_id = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise serializers.ValidationError(f"Категория с id {category_id} не существует.")

        # Обновление подкатегорий
        if undercats is not None:
            # Удаляем старые записи из UndercatList, которые не указаны в запросе
            UndercatList.objects.filter(cashflow_id=instance.id).delete()

            # Добавляем новые записи в UndercatList
            undercat_instances = []
            for undercat_id in undercats:
                try:
                    undercat_instance = Undercat.objects.get(id=undercat_id)
                    # Проверяем, относится ли подкатегория к указанной категории
                    if undercat_instance.category_id != instance.category_id:
                        raise serializers.ValidationError(
                            f"Подкатегория с id {undercat_id} не относится к категории с id {category_id}."
                        )

                    undercat_instances.append(undercat_instance)

                except Undercat.DoesNotExist:
                    raise serializers.ValidationError(f"Подкатегория с id {undercat_id} не существует.")

            # Создаем новые связи в UndercatList
            for undercat_instance in undercat_instances:
                UndercatList.objects.create(cashflow_id=instance, undercat_id=undercat_instance)

        # Обновляем другие данные
        instance.summ = validated_data.get('summ', instance.summ)
        instance.comment = validated_data.get('comment', instance.comment)

        instance.save()  # Сохраняем изменения в объекте Cashflow

        return instance


class UndercatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndercatList
        fields = '__all__'
