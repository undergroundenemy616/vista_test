# Generated by Django 3.1.1 on 2021-03-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201011_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.TextField(verbose_name='Цвет тега'),
        ),
    ]
