# Generated by Django 4.0.4 on 2022-05-23 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('introduction', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.log')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]