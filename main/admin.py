from django.contrib import admin

from .models import TextPage, TextPageSection, BlogPost, SocialMediaLink, SocialMediaGroup, NavbarButton, NavbarDropdown, NavbarDropdownItem

# Register your models here.

class TextPageSectionInline(admin.StackedInline):
    model = TextPageSection
    extra = 0

class TextPageAdmin(admin.ModelAdmin):
    inlines = [TextPageSectionInline]

class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost

class SocialMediaLinkInline(admin.StackedInline):
    model = SocialMediaLink
    extra = 0

class SocialMediaGroupAdmin(admin.ModelAdmin):
    inlines = [SocialMediaLinkInline]

class NavbarDropdownItemInline(admin.StackedInline):
    model = NavbarDropdownItem
    extra = 2

class NavbarDropdownAdmin(admin.ModelAdmin):
    inlines = [NavbarDropdownItemInline]

class NavbarButtonAdmin(admin.ModelAdmin):
    pass

admin.site.register(TextPage, TextPageAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SocialMediaGroup, SocialMediaGroupAdmin)
admin.site.register(NavbarDropdown, NavbarDropdownAdmin)
admin.site.register(NavbarButton, NavbarButtonAdmin)
