# Generated by Django 5.1.4 on 2025-01-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlog', '0006_rename_lactose_product_lactose_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lactose_free',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Lactose free'),
        ),
    ]
