# Generated by Django 4.2.1 on 2023-05-13 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0007_alter_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
