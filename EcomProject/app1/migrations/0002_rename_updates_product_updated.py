# Generated by Django 4.1.3 on 2022-11-22 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='updates',
            new_name='updated',
        ),
    ]
