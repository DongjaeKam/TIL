# Generated by Django 3.2.13 on 2022-11-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_type_of_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
