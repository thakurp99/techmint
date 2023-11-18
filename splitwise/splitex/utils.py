# utils.py
from splitex.models import Balance

def simplify_all_balances():
    """
    Simplify all balances by consolidating debts and credits.
    """
    balances = Balance.objects.exclude(amount=0)

    for balance in balances:
        balance.simplify_balance()
