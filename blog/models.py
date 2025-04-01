from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title =  models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # noqa: E501
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


