# Generated by Django 5.1.4 on 2025-01-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlog', '0004_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lactose',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Lactose'),
        ),
    ]
