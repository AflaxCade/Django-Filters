# Generated by Django 5.0.6 on 2024-08-31 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateField(),
        ),
    ]
