from django.db import models

# Create your models here.

class TextPage(models.Model):
    url_path = models.CharField(max_length=200, unique=True, primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title + " (" + self.url_path + ")"

class TextPageSection(models.Model):
    page = models.ForeignKey(TextPage, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.heading

class SocialMediaGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class SocialMediaLink(models.Model):
    icon = models.TextField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)

    group = models.ForeignKey(SocialMediaGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
