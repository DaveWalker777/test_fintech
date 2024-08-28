# Тестовое задание на финтех разработчика

Этот проект представляет собой веб-приложение на Django для управления заказами и предметами, с интеграцией Stripe для обработки платежей. Приложение развернуто с помощью Docker и использует Nginx в качестве веб-сервера.

# Стек технологий

- Django, DRF
- PostgreSQL, pgAdmin
- Stripe
- HTML
- Docker, docker-compose
- Nginx
- Github Actions CI/CD

# Установка и запуск

## 1. Простой способ
Приложение некоторе время будет развёрнуто на моём собственном хостинге https://www.davewalker.ru/ и доступно к 
использованию. В БД имеется несколько тестовых данных и готовый суперпользователь.

### Данные суперпользователя
- **URL:** https://www.davewalker.ru/admin
- **Пользователь:** `test`
- **Пароль:** `test`

### Данные для pgAdmin 
- **URL:** http://www.davewalker.ru:5050
- **Вход:**
  - **Email:** `testfintech@yandex.ru`
  - **Пароль:** `testpassword`
- **Подключение:**
  - **Имя/адрес сервера:** `db`
  - **Порт:** `5432`
  - **Служебная БД:** `fintech`
  - **Имя пользователя:** `test`
  - **Пароль:** `testpassword`
  

## 2. Клонирование
```
git clone https://github.com/DaveWalker777/test_fintech.git
cd test_fintech
```

### Настройка
В файле /test_fintech/test_fintech/settings.py в строке ALLOWED_HOSTS добавить 'localhost'
### Запуск контейнеров
``` 
docker-compose up --build
```
### Миграции и сбор статики
``` 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
```
### Создание суперпользователя
``` 
docker-compose exec web python manage.py createsuperuser
```
### Создание переменных окружения
Создайте файл /test_fintech/.env

Укажите следующие переменные:
``` 
STRIPE_SECRET_KEY=''
STRIPE_PUBLIC_KEY=''
DJANGO_SECRET_KEY=''

POSTGRES_USER=''
POSTGRES_PASSWORD=''
POSTGRES_DB=''
PGADMIN_DEFAULT_EMAIL=''
PGADMIN_DEFAULT_PASSWORD=''
```

# Выполненные задания
### 1. Реализован Django + Stripe API бэкенд 

### 2. Созданы модели Item, Order, Discount, Tax

### 3. Реализованы методы API GET /buy/{id} и GET /item/{id}

### 4. Использован Docker и docker-compose

### 5. Использована библиотека dotenv для сокрытия секретных ключей через переменные окружения

### 6. Все модели доступны к просмотру в админ-панели

### 7. Приложение запущено на удаленном сервере с возможностью тестирования, используются Nginx и Gunicorn

### 8. Модель Order объединяет несколько Item и позволяет совершить платёж по общей стоимости

### 9. Модели Discount и Tax прикрепляются к Order и позволяют модифицировать конечную стоимость заказа

### 10. Реализован ввод валюты item.currency, изначально указан USD. В 2 ключах Stripe нет нужды (?), можно подвязывать на один. 

### 11. Реализована обработка ошибки в том случае, если в Order добавлены несколько Item с различной валютой

### 12. Реализованы Stripe Session и Stripe Payment Intent. Сессия используется для одиночных предметов (по запросу к методу GET /item/{id}). Для Order используется Payment Intent.

### Дополнительно: реализовано CI/CD при помощи Github Actions

# Использование 

Проверка работоспособности методов API:

- https://www.davewalker.ru/item/1/ 
- https://www.davewalker.ru/buy/1/

Проверка Order'а:
- https://www.davewalker.ru/order/3/

Тестовые данные карты:
```
4242 4242 4242 4242
ММ/ГГ - любая будущая дата
CVC - любые 3 цифры
```
В случае успешного выполнения запроса (покупки), клиент будет перенаправлен на страницу Success и получит уведомление.