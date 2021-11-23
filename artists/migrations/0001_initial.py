# Generated by Django 3.2.9 on 2021-11-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('nationality', models.CharField(max_length=254)),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('date_of_death', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]