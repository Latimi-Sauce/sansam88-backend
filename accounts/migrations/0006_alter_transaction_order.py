# Generated by Django 4.0.5 on 2022-06-20 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_remove_orderimage_name_alter_orderimage_id'),
        ('accounts', '0005_alter_transaction_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='orders.order'),
        ),
    ]
