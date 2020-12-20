from django.db import models
from django.utils.text import slugify
import uuid


class Issue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(default="default_post.jpg", upload_to="media")
    slug = models.SlugField(max_length=200, unique=True, blank=True, default="")
    published_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["published_date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Issue, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


STATUS = (
    (0, "Draft"),
    (1, "Submit"),
)

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ManyToManyField('blog.Category', related_name='categories')
    contributors = models.ManyToManyField('profiles.Contributor_Profile',related_name='contributors')
    image = models.ImageField(default="default_post.jpg", upload_to="media")
    slug = models.SlugField(max_length=200, unique=True, blank=True, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        verbose_name = 'Issue Content'
        verbose_name_plural = 'Issue Contents'


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Content, self).save(*args, **kwargs)
