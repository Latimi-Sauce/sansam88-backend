# Generated by Django 4.0.5 on 2022-06-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0009_alter_log_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='title',
            field=models.CharField(blank=True, default='<function now at 0x7fb1c3eb2040>', max_length=255, null=True),
        ),
    ]