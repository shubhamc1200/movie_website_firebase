# Generated by Django 3.1 on 2020-09-03 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='movie',
        ),
    ]
