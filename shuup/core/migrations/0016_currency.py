# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-16 23:53
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import jsonfield.fields
import shuup.utils.analog


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup', '0015_shipment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='The ISO-4217 code of the currency', max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='code')),
                ('decimal_places', models.PositiveSmallIntegerField(default=2, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='decimal places')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='CurrencyLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, enum=shuup.utils.analog.LogEntryKind, verbose_name='log entry kind')),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_entries', to='shuup.Currency', verbose_name='target')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
