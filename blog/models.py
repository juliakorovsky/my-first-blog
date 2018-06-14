from django.db import models
from django.utils import timezone
from tinymce import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = HTMLField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=200, default='Untitled')
    sample = models.ImageField(upload_to='media')
    description = HTMLField()

    def add_work(self):
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
