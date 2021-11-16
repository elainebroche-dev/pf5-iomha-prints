# Generated by Django 3.2.9 on 2021-11-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20211116_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='print_option',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='item_dimensions',
            field=models.CharField(default='A', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=6),
            preserve_default=False,
        ),
    ]
