# Generated by Django 4.1.7 on 2023-02-22 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_calendar_user_id_team_user_id_title_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='title',
            old_name='user_id',
            new_name='user',
        ),
    ]