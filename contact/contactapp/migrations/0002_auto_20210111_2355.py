# Generated by Django 3.1.3 on 2021-01-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='address_1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='address_2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.CharField(max_length=20),
        ),
    ]