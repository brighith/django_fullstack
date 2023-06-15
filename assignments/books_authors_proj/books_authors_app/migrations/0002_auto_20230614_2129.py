# Generated by Django 2.2.4 on 2023-06-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Book'),
        ),
    ]
