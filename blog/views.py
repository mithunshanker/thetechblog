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

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

def details(request, id):
    post = get_object_or_404(Post, pk=id)
    total_posts = Post.objects.count()

    # Suggested Posts Logic
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

    # Comment Form Logic
    comments = post.comments.order_by('-created_at')  # Latest first
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            form = CommentForm()  # Clear the form after submission
    else:
        form = CommentForm()

    return render(request, "details.html", {
        'post': post,
        'suggested_posts': suggestions,
        'comments': comments,
        'form': form
    })
