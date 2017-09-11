# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name=b'title')),
                ('slug', models.SlugField(unique=True, verbose_name=b'slug')),
                ('body', models.TextField(blank=True, verbose_name=b'body')),
                ('status', models.IntegerField(choices=[(1, b'Draft'), (2, b'Public')], default=2, verbose_name=b'status')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'publish')),
                ('show_publish', models.BooleanField(default=True, help_text=b'Whether or not to show the published date on the page', verbose_name=b'show publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modified')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'publish',
                'ordering': ('-publish',),
                'verbose_name_plural': 'pages',
                'db_table': 'base_pages',
                'verbose_name': 'page',
            },
        ),
    ]