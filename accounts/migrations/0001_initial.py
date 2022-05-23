# Generated by Django 4.0.4 on 2022-05-23 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('wallet', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('deposit', 'Deposit'), ('expense', 'Expense')], max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]