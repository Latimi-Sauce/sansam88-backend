# Generated by Django 4.0.4 on 2022-05-23 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='farm',
            name='log',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farms.log'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]