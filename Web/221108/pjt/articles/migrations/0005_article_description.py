# Generated by Django 3.2.13 on 2022-11-14 00:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20221112_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]