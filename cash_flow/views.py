from django.shortcuts import render

from django.views.generic import ListView

from cash_flow.filters import TransactionFilter
from cash_flow.models import Transaction


class TransactionListView(ListView):
    '''Представление для отображения списка транзакций'''
    model = Transaction
    template_name = 'cash_flow/transaction_list.html'
    context_object_name = 'transactions'
    # Указать класс фильтра, который будет обрабатывать параметры запроса
    filterset_class = TransactionFilter # TransactionFilter - кастомный класс фильтра

    def get_queryset(self):
        # Получить все объекты модели Transaction + все связанные данные
        queryset = super().get_queryset().select_related(
            'status',
            'operation_type',
            'category',
            'subcategory',
        )
        # Применить фильтр. В TransactionFilter передаем параметры из URL (self.request.GET) и queryset
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Возвратить результат фильтрации
        return self.filterset.qs

    # Передать фильтр в шаблон
    def get_context_data(self, **kwargs):
        # Берем стандартные данные, которые Django уже подготовил
        context = super().get_context_data(**kwargs)
        # Добавляем наш фильтр в эти данные под ключом 'filter'. filterset определяется в методе get_queryset
        context['filter'] = self.filterset
        # Возвращаем обновленный набор данных
        return context


