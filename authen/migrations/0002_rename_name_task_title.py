# Generated by Django 4.0 on 2022-01-18 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='title',
        ),
    ]
