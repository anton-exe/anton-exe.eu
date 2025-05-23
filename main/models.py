from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class TextPage(models.Model):
    url_path = models.CharField(max_length=200, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    javascript = models.TextField(blank=True)

    def __str__(self):
        return self.title + " (" + self.url_path + ")"
    
    def get_absolute_url(self):
        return reverse('main:textpage', kwargs={'pk': self.url_path})

class TextPageSection(models.Model):
    page = models.ForeignKey(TextPage, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    index = models.IntegerField(default=0)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["index"] 

class BlogPost(models.Model):
    url_path = models.CharField(max_length=200, unique=True, primary_key=True, default=timezone.now().strftime("%Y-%m-%d"))

    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)

    content = models.TextField()

    def __str__(self):
        return self.title + " (" + self.url_path + ")"

    def get_absolute_url(self):
        return reverse('main:blogpost', kwargs={'pk': self.url_path})
    
    class Meta:
        ordering = ["creation_date"]

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
    
    class Meta:
        ordering = ["name"]

class NavbarButton(models.Model):
    text = models.CharField(max_length=50)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class NavbarDropdown(models.Model):
    text = models.CharField(max_length=50)
    
    def __str__(self):
        return self.text

class NavbarDropdownItem(models.Model):
    text = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    index = models.IntegerField(default=0)

    dropdown = models.ForeignKey(NavbarDropdown, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["index"] 
