# Generated by Django 4.0.6 on 2024-05-25 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='titel',
            new_name='title',
        ),
    ]