# Generated by Django 3.2.9 on 2021-11-16 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_printoption_dimensions'),
        ('checkout', '0003_alter_orderlineitem_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='print_option',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.printoption'),
            preserve_default=False,
        ),
    ]