# Generated by Django 3.2.9 on 2021-11-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211110_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='rating',
            field=models.IntegerField(blank=0, choices=[(0, 'Unrated'), (1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=0),
        ),
    ]
