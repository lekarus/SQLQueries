# Generated by Django 4.0.4 on 2022-05-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_rename_name_client_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='tovar',
            name='sort',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
