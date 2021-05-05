from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title