# expenses/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_paid')
    participants = models.ManyToManyField(User, related_name='expenses_shared')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.date}"

class Balance(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debts')
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.debtor} owes {self.amount} to {self.creditor}"

@receiver(post_save, sender=Balance)
def update_balances(sender, instance, **kwargs):
    # Update balances after each transaction
    instance.debtor.balance -= instance.amount
    instance.creditor.balance += instance.amount
    instance.debtor.save()
    instance.creditor.save()


class PassbookEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed
