# Generated by Django 5.0 on 2024-01-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0017_student_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_feedback',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
