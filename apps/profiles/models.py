import os
from django.db import models
from django.contrib import admin


def contributor_photo_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_profile-pic.%s" % (instance.Username, ext)
    return os.path.join("contributor_profile_pics", filename)


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
        (TUMBLR, "Tmblr"),
    ]

    Username = models.CharField(max_length=200, null=False, unique=True)
    First_name = models.CharField(max_length=50, null=False)
    Last_name = models.CharField(max_length=50, null=False)
    Date_of_Birth = models.DateField()
    Email = models.EmailField(unique=True)
    Phone_number = models.IntegerField()
    Image = models.FileField(default="default.jpg", upload_to=contributor_photo_path)
    Password = models.CharField(max_length=200)
    Social_media_platform = models.CharField(
        max_length=50, choices=SOCIAL_MEDIA_PLATFORMS, default=FACEBOOK
    )
    Social_media_handles = models.CharField(max_length=50, default="@Username")

    def __str__(self):
        return f"{self.Username}"


def reader_photo_path(instance, filename):
    basename, file_ext = os.path.splitext(filename)
    return "media/reader_profile_pics/{instance.user.Username}{instance.user.id}_profile_pic"


class Reader_Profile(models.Model):
    class Meta:
        verbose_name = "Reader Profile"

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

    # PHONE NUMBER FIELDS CANNOT START WITH A '0'
    Username = models.CharField(max_length=200, null=False, unique=True)
    First_name = models.CharField(max_length=50, null=False)
    Date_of_Birth = models.DateField()
    Email = models.EmailField(null=False)
    Image = models.FileField(default="default.jpg", upload_to=reader_photo_path)
    Password = models.CharField(max_length=200)
    Social_media_platform = models.CharField(
        max_length=30, choices=SOCIAL_MEDIA_PLATFORMS, default=FACEBOOK
    )
    Social_media_handles = models.CharField(max_length=50, default="@Username")

    def __str__(self):
        return f"{self.Username}"
