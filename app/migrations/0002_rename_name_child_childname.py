# Generated by Django 5.1.2 on 2024-11-27 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='name',
            new_name='childname',
        ),
    ]
