# Generated by Django 3.2.9 on 2021-11-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211110_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='print',
            options={'ordering': ['sku']},
        ),
        migrations.AlterField(
            model_name='printoption',
            name='size',
            field=models.IntegerField(choices=[(0, 'Small'), (1, 'Medium'), (2, 'Large')], unique=True),
        ),
    ]
