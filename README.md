# Cash Flow Management Service

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Веб-сервис для учета и анализа денежных операций с минимальным пользовательским интерфейсом

## 📌 О проекте

Приложение позволяет: 
- Вести учет денежных операций (транзакций)
- Анализировать расходы и доходы 
- Фильтровать транзакции по различным параметрам 

Основные элементы транзакций: 
- **Статус**: Бизнес, Личное, Налог 
- **Тип**: Пополнение, списание 
- **Категории**:
  - Инфраструктура (подкатегории: VPS, Proxy)
  - Маркетинг (подкатегории: Farpost, Avito)

## 🚀 Установка и запуск
1. Клонируйте репозиторий 
```bash
$ git clone https://github.com/TamirMandreev/cash_flow
$ cd cash_flow
```
2. Установите зависимости 
```bash
$ poetry install
```
3. Примените миграции 
```bash
python manage.py migrate
```
4. Загрузите данные из фикстуры 
```bash
python manage.py loaddata cash_flow.json
```
5. Запустите сервер 
```bash
python manage.py runserver
```
6. Откройте в браузере http://localhost:8000/references/

## 🖥️ Интерфейс
Главная страница содержит:
- Таблицу всех транзакций
- Возможность создания/редактирования/удаления записей 
- Фильтры по:
  - Дате 
  - Статусу 
  - Типу операции 
  - Категории и подкатегории
  
## 📂 Структура проекта
```text
cash_flow/
├── cash_flow/         # Основное приложение
├── config/            # Файлы конфигурации
├── static/            # Статические файлы (CSS, JS)
├── manage.py          # Управляющий скрипт
└── pyproject.toml     # Зависимости
```
