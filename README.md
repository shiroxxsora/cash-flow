## **Гайд по запуску**
1. Создать виртуальное окружение python -m venv .venv
2. Активирум окружение .venv/Scripts/activate.ps1 (windows) source .venv/bin/activate (linux)
3. Устанавливаем зависимости pip install -r source/requirements.txt 
4. Запуск python source/manage.py runserver

Сразу созданы таблицы с некоторыми данными поэтому не нужно делать миграции.

Ниже приведена структура таблицы.
![alt text](/tables.png)

Супер пользователь по умолчанию login: root, password: admin

Если будете добавлять новые записи лучше всего залогиниться на странице your.domen/admin, your.domen по умолчанию установлен 127.0.0.1:9000

## **Документация по API**

Можно посмотреть на сайте перейдя на url */api/v1*  
Также ниже приведены эндпоинты чуть подробнее  

### ****Основные эндпоинты****

---------------------------------------
**Создание записи о ДДС**

URL: */api/v1/cashflows/*

Метод: POST  

Параметры запроса:  
status_id (int): ID статуса записи (например, "Бизнес", "Личное").  
type_id (int): ID типа записи ("Пополнение" или "Списание").  
category_id (id): ID категории записи.  
undercats (list id): Список ID подкатегорий.  
summ (digital): Сумма в формате 100.00.  
comment (string): Комментарий (необязательный).  

Пример запроса:
    
    POST /api/v1/cashflows/
    {
      "status_id": 2,
      "type_id": 1,
      "category_id": 2,
      "undercats": [3, 4],
      "summ": 1000.00,
      "comment": "Оплата за рекламу"
    }
---------------------------------------
**Обновление записи о ДДС**

URL: */api/v1/cashflows/(id)/*

Метод: PUT  

Параметры запроса:  
id (int): ID Записи.
status_id (int): ID статуса записи (например, "Бизнес", "Личное").  
type_id (int): ID типа записи ("Пополнение" или "Списание").  
category_id (id): ID категории записи.  
undercats (list id): Список ID подкатегорий.  
summ (digital): Сумма в формате 100.00.  
comment (string): Комментарий (необязательный).  

Пример запроса:
    
    PUT /api/v1/cashflows/(id)
    {
      "status_id": 1,
      "type_id": 1,
      "category_id": 1,
      "undercats": [1, 2],
      "summ": 1000.00,
      "comment": "Test"
    }
    
В случае успеха возвращается объект

Например:

    {
    "id": 4,
    "creation_time": "2025-01-20T10:13:34.614585+03:00",
    "status": {
        "id": 1,
        "name": "Бизнес"
    },
    "type": {
        "id": 1,
        "name": "Пополнение"
    },
    "category": {
        "id": 1,
        "name": "Инфраструктура"
    },
    "summ": "1000.00",
    "comment": "Test",
    "undercats_data": [
        {
            "id": 1,
            "name": "VPS",
            "category_id": 1
        },
        {
            "id": 2,
            "name": "Proxy",
            "category_id": 1
        }
      ]
    }
    
---------------------------------------
**Получение записей о ДДС**
  
URL: */api/v1/cashflows/(id)*

Метод: GET  

Параметры запроса:  
id (int): ID Записи (необязательный).

Пример запроса:
    
    GET /api/v1/cashflows/

Ответ:

    [
    {
        "id": 1,
        "creation_time": "2025-01-20T07:27:28.599703+03:00",
        "status": {
            "id": 1,
            "name": "Бизнес"
        },
        "type": {
            "id": 2,
            "name": "Списание"
        },
        "category": {
            "id": 1,
            "name": "Инфраструктура"
        },
        "summ": "123.00",
        "comment": "22",
        "undercats_data": [
            {
                "id": 1,
                "name": "VPS",
                "category_id": 1
            }
        ]
    },
    {
        "id": 2,
        "creation_time": "2025-01-20T07:03:09.748558+03:00",
        "status": {
            "id": 1,
            "name": "Бизнес"
        },
        "type": {
            "id": 1,
            "name": "Пополнение"
        },
        "category": {
            "id": 1,
            "name": "Инфраструктура"
        },
        "summ": "1.00",
        "comment": "1",
        "undercats_data": [
            {
                "id": 1,
                "name": "VPS",
                "category_id": 1
            }
        ]
    },
    {
        "id": 3,
        "creation_time": "2025-01-20T07:11:11.221735+03:00",
        "status": {
            "id": 1,
            "name": "Бизнес"
        },
        "type": {
            "id": 1,
            "name": "Пополнение"
        },
        "category": {
            "id": 1,
            "name": "Инфраструктура"
        },
        "summ": "1.00",
        "comment": "1",
        "undercats_data": [
            {
                "id": 1,
                "name": "VPS",
                "category_id": 1
            }
        ]
    },
    {
        "id": 4,
        "creation_time": "2025-01-20T07:19:33.770488+03:00",
        "status": {
            "id": 2,
            "name": "Личное"
        },
        "type": {
            "id": 2,
            "name": "Списание"
        },
        "category": {
            "id": 2,
            "name": "Маркетинг"
        },
        "summ": "100.00",
        "comment": "100",
        "undercats_data": [
            {
                "id": 3,
                "name": "Farpost",
                "category_id": 2
            },
            {
                "id": 4,
                "name": "Avito",
                "category_id": 2
            }
        ]
    },
    {
        "id": 5,
        "creation_time": "2025-01-20T07:36:39.542036+03:00",
        "status": {
            "id": 1,
            "name": "Бизнес"
        },
        "type": {
            "id": 1,
            "name": "Пополнение"
        },
        "category": {
            "id": 2,
            "name": "Маркетинг"
        },
        "summ": "500.00",
        "comment": "22",
        "undercats_data": [
            {
                "id": 3,
                "name": "Farpost",
                "category_id": 2
            }
        ]
    }
    ]
    
