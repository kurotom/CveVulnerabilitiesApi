# Generated by Django 4.1.7 on 2023-02-17 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cve',
            new_name='CveModel',
        ),
    ]
