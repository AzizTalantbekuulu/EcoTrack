# EcoTrack Project

## Описание проекта
EcoTrack - это платформа для мониторинга и управления данными об окружающей среде от различных датчиков и устройств. Этот проект включает в себя RESTful API для управления списком датчиков качества воздуха.
## Используемые технологии
- Python
- Django
- Django REST Framework
- Django REST Framework SimpleJWT
- PostgreSQL

## Установка
1. Клонируйте репозиторий:
```bash
   git clone https://github.com/AzizTalantbekuulu/EcoTrack.git
```
2. Установите зависимости:
```bash
   pip install -r requirements.txt
```
3. Создайте базу данных PostgreSQL и настройте соединение в файле settings.py.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your_DB_name',
        'USER': 'Your_username',
        'PASSWORD': 'Your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
4. Выполните миграции:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```
## Использование

### Аутентификация
Для доступа к защищенным эндпоинтам необходимо получить токен аутентификации, используя эндпоинт `/api/token/`.

### Эндпоинты API

- **Регистрация нового пользователя:** `POST /eco/register/`
- **Логин пользователя:** `POST /eco/login/`
- **Получение нового доступного токена:** `POST /eco/token/refresh/`
- **Пользователи:**
  - `GET /eco/users/`
  - `POST /eco/users/`
  - `GET /eco/users/<user_id>/`
  - `PUT /eco/users/<user_id>/`
  - `PATCH /eco/users/<user_id>/`
  - `DELETE /eco/users/<user_id>/`
- **Датчики:**
  - `GET /eco/sensor/`
  - `POST /eco/sensor/`
  - `GET /eco/sensor/<sensor_id>/`
  - `PUT /eco/sensor/<sensor_id>/`
  - `PATCH /eco/sensor/<sensor_id>/`
  - `DELETE /eco/sensor/<sensor_id>/`
- **Данные для датчиков:**
  - `GET /eco/sensor/<sensor_id>/data/`
  - `POST /eco/sensor/<sensor_id>/data/`
  - `GET /eco/sensor/<sensor_id>/data/<data_id>/`
  - `PUT /eco/sensor/<sensor_id>/data/<data_id>/`
  - `PATCH /eco/sensor/<sensor_id>/data/<data_id>/`
  - `DELETE /eco/sensor/<sensor_id>/data/<data_id>/`
- **Оповещения:**
  - `GET /eco/sensor/<sensor_id>/alerts/`
  - `POST /eco/sensor/<sensor_id>/alerts/`
  - `GET /eco/sensor/<sensor_id>/alerts/<alerts_id>/`
  - `PUT /eco/sensor/<sensor_>/alerts/<alerts_id>/`
  - `PATCH /eco/sensor/<sensor_id>/alerts/<alerts_id>/`
  - `DELETE /eco/sensor/<sensor_id>/alerts/<alerts_id>/`

Каждый эндпоинт требует аутентификации через токен. Для этого в заголовках запроса необходимо указать `Authorization: Bearer <access_token>`.

## Github
- https://github.com/AzizTalantbekuulu/EcoTrack

