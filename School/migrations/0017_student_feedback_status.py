# Generated by Django 5.0 on 2024-01-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0016_alter_student_feedback_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
