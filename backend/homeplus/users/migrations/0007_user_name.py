# Generated by Django 5.1.5 on 2025-01-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1239, max_length=255),
            preserve_default=False,
        ),
    ]
