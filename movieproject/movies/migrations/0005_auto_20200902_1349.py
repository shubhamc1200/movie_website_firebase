# Generated by Django 3.1 on 2020-09-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200902_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='m',
            field=models.URLField(blank=True),
        ),
    ]
