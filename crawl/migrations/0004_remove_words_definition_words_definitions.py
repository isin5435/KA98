# Generated by Django 5.0 on 2023-12-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0003_remove_words_audio_alter_words_definition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='words',
            name='definition',
        ),
        migrations.AddField(
            model_name='words',
            name='definitions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]