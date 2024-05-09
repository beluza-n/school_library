# Generated by Django 3.2.16 on 2024-05-09 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_library', '0004_alter_book_author'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='asset_books', to='school_library.author'),
            preserve_default=False,
        ),
    ]