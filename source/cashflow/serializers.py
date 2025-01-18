from rest_framework import serializers
from .models import Cashflow


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = (
            'creation_time',
            'status_id',
            'type_id',
            'category_id',
            'summ',
            'comment'
        )
