# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 12:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.folder
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_gallery', '0003_auto_20160821_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryplugin',
            name='engine',
            field=models.CharField(choices=[('fade', 'Fade'), ('slide', 'Slide')], default='fade', max_length=50, verbose_name='Engine'),
        ),
        migrations.AlterField(
            model_name='galleryplugin',
            name='style',
            field=models.CharField(choices=[('standard', 'Standard')], default='standard', max_length=50, verbose_name='Style'),
        ),
        migrations.AlterField(
            model_name='slidefolderplugin',
            name='folder',
            field=filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.PROTECT, to='filer.Folder', verbose_name='folder'),
        ),
        migrations.AlterField(
            model_name='slideplugin',
            name='content',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='slideplugin',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.FILER_IMAGE_MODEL, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='slideplugin',
            name='target',
            field=models.CharField(blank=True, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], max_length=100, verbose_name='target'),
        ),
    ]
