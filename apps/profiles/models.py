import os
from django.db import models
from django.contrib import admin
from django.contrib.auth.hashers import make_password, check_password
import uuid


# FUNCTIONS
# PATH TO UPLOAD PROFILE PHOTOS TO
# TODO ==> SWITCH TO A CONTENT DELIVERY NETWORK OR PLATFORM

def contributor_photo_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_profile-pic.%s" % (instance.username, ext)
    return os.path.join("profile_pics/contributors/", filename)


def reader_photo_path(instance, filename):
    basename, file_ext = os.path.splitext(filename)
    return "profile_pics/readers/{instance.user.username}_profile_pic"




class Contributor_Profile(models.Model):
    class Meta:
        verbose_name = "Contributor Profile"
        verbose_name_plural = "Contributor Profiles"

    FACEBOOK = "FB"
    TWITTER = "TW"
    INSTAGRAM = "IG"
    TUMBLR = "TB"
    PINTREST = "PT"

    SOCIAL_MEDIA_PLATFORMS = [
        (TWITTER, "Twitter"),
        (FACEBOOK, "Facebook"),
        (INSTAGRAM, "Instagram"),
        (PINTREST, "Pintrest"),
        (TUMBLR, "Tumblr"),
    ]

    GENDER_CHOICES = [
        ('MALE', "Male"),
        ('FEMALE', "Female"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200, null=False, unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='')

    # TODO VALIDATE EMAIL
    email = models.EmailField(unique=True)

    # TODO VALIDATE PHONE NUMBER
    phone_number = models.CharField(max_length=14)
    blog_post = models.ForeignKey('blog.BlogPost', max_length=1000, null=True, blank=True, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField('blog.BlogPost', related_name="likes", blank=True)
    is_active = models.BooleanField(default=True)

    # TODO VALIDATE IMAGE FORMAT
    image = models.FileField(default="default.jpeg", upload_to=contributor_photo_path)

    # TODO ENCRYPT PASSWORD
    password = models.CharField(max_length=200)
    social_media_platform = models.CharField(max_length=50, choices=SOCIAL_MEDIA_PLATFORMS, default=FACEBOOK)
    social_media_handles = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"


class Reader_Profile(models.Model):
    class Meta:
        verbose_name = "Reader Profile"
        verbose_name_plural = "Reader Profiles"

    FACEBOOK = "FB"
    TWITTER = "TW"
    INSTAGRAM = "IG"
    TUMBLR = "TB"
    PINTREST = "PT"

    SOCIAL_MEDIA_PLATFORMS = [
        (TWITTER, "Twitter"),
        (FACEBOOK, "Facebook"),
        (INSTAGRAM, "Instagram"),
        (PINTREST, "Pintrest"),
        (TUMBLR, "Tmblr"),
    ]


    GENDER_CHOICES = [
        ('MALE', "Male"),
        ('FEMALE', "Female"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200, null=False, unique=True)
    first_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='')
    date_of_birth = models.DateField()

    # TODO VALIDATE EMAIL
    email = models.EmailField(null=False)

    # TODO VALIDATE IMAGE FORMAT
    image = models.FileField(default="default.jpeg", upload_to=reader_photo_path)
    likes = models.ManyToManyField('blog.BlogPost', related_name="liked_by", blank=True)

    # TODO ENCRYPT PASSWORD
    password = models.CharField(max_length=200)
    social_media_platform = models.CharField(max_length=30, choices=SOCIAL_MEDIA_PLATFORMS, default=FACEBOOK)
    social_media_handles = models.CharField(max_length=50, default="@Username")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.username}"
