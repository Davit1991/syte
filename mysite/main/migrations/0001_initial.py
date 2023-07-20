# Generated by Django 4.2.2 on 2023-07-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FEATURES_ITEMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='FEATURES_ITEMS name')),
                ('price', models.PositiveIntegerField(verbose_name='FEATURES_ITEMS price')),
                ('image', models.ImageField(upload_to='images', verbose_name='FEATURES_ITEMS img')),
            ],
        ),
    ]
