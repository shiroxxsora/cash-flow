**Гайд по запуску**
1. Создать виртуальное окружение python -m venv .venv
2. Активирум окружение .venv/Scripts/activate.ps1 (windows) source .venv/bin/activate (linux)
3. Устанавливаем зависимости pip install -r source/requirements.txt 
4. Запуск python source/manage.py runserver

Сразу созданы таблицы с некоторыми данными поэтому не нужно делать миграции.

Ниже приведена структура таблицы.
![alt text](/tables.png)

Супер пользователь по умолчанию login: root, password: admin

Если будете добавлять новые записи лучше всего залогиниться на странице your.domen/admin, your.domen по умолчанию установлен 127.0.0.1:9000

Документация по API
