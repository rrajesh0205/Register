# Generated by Django 3.0.4 on 2020-03-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winkelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prod_sprice',
            field=models.IntegerField(null=True),
        ),
    ]
