# Generated by Django 5.0 on 2024-01-13 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0020_attendance_attendance_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance_data',
            new_name='attendance_date',
        ),
    ]
