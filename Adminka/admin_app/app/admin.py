from django.contrib import admin
from .models import Article, Author, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('author', 'category', 'created_at')
    search_fields = ('title', 'content')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Возвращаем статьи только для определенного автора или категории
        if request.GET.get('author__id'):
            queryset = queryset.filter(author__id=request.GET['author__id'])
        if request.GET.get('category__id'):
            queryset = queryset.filter(category__id=request.GET['category__id'])
        return queryset

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Category)

