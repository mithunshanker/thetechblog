from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    posts = Post.objects.all().order_by('-created_at')  # Most recent first

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    paginator = Paginator(posts, 12)  # 12 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {
        'message': page_obj,
        'search_query': query,
        'page_obj': page_obj
    })

def details(request, id):
    post = Post.objects.get(pk=id)
    total_posts = Post.objects.count()

    def sug(pri):
        prik = pri
        if int(prik) > total_posts:
            prik = str(int(pri) - total_posts)
        return Post.objects.get(pk=prik)

    suggestions = []
    for i in range(1, 4):
        try:
            suggestions.append(sug(str(int(id) + i)))
        except Post.DoesNotExist:
            continue

    return render(request, "details.html", {
        'post': post,
        'suggested_posts': suggestions
    })
