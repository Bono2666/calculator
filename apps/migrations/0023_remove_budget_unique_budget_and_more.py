# Generated by Django 4.2.6 on 2023-11-17 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_budgetdetail_budget_month_budgetdetail_budget_year'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='budget',
            name='unique_budget',
        ),
        migrations.RemoveField(
            model_name='budgetdetail',
            name='budget_month',
        ),
        migrations.RemoveField(
            model_name='budgetdetail',
            name='budget_year',
        ),
    ]
