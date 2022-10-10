from django.contrib import admin

from .models import TextPage, TextPageSection

# Register your models here.

class TextPageSectionInline(admin.StackedInline):
    model = TextPageSection
    extra = 0

class TextPageAdmin(admin.ModelAdmin):
    fields = ['url_path', 'title']
    inlines = [TextPageSectionInline]

admin.site.register(TextPage, TextPageAdmin)