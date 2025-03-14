# Generated by Django 5.1.4 on 2025-01-05 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('energy', models.FloatField(verbose_name='Energy')),
                ('proteins', models.FloatField(verbose_name='Proteins')),
                ('fats', models.FloatField(verbose_name='Fats')),
                ('carbs', models.FloatField(verbose_name='Carbs')),
                ('sugar', models.FloatField(blank=True, null=True, verbose_name='Sugar')),
                ('salt', models.FloatField(blank=True, null=True, verbose_name='Salt')),
                ('note', models.CharField(blank=True, max_length=150, null=True, verbose_name='Note')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Daily Intake',
                'verbose_name_plural': 'Daily Intakes',
            },
        ),
        migrations.CreateModel(
            name='MealTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Meal Title',
                'verbose_name_plural': 'Meal Titles',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('energy', models.FloatField(verbose_name='Energy')),
                ('proteins', models.FloatField(verbose_name='Proteins')),
                ('fats', models.FloatField(verbose_name='Fats')),
                ('carbs', models.FloatField(verbose_name='Carbs')),
                ('sugar', models.FloatField(blank=True, null=True, verbose_name='Sugar')),
                ('salt', models.FloatField(blank=True, null=True, verbose_name='Salt')),
                ('note', models.CharField(blank=True, max_length=150, null=True, verbose_name='Note')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='Rate')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True, verbose_name='Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('daily_intake', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodlog.dailyintake', verbose_name='Daily Intake')),
            ],
            options={
                'verbose_name': 'Day',
                'verbose_name_plural': 'Days',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodlog.day', verbose_name='Day')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodlog.mealtitle', verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('note', models.CharField(blank=True, max_length=150, null=True, verbose_name='Note')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodlog.meal', verbose_name='Meal')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodlog.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
            },
        ),
    ]
