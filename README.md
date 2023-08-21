# YaCut
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=flat&logo=jinja&logoColor=black)
![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=black)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)

Это проект создающий короткие ссылки на веб-ресурcы.
Проект создан с применением фреймворка Flask и SQLAlchemy.

Доступ осуществляется через веб-сайт или посредством API.
Спецификация API находится в файле openapi.yml

### Содержание: 
- [YaCut](#yacut)
    - [Содержание:](#содержание)
  - [Ключевые возможности сервиса](#ключевые-возможности-сервиса)
  - [Как установить программу](#как-установить-программу)
  - [Пример запросов](#пример-запросов)
  - [Автор](#автор)

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
## Пример запросов

POST запрос
```
http://127.0.0.1:5000/api/1/
```
Request
```
{ "url": "https://018-algoritmy-i-struktury-dannyh"}
```
Response
```
{
    "short_link": "http://127.0.0.1:5000/Zysj48",
    "url": "https://018-algoritmy-i-struktury-dannyh"
}
```
GET запрос
```
http://127.0.0.1:5000/api/id/vRxach/
```
Request
```
{ "custom_id": "vRxach" }
```
Response
```
{"url": "https://romansementsov.ru/%D0%9A%D1%83%D1%80%D1%81%D1%8B_%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B_%D0%94%D0%B0%D0%BD%D0%BD%D1%8B%D1%85/"}
```

## Автор 

 * Савельева Анастасия (Visteria09@yandex.ru, https://github.com/Esperansa08) 
