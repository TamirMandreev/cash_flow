from django.urls import path
from cash_flow import views

urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transactions' ),
]