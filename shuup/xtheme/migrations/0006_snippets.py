# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-09-03 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import shuup.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0050_move_product_status_text'),
        ('shuup_xtheme', '0001_squashed_0005_alter_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=64, verbose_name='location')),
                ('snippet_type', models.CharField(choices=[('inline_js', 'Inline JavaScript'), ('inline_css', 'Inline CSS'), ('inline_html', 'Inline HTML')], max_length=20, verbose_name='snippet type')),
                ('snippet', models.TextField(verbose_name='snippet')),
                ('themes', shuup.core.fields.SeparatedValuesField(blank=True, help_text='Select the themes that will have this snippet injected. Leave the field blank to inject in all themes.', null=True, verbose_name='themes')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='shuup.Shop')),
            ],
            options={
                'verbose_name': 'Snippet',
                'verbose_name_plural': 'Snippets',
            },
        ),
    ]
