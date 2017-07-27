# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('zipCode', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='users',
            field=models.ManyToManyField(related_name='movies', to='movies_app.User'),
        ),
    ]