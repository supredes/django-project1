# Generated by Django 4.0.3 on 2022-03-23 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='email',
            new_name='emails',
        ),
    ]
