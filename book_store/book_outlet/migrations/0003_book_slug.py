# Generated by Django 4.2.2 on 2023-08-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_author_book_is_bestselling_alter_book_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]