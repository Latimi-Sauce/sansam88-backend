# Generated by Django 4.0.4 on 2022-05-23 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_log_content_log_title_alter_farm_log_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='log',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to='farms.log'),
        ),
    ]