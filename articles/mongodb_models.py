from mongoengine import Document, StringField, ListField, ImageField, DateTimeField
from datetime import datetime

class Article(Document):
    title = StringField(max_length=200, required=True)
    content = StringField(required=True)  # Markdown
    categories = ListField(StringField(max_length=50))
    image = ImageField(upload_to='article_images/')
    pub_date = DateTimeField(default=datetime.now)
    
    meta = {'indexes': ['title', 'categories']}
