from django.db import models


# Create your models here.

class Book(models.Model):
    GENRE_CHOISES = [
        ('novel', 'novel'),
        ('short_story', 'short_story'),
        ('novella', 'novella'),
        ('fairytale', 'fairytale'),
        ('tragedy', 'tragedy'),
        ('comedy', 'comedy'),
        ('drama', 'drama'),
    ]
    name = models.CharField(
        max_length=150, verbose_name='название'
    )
    genre = models.CharField(
        choices=GENRE_CHOISES, max_length=150,
        verbose_name='жанр',
    )
    author = models.CharField(
        max_length=150, verbose_name='автор'
    )
    cost = models.IntegerField(
        verbose_name='стоимость'
    )
    buyer = models.ForeignKey(
        to='users.User', to_field='email',
        verbose_name='покупатель', on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

