# Generated by Django 4.2.4 on 2023-09-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_cabang_alamat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
    ]
