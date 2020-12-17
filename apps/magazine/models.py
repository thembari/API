from django.db import models
import uuid
from django.utils.text import slugify



class Issue(models.Model):
    id = uuid.uuid4()
    title = models.CharField(max_length=200, unique=True)
    image = models.FileField(default="default_post.jpg", upload_to="media")
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
    id = uuid.uuid4()
    issue = models.ForeignKey(Issue, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.ManyToManyField('blog.Category')
    contributors = models.ManyToManyField('profiles.Contributor_Profile')
    image = models.FileField(default="default_post.jpg", upload_to="media")
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
