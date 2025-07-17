from django.shortcuts import render

from django.views.generic import ListView

from cash_flow.models import Transaction


class TransactionListView(ListView):
    '''Представление для отображения списка транзакций'''
    model = Transaction
    template_name = 'cash_flow/transaction_list.html'
    context_object_name = 'transactions'

