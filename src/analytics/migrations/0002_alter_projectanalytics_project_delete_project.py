# Generated by Django 5.1.3 on 2024-11-26 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectanalytics',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='auth_app.project'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]