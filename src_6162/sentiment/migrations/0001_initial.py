# Generated by Django 5.1.3 on 2024-11-25 11:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_app', '0001_initial'),
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_succ', models.BooleanField(default=False)),
                ('api_hit', models.IntegerField(default=0)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentiment_data', to='base.data')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
