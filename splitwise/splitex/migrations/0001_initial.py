# Generated by Django 4.2.2 on 2023-11-18 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassbookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splitex.user')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('participants', models.ManyToManyField(related_name='expenses_shared', to='splitex.user')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses_paid', to='splitex.user')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='splitex.user')),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debts', to='splitex.user')),
            ],
        ),
    ]
