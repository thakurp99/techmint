# expenses/urls.
from django.urls import path
from .views import UserListCreateView, ExpenseListCreateView, BalanceListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('balances/', BalanceListCreateView.as_view(), name='balance-list-create'),
]
