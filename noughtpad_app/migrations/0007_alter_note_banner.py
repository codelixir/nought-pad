# Generated by Django 3.2.4 on 2021-06-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noughtpad_app', '0006_note_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='user_content/images/'),
        ),
    ]
