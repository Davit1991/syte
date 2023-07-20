# Generated by Django 4.2.2 on 2023-07-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Contact name')),
                ('email', models.EmailField(max_length=254, verbose_name='Contact email')),
                ('subject', models.CharField(max_length=100, verbose_name='Contact subject')),
                ('message', models.TextField(verbose_name='Contact message')),
            ],
        ),
    ]
