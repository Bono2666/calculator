# Generated by Django 5.0.1 on 2024-03-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_order_souvenir_alter_orderpackage_box_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='package_price',
            new_name='female_price',
        ),
        migrations.AddField(
            model_name='orderpackage',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='male_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderpackage',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]