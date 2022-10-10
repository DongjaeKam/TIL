# Generated by Django 3.2.11 on 2022-10-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=20)),
                ('movie_title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('grade', models.FloatField(default=10.0)),
            ],
        ),
    ]
