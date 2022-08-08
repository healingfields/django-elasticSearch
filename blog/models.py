from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


ARTICLE_TYPES = [
    ('UN', 'Unspecified'),
    ('TU', 'Tutorial'),
    ('RS', 'Research'),
    ('RW', 'Review'),
]

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to=User,
        related_name='articles',
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default='UN')
    categories = models.ManyToManyField(
        to=Category,
        blank=True,
        related_name='articles'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author__username}: {self.title} ({self.created_at.date()})'
