# Generated by Django 5.1.1 on 2024-09-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_info_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='middleName',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
