# Generated by Django 3.2.16 on 2024-05-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_library', '0002_auto_20240509_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='middlename',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]