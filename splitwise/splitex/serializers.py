# expenses/serializers.py
from rest_framework import serializers
from .models import User, Expense, Balance, PassbookEntry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class PassbookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PassbookEntry
        fields = '__all__'
