# Generated by Django 5.1.4 on 2025-01-12 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlog', '0003_takingpill_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Time')),
                ('note', models.TextField(verbose_name='Note')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodlog.day', verbose_name='Day')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
    ]
