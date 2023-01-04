from django.db import models

# Create your models here.
class News(models.Model):
    content_title = models.CharField(max_length=100)
    content_body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    writers = models.CharField(max_length=50, default="author")
    content_category = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return f"{self.id}. {self.content_title}"
