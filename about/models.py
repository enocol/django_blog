from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
