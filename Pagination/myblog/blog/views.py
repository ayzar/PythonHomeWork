from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    page_size = request.GET.get('page_size', 5)  # по умолчанию 5 постов
    paginator = Paginator(post_list, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'page_size': page_size})
