# Generated by Django 5.0 on 2024-01-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
