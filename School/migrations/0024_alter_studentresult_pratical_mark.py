# Generated by Django 5.0 on 2024-01-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0023_studentresult_grade_mark_studentresult_pratical_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='pratical_mark',
            field=models.IntegerField(),
        ),
    ]
