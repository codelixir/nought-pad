# Generated by Django 3.2.4 on 2021-06-15 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noughtpad_app', '0004_auto_20210615_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='preview',
        ),
    ]
