# Generated by Django 3.0.3 on 2020-04-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200425_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]