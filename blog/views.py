from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.


def post_list(request):
    posts = Post.objects.annotate(comment_count=Count('comments'))
    paginator = Paginator(posts, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/index.html", {"page_obj": page_obj})


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    
    post = get_object_or_404(queryset, slug=slug)
    # If the post is not found, render a 404 page
    comments = post.comments.all()


    return render(
        request,
        "blog/post_details.html",
        {"post": post, "comments": comments},
    )


