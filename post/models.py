from django.db import models

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000, blank=True)
    owner = models.ForeignKey('auth.User', related_name='posts',
                              on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.title[:25]}'

    class Meta:
        ordering = ('created_at',)


class PostImage(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, related_name='images',
                             on_delete=models.CASCADE)
