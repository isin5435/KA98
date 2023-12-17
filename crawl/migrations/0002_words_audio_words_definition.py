# Generated by Django 5.0 on 2023-12-16 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='audio',
            field=models.URLField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='words',
            name='definition',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
    ]
