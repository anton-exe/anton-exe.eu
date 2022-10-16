from django.contrib import admin

from .models import TextPage, TextPageSection, SocialMediaLink, SocialMediaGroup

# Register your models here.

class TextPageSectionInline(admin.StackedInline):
    model = TextPageSection
    extra = 0

class TextPageAdmin(admin.ModelAdmin):
    fields = ['url_path', 'title']
    inlines = [TextPageSectionInline]

class SocialMediaLinkInline(admin.StackedInline):
    model = SocialMediaLink
    extra = 0

class SocialMediaGroupAdmin(admin.ModelAdmin):
    inlines = [SocialMediaLinkInline]

admin.site.register(TextPage, TextPageAdmin)
admin.site.register(SocialMediaGroup, SocialMediaGroupAdmin)