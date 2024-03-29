# Generated by Django 4.1 on 2022-08-24 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_subscribedusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisitersCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits_num', models.IntegerField(default=1)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date updated')),
            ],
        ),
    ]
