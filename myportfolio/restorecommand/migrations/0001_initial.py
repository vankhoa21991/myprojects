# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('mealType', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('address', models.TextField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]