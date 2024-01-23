# Generated by Django 5.0 on 2024-01-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0008_alter_staff_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='salary',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
    ]
