from django.urls import path
from cash_flow import views

urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name='transactions' ),
    path('transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create' ),
    path('transactions/update/<int:pk>/', views.TransactionUpdateView.as_view(), name='transaction_update' ),
    path('transactions/delete/<int:pk>/', views.TransactionDeleteView.as_view(), name='transaction_delete' ),

    path('references/', views.ReferencesTemplateView.as_view(), name='references' ),

    path('statuses/', views.StatusListView.as_view(), name='statuses' ),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('statuses/update/<int:pk>/', views.StatusUpdateView.as_view(), name='status_update'),
    path('statuses/delete/<int:pk>/', views.StatusDeleteView.as_view(), name='status_delete'),
]