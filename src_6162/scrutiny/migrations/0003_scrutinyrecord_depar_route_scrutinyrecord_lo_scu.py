# Generated by Django 5.1.3 on 2024-11-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrutiny', '0002_rename_l1scrdeprrouting_scrutinyrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrutinyrecord',
            name='depar_route',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scrutinyrecord',
            name='lo_scu',
            field=models.TextField(blank=True, null=True),
        ),
    ]
