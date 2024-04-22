# Generated by Django 5.0.4 on 2024-04-13 19:47

import book.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('genre', models.CharField(choices=[('novel', 'novel'), ('short_story', 'short_story'), ('novella', 'novella'), ('fairytale', 'fairytale'), ('tragedy', 'tragedy'), ('comedy', 'comedy'), ('drama', 'drama')], max_length=150, verbose_name='жанр')),
                ('author', models.CharField(max_length=150, validators=[book.validators.valid_author], verbose_name='автор')),
                ('cost', models.IntegerField(verbose_name='стоимость')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]