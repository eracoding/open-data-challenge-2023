# Generated by Django 4.1.5 on 2023-01-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
