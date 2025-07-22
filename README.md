## Тестовое задание 

### Веб-сервис для управления движением денежныхсредств (ДДС)

### Автор: Тамир Мандреев  

Условия задания: https://drive.google.com/file/d/1vbPk2aiMe52pDFW57zMUDMaW7rqrHypc/view

1. Клонировать репозиторий  
2. Загрузить данные из фикстуры 
- python3 manage.py loaddata cash_flow.json
3. Создать и применить миграции 
- python3 manage.py makemigrations
- python3 manage.py migrate
4. Перейти на страницу http://localhost:8000/references/
