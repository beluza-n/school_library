# Generated by Django 3.2.16 on 2024-05-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='middlename',
            field=models.CharField(max_length=256, null=True),
        ),
    ]