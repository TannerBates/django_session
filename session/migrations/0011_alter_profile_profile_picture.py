# Generated by Django 4.2.16 on 2024-10-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0010_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
