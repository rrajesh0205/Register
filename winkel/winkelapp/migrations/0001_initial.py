# Generated by Django 3.0.4 on 2020-03-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_img', models.ImageField(upload_to='pics')),
                ('prod_desc', models.TextField()),
                ('prod_price', models.IntegerField()),
            ],
        ),
    ]
