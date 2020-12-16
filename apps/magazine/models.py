from django.db import models

# from django.contrib.auth.models import User
from apps.profiles.models import Contributor_Profile
from django.utils.timezone import timezone


STATUS = (
    (0, "Draft"),
    (1, "Submit"),
)


class Issue(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Content = models.TextField()
    Category = models.CharField(max_length=200)
    Author = models.ForeignKey(Contributor_Profile, on_delete=models.CASCADE)
    Image = models.FileField(default="default_post.jpg", upload_to="media")
    Slug = models.SlugField(max_length=200, unique=True, blank=True, default="")
    Created_on = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-Created_on"]

    def __str__(self):
        return self.title + " By: " + self.Author


class Issue_content(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Content = models.TextField()
    Author = models.ForeignKey(
        Contributor_Profile, on_delete=models.CASCADE, related_name="blog_posts"
    )