### Проект YaCut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Технологии

1. Python 3.7.9
2. Flask 2.0.2
3. REST API

## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```
```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```
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

Запустить FLASK
```
flask run
```

Проект будет доступен по ссылке http://127.0.0.1:5000/

## Работа с API. Примеры использования

1. http://127.0.0.1:5000/api/id/ — POST-запрос на создание новой короткой ссылки.

Пример 1:

```
# Запрос:
{
  "url": "https://practicum.yandex.ru/",
  "custom_id": "qwerty1"
}

# Ответ:
{
  "url": "https://practicum.yandex.ru/",
  "short_link": "http://127.0.0.1:5000/qwerty1"
}
```

Пример 2:
```
# Запрос:
{
  "url": "https://practicum.yandex.ru/",
  "custom_id": "бла-бла-бла"
}

# Ответ:
{
  "message": "Указано недопустимое имя для короткой ссылки"
}
```

Пример 3:
```
# Запрос:
{
  "url": "https://practicum.yandex.ru/",
}

# Ответ:
{
  "url": "https://practicum.yandex.ru/",
  "short_link": "http://127.0.0.1:5000/ie58Hj"
}
```

2. http://127.0.0.1:5000/api/id/<short_id>/ - GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Пример 1:

```
# Запрос:
http://127.0.0.1:5000/api/id/ie58Hj/

# Ответ:
{
  "url": "https://practicum.yandex.ru/"
}
```

Пример 2:

```
# Запрос:
http://127.0.0.1:5000/api/id/XXXXXX/

# Ответ:
{
  "message": "Указанный id не найден"
}
```

## Разработчик
Батова Ольга, [@olgabato](https://t.me/olgabato)
