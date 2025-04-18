from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6


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


    return render(
        request,
        "blog/post_details.html",
        {"post": post},
    )


