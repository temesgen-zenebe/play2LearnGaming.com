# Generated by Django 4.1 on 2022-08-29 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_delete_subscribedusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoggedUser',
        ),
    ]
