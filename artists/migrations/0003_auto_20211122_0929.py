# Generated by Django 3.2.9 on 2021-11-22 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20211118_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='date_of_birth',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='date_of_death',
        ),
    ]