Пример запроса 2:
    
    GET /api/v1/cashflows/1/

Ответ:

    {
    "id": 1,
    "creation_time": "2025-01-20T07:27:28.599703+03:00",
    "status": {
        "id": 1,
        "name": "Бизнес"
    },
    "type": {
        "id": 2,
        "name": "Списание"
    },
    "category": {
        "id": 1,
        "name": "Инфраструктура"
    },
    "summ": "123.00",
    "comment": "22",
    "undercats_data": [
        {
            "id": 1,
            "name": "VPS",
            "category_id": 1
        }
    ]
    }
---------------------------------------
**Удаление записи о ДДС**
  
URL: */api/v1/cashflows/(id)*

Метод: DELETE  

Параметры запроса:  
id (int): ID Записи.

Пример запроса:
    
    DELETE /api/v1/cashflows/5/

В случае удаления:

    HTTP 204 No Content

В случае если записи небыло:

    HTTP 404 Not Found

---------------------------------------
**Создание статуса**
  
URL: */api/v1/statuses/*

Метод: POST  

Параметры запроса:  
name (string): Название статуса.

Пример запроса:

    POST /api/v1/statuses/
    {
        name: "Отменён"
    }
    
---------------------------------------
**Обновление статуса**
  
URL: */api/v1/statuses/(id)/*

Метод: PUT  

Параметры запроса:  
id (int): ID статуса.  
name (string): Название статуса.

Пример запроса:

    PUT /api/v1/statuses/2/
    {
        name: "Отменён"
    }

---------------------------------------
**Получение статуса**
  
URL: */api/v1/statuses/(id)/*

Метод: GET  

Параметры запроса:  
id (string): ID статуса (не обязательно).

Пример запроса:

    GET /api/v1/statuses/

Ответ:

    [
    {
        "id": 1,
        "name": "Бизнес"
    },
    {
        "id": 2,
        "name": "Личное"
    },
    {
        "id": 6,
        "name": "Налог"
    }
    ]

Пример запроса 2:

    GET /api/v1/statuses/1

Ответ:

    {
        "id": 1,
        "name": "Бизнес"
    }
    
---------------------------------------
**Удаление статуса**
  
URL: */api/v1/statuses/(id)*

Метод: DELETE  

Параметры запроса:  
id (int): ID статуса.

Пример запроса:
    
    DELETE /api/v1/statuses/1

В случае удаления:

    HTTP 204 No Content

В случае если записи небыло:

    HTTP 404 Not Found

---------------------------------------
**Создание типа**
  
URL: */api/v1/types/*

Метод: POST  

Параметры запроса:  
name (string): Название типа.

Пример запроса:

    POST /api/v1/types/
    {
        name: "Возврат"
    }
    
---------------------------------------
**Обновление типа**
  
URL: */api/v1/types/(id)/*

Метод: PUT  

Параметры запроса:  
id (int): ID типа.  
name (string): Название типа.

Пример запроса:

    PUT /api/v1/types/2/
    {
        name: "Возврат"
    }

---------------------------------------
**Получение типа**
  
URL: */api/v1/types/(id)/*

Метод: GET  

Параметры запроса:  
id (string): ID типа (не обязательно).

Пример запроса:

    GET /api/v1/types/

Ответ:

    [
    {
        "id": 1,
        "name": "Пополнение"
    },
    {
        "id": 2,
        "name": "Списание"
    }
    ]

Пример запроса 2:

    GET /api/v1/types/1

Ответ:

    {
        "id": 1,
        "name": "Пополнение"
    }
    
---------------------------------------
**Удаление типа**
  
URL: */api/v1/types/(id)*

