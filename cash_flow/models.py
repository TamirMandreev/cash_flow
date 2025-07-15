from django.db import models
from django.template.defaultfilters import first
from django.utils import timezone


class Status(models.Model):
    '''Модель для статусов денежных операций (Бизнес, личное, налог и т.д.)'''
    name = models.CharField(max_length=100, unique=True, verbose_name='Название статуса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class OperationType(models.Model):
    '''Модель для типов операций (Пополнение, списание и т.д.)'''
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип операции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип операции'
        verbose_name_plural = 'Типы операций'


class Category(models.Model):
    '''Модель для категорий, привязанных к типам операций'''
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE, verbose_name='Тип операции')

    def __str__(self):
        return f'{self.name} ({self.operation_type})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # Сделать комбинацию указанных полей уникальной
        unique_together = ('name', 'operation_type')


class SubCategory(models.Model):
    '''Модель для подкатегорий, привязанных к категориям'''
    name = models.CharField(max_length=100, verbose_name='Название подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        # Сделать комбинацию указанных полей уникальной
        unique_together = ('name', 'category')


class Transaction(models.Model):
    '''Основная модель для учета денежных операций'''
    # Дата создания записи
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания записи')
    # Статус
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    # Тип операции
    operation_type = models.ForeignKey(OperationType, on_delete=models.PROTECT, verbose_name='Тип операции')
    # Категория
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    # Подкатегория
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='Подкатегория')
    # Сумма
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма (руб)')
    # Комментарий
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий', help_text='Необязательное поле')

    def __str__(self):
        return f'{self.created_at} | {self.operation_type} | {self.amount} руб. | {self.status}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ('-created_at',)