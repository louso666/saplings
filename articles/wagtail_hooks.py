from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import ArticlePage

class ArticlePageAdmin(ModelAdmin):
    model = ArticlePage
    menu_label = "Статьи"  # Название в меню
    menu_icon = "doc-full"  # Иконка (можно выбрать другую)
    menu_order = 200  # Порядок в меню
    add_to_settings_menu = False  # Не добавлять в настройки
    exclude_from_explorer = False  # Показывать в explorer
    list_display = ('title', 'intro', 'cover_image')  # Поля для отображения в списке
    search_fields = ('title', 'intro', 'body')  # Поля для поиска

modeladmin_register(ArticlePageAdmin)
