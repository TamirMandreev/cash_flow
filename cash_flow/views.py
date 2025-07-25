from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from cash_flow import services
from cash_flow.filters import TransactionFilter
from cash_flow.models import (Category, OperationType, Status, SubCategory,
                              Transaction)


def load_categories(request):
    """Представление для обработки AJAX-запроса"""
    operation_type_id = request.GET.get("operation_type_id")
    categories = services.load_categories(operation_type_id)
    context = {"categories": categories}
    options = render_to_string("cash_flow/category_dropdown_list_options.html", context)
    return JsonResponse({"options": options})


def load_subcategories(request):
    """Представление для обработки AJAX-запроса"""
    category_id = request.GET.get("category_id")
    subcategories = services.load_subcategories(category_id)
    context = {"subcategories": subcategories}
    options = render_to_string(
        "cash_flow/subcategory_dropdown_list_options.html", context
    )
    return JsonResponse({"options": options})


class TransactionListView(ListView):
    """Представление для отображения списка транзакций"""

    model = Transaction
    template_name = "cash_flow/transaction_list.html"
    context_object_name = "transactions"
    filterset_class = TransactionFilter

    def get_queryset(self):
        """
        Получает набор данных из базы данных, который будет использован в представлении
        :return:
        """
        queryset = (
            super()
            .get_queryset()
            .select_related(
                "status",
                "operation_type",
                "category",
                "subcategory",
            )
        )
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        """
        Расширяет стандартный контекст представления, добавляя ссылку на фильтр
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context


class TransactionCreateView(CreateView):
    """Представление для создания транзакции"""

    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("transactions")

    def get_form(self, form_class=None):
        """Кастомизирует форму"""
        form = super().get_form(form_class)
        return services.prepare_transaction_form_fields(form)


class TransactionUpdateView(UpdateView):
    """Представление для обновления транзакции"""

    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("transactions")


class TransactionDeleteView(DeleteView):
    """Представление для удаления транзакции"""

    model = Transaction
    success_url = reverse_lazy("transactions")


class ReferencesTemplateView(TemplateView):
    """Представление для отображения справочников"""

    template_name = "cash_flow/references.html"


class StatusListView(ListView):
    """Представление для отображения списка статусов"""

    model = Status
    template_name = "cash_flow/status_list.html"
    context_object_name = "statuses"


class StatusCreateView(CreateView):
    """Представление для создания статуса"""

    model = Status
    fields = "__all__"
    success_url = reverse_lazy("statuses")


class StatusUpdateView(UpdateView):
    """Представление для обновления статуса"""

    model = Status
    fields = "__all__"
    success_url = reverse_lazy("statuses")


class StatusDeleteView(DeleteView):
    """Представление для удаления статуса"""

    model = Status
    success_url = reverse_lazy("statuses")


class OperationTypeListView(ListView):
    """Представление для отображения списка типов операций"""

    model = OperationType
    template_name = "cash_flow/operation_type_list.html"
    context_object_name = "operation_types"


class OperationTypeCreateView(CreateView):
    """Представление для создания типа операции"""

    model = OperationType
    fields = "__all__"
    success_url = reverse_lazy("operation_types")


class OperationTypeUpdateView(UpdateView):
    """Представление для обновления типа операции"""

    model = OperationType
    fields = "__all__"
    success_url = reverse_lazy("operation_types")


class OperationTypeDeleteView(DeleteView):
    """Представление для удаления типа операции"""

    model = OperationType
    success_url = reverse_lazy("operation_types")


class CategoryListView(ListView):
    """Представление для отображения списка категорий"""

    model = Category
    template_name = "cash_flow/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    """Представление для создания категории"""

    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories")


class CategoryUpdateView(UpdateView):
    """Представление для обновления категории"""

    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories")


class CategoryDeleteView(DeleteView):
    """Представление для удаления категории"""

    model = Category
    success_url = reverse_lazy("categories")


class SubCategoryListView(ListView):
    """Представление для отображения списка подкатегорий"""

    model = SubCategory
    template_name = "cash_flow/subcategory_list.html"
    context_object_name = "subcategories"


class SubCategoryCreateView(CreateView):
    """Представление для создания подкатегории"""

    model = SubCategory
    fields = "__all__"
    success_url = reverse_lazy("subcategories")


class SubCategoryUpdateView(UpdateView):
    """Представление для обновления подкатегории"""

    model = SubCategory
    fields = "__all__"
    success_url = reverse_lazy("subcategories")


class SubCategoryDeleteView(DeleteView):
    """Представление для удаления подкатегории"""

    model = Category
    success_url = reverse_lazy("categories")
