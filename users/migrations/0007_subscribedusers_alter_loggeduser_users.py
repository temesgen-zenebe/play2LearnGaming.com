# Generated by Django 4.1 on 2022-08-24 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_loggeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
            ],
        ),
        migrations.AlterField(
            model_name='loggeduser',
            name='users',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
