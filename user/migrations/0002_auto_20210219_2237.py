# Generated by Django 3.1.5 on 2021-02-19 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='introducion',
            new_name='introduction',
        ),
    ]
