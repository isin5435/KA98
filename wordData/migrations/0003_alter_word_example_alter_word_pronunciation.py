# Generated by Django 5.0 on 2023-12-20 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordData', '0002_uservocabulary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='example',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='pronunciation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
