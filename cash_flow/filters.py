import django_filters

from .models import Category, OperationType, Status, SubCategory, Transaction


class TransactionFilter(django_filters.FilterSet):
    """Класс для фильтрации модели Transaction"""

    date_range = django_filters.DateFromToRangeFilter(
        field_name="created_at",
        label="Период дат",
        widget=django_filters.widgets.RangeWidget(attrs={"type": "date"}),
    )
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        empty_label="Все статусы",
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
