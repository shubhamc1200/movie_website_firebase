# Generated by Django 3.1 on 2020-09-02 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200902_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='m',
            new_name='movie_url',
        ),
    ]
