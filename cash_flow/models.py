from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Status(models.Model):
    """Модель для статусов денежных операций (Бизнес, личное, налог и т.д.)"""

    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название статуса"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class OperationType(models.Model):
    """Модель для типов операций (Пополнение, списание и т.д.)"""

    name = models.CharField(max_length=100, unique=True, verbose_name="Тип операции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    """Модель для категорий, привязанных к типам операций"""

    name = models.CharField(max_length=100, verbose_name="Название категории")
    operation_type = models.ForeignKey(
        OperationType, on_delete=models.CASCADE, verbose_name="Тип операции"
    )

    def __str__(self):
        return f"{self.name} ({self.operation_type})"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ("name", "operation_type")


class SubCategory(models.Model):
    """Модель для подкатегорий, привязанных к категориям"""

    name = models.CharField(max_length=100, verbose_name="Название подкатегории")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ("name", "category")


class Transaction(models.Model):
    """Основная модель для учета денежных операций"""

    created_at = models.DateField(
        default=timezone.now, verbose_name="Дата создания записи"
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    operation_type = models.ForeignKey(
        OperationType, on_delete=models.PROTECT, verbose_name="Тип операции"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.PROTECT, verbose_name="Подкатегория"
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Сумма (руб)"
    )
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.created_at} | {self.operation_type} | {self.amount} руб. | {self.status}"

    def save(self):
        if self.category.operation_type != self.operation_type:
            raise ValidationError('Выбранная категория не соответствует указанному типу операции')

        if self.subcategory.category != self.category:
            raise ValidationError('Выбранная подкатегория не соответствует указанной категории')
        super().save()

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
        ordering = ("-created_at",)
