# Generated by Django 4.2.1 on 2023-05-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_room_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_images/'),
        ),
    ]
