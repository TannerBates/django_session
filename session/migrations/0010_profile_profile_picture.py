# Generated by Django 4.2.16 on 2024-10-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
