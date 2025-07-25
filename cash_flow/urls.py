from django.urls import path

from cash_flow import views
from cash_flow.views import load_categories, load_subcategories

urlpatterns = [
    path("transactions/", views.TransactionListView.as_view(), name="transactions"),
    path(
        "transactions/create/",
        views.TransactionCreateView.as_view(),
        name="transaction_create",
    ),
    path(
        "transactions/update/<int:pk>/",
        views.TransactionUpdateView.as_view(),
        name="transaction_update",
    ),
    path(
        "transactions/delete/<int:pk>/",
        views.TransactionDeleteView.as_view(),
        name="transaction_delete",
    ),
    path("references/", views.ReferencesTemplateView.as_view(), name="references"),
    path("statuses/", views.StatusListView.as_view(), name="statuses"),
    path("statuses/create/", views.StatusCreateView.as_view(), name="status_create"),
    path(
        "statuses/update/<int:pk>/",
        views.StatusUpdateView.as_view(),
        name="status_update",
    ),
    path(
        "statuses/delete/<int:pk>/",
        views.StatusDeleteView.as_view(),
        name="status_delete",
    ),
    path(
        "operation_types/",
        views.OperationTypeListView.as_view(),
        name="operation_types",
    ),
    path(
        "operation_types/create/",
        views.OperationTypeCreateView.as_view(),
        name="operation_type_create",
    ),
    path(
        "operation_types/update/<int:pk>/",
        views.OperationTypeUpdateView.as_view(),
        name="operation_type_update",
    ),
    path(
        "operation_types/delete/<int:pk>/",
        views.OperationTypeDeleteView.as_view(),
        name="operation_type_delete",
    ),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path(
        "categories/create/", views.CategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "categories/update/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/delete/<int:pk>/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("subcategories/", views.SubCategoryListView.as_view(), name="subcategories"),
    path(
        "subcategories/create/",
        views.SubCategoryCreateView.as_view(),
        name="subcategory_create",
    ),
    path(
        "subcategories/update/<int:pk>/",
        views.SubCategoryUpdateView.as_view(),
        name="subcategory_update",
    ),
    path(
        "subcategories/delete/<int:pk>/",
        views.SubCategoryDeleteView.as_view(),
        name="subcategory_delete",
    ),
    path("ajax/load-categories/", load_categories, name="load_categories"),
    path("ajax/load-subcategories/", load_subcategories, name="load_subcategories"),
]
