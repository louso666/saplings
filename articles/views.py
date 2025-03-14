from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Article, ArticleImage
from datetime import datetime
import uuid

# Функция для отображения списка статей
def article_list(request):
    articles = Article.objects.all()  # Получаем все статьи из PostgreSQL
    return render(request, 'articles/list.html', {'articles': articles})

# Функция для отображения деталей статьи
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    images = ArticleImage.objects.filter(article_id=pk)  # Получаем изображения для статьи из MongoDB
    return render(request, 'articles/detail.html', {'article': article, 'images': images})

# Функция для загрузки изображений через TinyMCE
@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name = f"{uuid.uuid4()}_{uploaded_file.name}"

        # Сохраняем изображение в MongoDB
        image = ArticleImage(
            article_id=0,  # Временно, пока не связана статья
            image=uploaded_file,
            created_at=datetime.now()
        )
        image.save()

        # Возвращаем URL изображения
        image_url = f"/media/{file_name}"  # Пример URL
        return JsonResponse({'location': image_url})

    return JsonResponse({'error': 'Invalid request'}, status=400)
