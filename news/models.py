from django.db import models
from django.utils.text import slugify


# Create your models here.
class News(models.Model):
    content_title = models.CharField(max_length=100)
    content_body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    writers = models.CharField(max_length=50, default="author")
    content_category = models.CharField(blank=True, max_length=30)
    slug = models.SlugField(blank=True, max_length=100, editable=False)

    def save(self):
        self.slug = slugify(self.content_title)
        super(News, self).save()

    def __str__(self):
        return f"{self.id}. {self.content_title}"
