from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
        # "slug": "aliquam-vel-est-ornare-feugiat",
        # "author": "John",
        # "author_img": "profile.png",
        # "title": "Aliquam vel est ornare, feugiat orci at, blandit ligula. Nam pulvinar iaculis lacinia. Aliquam ornare.",
        # "date": datetime(2023, 11, 10),
        # "views": 100,
        # "content": '''

class Posts (models.Model):
    author = models.CharField(max_length=20)
    slug = models.SlugField(db_index= True, blank= True)
    title = models.CharField(max_length=250)
    author_img = models.CharField(max_length=50)
    views = models.IntegerField()
    date = models.DateTimeField(default = datetime.now())
    content = models.TextField(default = '')

    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    post_count = models.IntegerField(default = 0)
