import django_filters

from .models import Category, OperationType, Status, SubCategory, Transaction


class TransactionFilter(django_filters.FilterSet):
    """Класс для фильтрации модели Transaction"""

    # Добавить фильтрацию по диапазонам дат
    date_range = django_filters.DateFromToRangeFilter(  # DateFromToRangeFilter - фильтр для работы с диапазоном дат
        field_name="created_at",  # Указываем по какому полю выполнять фильтрацию
        label="Период дат",  # Задаем человекочитаемую метку для поля формы. Если не указать, будет использовано имя "date_range"
        widget=django_filters.widgets.RangeWidget(  # Определяем виджет для отображения. RangeWidget - специальный виджет для диапазонов значений
            attrs={"type": "date"}  # Делаем поля ввода типа "дата"
        ),
    )
    #
    status = django_filters.ModelChoiceFilter(  # ModelChoiceFilter - фильтр для выбора значения из связанной модели (Создает выпадающий список со всеми возможными статусами)
        queryset=Status.objects.all(),  # Откуда брать варианты для выпадающего списка
        empty_label="Все статусы",  # Добавляет пустой вариант в начало списка
    )

    operation_type = django_filters.ModelChoiceFilter(
        queryset=OperationType.objects.all(), empty_label="Все типы"
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(), empty_label="Все категории"
    )

    subcategory = django_filters.ModelChoiceFilter(
        queryset=SubCategory.objects.all(), empty_label="Все подкатегории"
    )

    class Meta:
        model = Transaction
        fields = []
