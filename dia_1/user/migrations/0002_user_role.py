# Generated by Django 5.1.6 on 2025-02-20 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Rol'),
        ),
    ]
