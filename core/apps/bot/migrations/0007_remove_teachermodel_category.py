# Generated by Django 5.1.3 on 2025-05-16 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_alter_usermodel_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachermodel',
            name='category',
        ),
    ]
