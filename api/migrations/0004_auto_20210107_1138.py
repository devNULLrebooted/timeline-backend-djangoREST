# Generated by Django 3.1.4 on 2021-01-07 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210104_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='activity',
            new_name='activityID',
        ),
    ]
