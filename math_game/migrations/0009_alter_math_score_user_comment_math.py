# Generated by Django 4.0.5 on 2022-08-12 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('math_game', '0008_alter_math_score_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math_score',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment_math',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(choices=[(None, '--Please choose--'), ('Ad', 'Addition'), ('Div', 'Division'), ('Mul', 'Multiplication'), ('Sub', 'Subtraction')], max_length=10)),
                ('comment', models.TextField(max_length=300)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='player_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
