# Generated by Django 4.2.6 on 2023-11-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_closing'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='budget',
            constraint=models.UniqueConstraint(fields=('budget_id', 'budget_month', 'budget_year'), name='unique_budget'),
        ),
    ]
