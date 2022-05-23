# Generated by Django 4.0.4 on 2022-05-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receiver',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customerMemo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sellerMemo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
