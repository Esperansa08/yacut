# YaCut
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)

Это проект создающий короткие ссылки на веб-ресурcы.
Проект создан с применением фреймворка Flask и SQLAlchemy.
Доступ осуществляется через веб-сайт или посредством API.
Спецификация API находится в файле openapi.yml

## Ключевые возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Доступны web и api интерфейсы.

## Как установить программу

Системные требования:

- Python==3.7.9
- sqlalchemy==1.4.29
- flask==2.0.2

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Esperansa08/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запустить программу:

```
flask run
```

## Автор 

 * Савельева Анастасия (Visteria09@yandex.ru, https://github.com/Esperansa08) 
