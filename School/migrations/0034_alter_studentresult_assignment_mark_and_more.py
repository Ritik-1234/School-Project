# Generated by Django 5.0 on 2024-01-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0033_alter_studentresult_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='assignment_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='exam_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='grace_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='midsem_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentresult',
            name='practical_mark',
            field=models.IntegerField(default=0),
        ),
    ]
