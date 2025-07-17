from django.contrib import admin

from .models import Transaction, Status, OperationType, Category, SubCategory


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'operation_type', 'category', 'subcategory', 'amount', 'comment')
    list_filter = ('created_at', 'status', 'operation_type', 'category', 'subcategory')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'operation_type')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')