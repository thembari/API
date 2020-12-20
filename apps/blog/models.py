from django.db import models
import uuid
from django.utils.text import slugify

class Category(models.Model):
    class Meta:
        verbose_name = 'Blog Post Category'
        verbose_name_plural = 'Blog Post Categories'

    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name}"


class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(max_length=800, blank=False, null=False)
    author = models.ForeignKey('profiles.Contributor_Profile', on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Posted on")
    category = models.ManyToManyField(Category, related_name='Category')
    slug = models.SlugField(max_length=40, default="", blank=True)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"
