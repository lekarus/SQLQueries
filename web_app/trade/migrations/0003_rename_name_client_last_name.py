# Generated by Django 4.0.4 on 2022-05-07 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_alter_client_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='last_name',
        ),
    ]