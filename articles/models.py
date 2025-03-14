from django.db import models
from mongoengine import Document, fields
from django.utils import timezone

# Модель статьи в Django (PostgreSQL)
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Модель изображения в MongoEngine (MongoDB)
class ArticleImage(Document):
    article_id = fields.IntField(required=True)  # Ссылка на статью в PostgreSQL
    image = fields.ImageField(size_max=(1920, 1080), file_size_max=15 * 1024 * 1024)
    created_at = fields.DateTimeField(default=timezone.now)

    meta = {'collection': 'article_images'}
