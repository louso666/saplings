# /app/articles/apps.py

from django.apps import AppConfig
from .utils import connect_to_mongodb

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'

    def ready(self):
        connect_to_mongodb()
