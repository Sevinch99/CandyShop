# Generated by Django 4.1.3 on 2022-11-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_is_complited_order_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(verbose_name='delivery_time'),
        ),
    ]
