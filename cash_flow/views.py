from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from cash_flow.filters import TransactionFilter
from cash_flow.models import Transaction, Status, OperationType, Category, SubCategory


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


class TransactionCreateView(CreateView):
    '''Представление для создания транзакции'''
    model = Transaction
    # Поля, которые будут отображться в форме
    fields = '__all__'
    # Куда пользователь будет перенаправлен после успешной отправки формы
    success_url = reverse_lazy('transactions')


class TransactionUpdateView(UpdateView):
    '''Представление для обновления транзакции'''
    model = Transaction
    fields = '__all__'
    success_url = reverse_lazy('transactions')


class TransactionDeleteView(DeleteView):
    '''Представление для удаления транзакции'''
    model = Transaction
    success_url = reverse_lazy('transactions')


class ReferencesTemplateView(TemplateView):
    '''Представление для отображения справочников'''
    template_name = 'cash_flow/references.html'


class StatusListView(ListView):
    '''Представление для отображения списка статусов'''
    model = Status
    template_name = 'cash_flow/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    '''Представление для создания статуса'''
    model = Status
    fields = '__all__'
    success_url = reverse_lazy('statuses')


class StatusUpdateView(UpdateView):
    '''Представление для обновления статуса'''
    model = Status
    fields = '__all__'
    success_url = reverse_lazy('statuses')


class StatusDeleteView(DeleteView):
    '''Представление для удаления статуса'''
    model = Status
    success_url = reverse_lazy('statuses')

