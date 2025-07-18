from django.urls import path
from cash_flow import views

urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transactions' ),
    path('transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create' ),
    path('transactions/update/<int:pk>/', views.TransactionUpdateView.as_view(), name='transaction_update' ),
]