Метод: DELETE  

Параметры запроса:  
id (int): ID типа.

Пример запроса:
    
    DELETE /api/v1/types/1

В случае удаления:

    HTTP 204 No Content

В случае если записи небыло:

    HTTP 404 Not Found

---------------------------------------
**Создание категории**
  
URL: */api/v1/categories/*

Метод: POST  

Параметры запроса:  
name (string): Название категории.

Пример запроса:

    POST /api/v1/categories/
    {
        name: "Зарплата"
    }
    
---------------------------------------
**Обновление категории**
  
URL: */api/v1/categories/(id)/*

Метод: PUT  

Параметры запроса:  
id (int): ID категории.  
name (string): Название категории.

Пример запроса:

    PUT /api/v1/categories/2/
    {
        name: "Зарплата"
    }

---------------------------------------
**Получение категории**
  
URL: */api/v1/categories/(id)/*

Метод: GET  

Параметры запроса:  
id (string): ID категории (не обязательно).

Пример запроса:

    GET /api/v1/categories/

Ответ:

    [
    {
        "id": 1,
        "name": "Инфраструктура"
    },
    {
        "id": 2,
        "name": "Маркетинг"
    }
    ]

Пример запроса 2:

    GET /api/v1/categories/1

Ответ:

    {
        "id": 1,
        "name": "Инфраструктура"
    }
    
---------------------------------------
**Удаление категории**
  
URL: */api/v1/categories/(id)*

Метод: DELETE  

Параметры запроса:  
id (int): ID категории.

Пример запроса:
    
    DELETE /api/v1/categories/1

В случае удаления:

    HTTP 204 No Content

В случае если записи небыло:

    HTTP 404 Not Found

---------------------------------------
**Создание подкатегории**
  
URL: */api/v1/undercats/*

Метод: POST  

Параметры запроса:  
name (string): Название подкатегории.
category_id (int) : ID Категории

Пример запроса:

    POST /api/v1/undercats/
    {
        name: "HH",
        category_id: 2
    }
    
---------------------------------------
**Обновление подкатегории**
  
URL: */api/v1/undercats/(id)/*

Метод: PUT  

Параметры запроса:  
id (int): ID подкатегории.  
name (string): Название подкатегории.
category_id (int) : ID Категории

Пример запроса:

    PUT /api/v1/undercats/4/
    {
        name: "HH",
        category_id: 2
    }

---------------------------------------
**Получение подкатегории**
  
URL: */api/v1/undercats/(id)/*

Метод: GET  

Параметры запроса:  
id (string): ID подкатегории (не обязательно).

Пример запроса:

    GET /api/v1/undercats/

Ответ:

    [
    {
        "id": 1,
        "name": "VPS",
        "category_id": 1
    },
    {
        "id": 2,
        "name": "Proxy",
        "category_id": 1
    },
    {
        "id": 3,
        "name": "Farpost",
        "category_id": 2
    },
    {
        "id": 4,
        "name": "Avito",
        "category_id": 2
    }
    ]

Пример запроса 2:

    GET /api/v1/undercats/1

Ответ:

    {
        "id": 1,
        "name": "VPS",
        "category_id": 1
    }
    
---------------------------------------
**Удаление подкатегории**
  
URL: */api/v1/undercats/(id)*

Метод: DELETE  

Параметры запроса:  
id (int): ID подкатегории.

Пример запроса:
    
    DELETE /api/v1/undercats/1

В случае удаления:

    HTTP 204 No Content

В случае если записи небыло:

    HTTP 404 Not Found

---------------------------------------
**Создание записи в таблица пересечения подкатегории и записи ДДС**

URL: */api/v1/undercat-lists/*

Метод: POST  

Параметры запроса:  
cashflow_id (int) : ID Записи ДДС
undercat_id (int) :  ID Подкатегории

Пример запроса:

    POST /api/v1/undercat-lists/
    {
        "cashflow_id": 1,
        "undercat_id": 1
    }

Ответ:

    {
        "id": 22,  // ID записи в таблице пересечения
        "cashflow_id": 1,
        "undercat_id": 1
    }

---------------------------------------
**Удаление записи в таблица пересечения подкатегории и записи ДДС**

URL: */api/v1/undercat-lists/(id)/*

Метод: DELETE  

Параметры запроса:  
id (int) : ID Записи таблицы пересечения  

Пример запроса:
    
    DELETE /api/v1/undercat-lists/22

В случае удаления:

    HTTP 204 No Content

В случае если записи небыло:

    HTTP 404 Not Found
