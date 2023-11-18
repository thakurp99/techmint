# expenses/views.py
from rest_framework import generics
from .models import User, Expense, Balance, update_balances
from .serializers import UserSerializer, ExpenseSerializer, BalanceSerializer, PassbookEntrySerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class BalanceListCreateView(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

    def perform_create(self, serializer):
        transaction = serializer.save()
        update_balances(transaction)


class PassbookEntryListView(generics.ListAPIView):
    serializer_class = PassbookEntrySerializer
