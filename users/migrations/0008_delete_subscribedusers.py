# Generated by Django 4.1 on 2022-08-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_subscribedusers_alter_loggeduser_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubscribedUsers',
        ),
    ]
