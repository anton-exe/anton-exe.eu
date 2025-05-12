from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import TextPage, BlogPost, SocialMediaGroup, NavbarButton, NavbarDropdown

def handler404(request, exception):
    template_name: str = "main/TextPage.html"

    page = TextPage.objects.get(url_path="404")
    context = {
        "sections": page.textpagesection_set.all(),
        "page": page,
        "navbar_buttons": NavbarButton.objects.all(),
        "navbar_dropdowns": NavbarDropdown.objects.all(),
    }
    return render(request, template_name, context, status=404)

class IndexView(generic.TemplateView):
    template_name: str = "main/TextPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = TextPage.objects.get(url_path="index")
        context["sections"] = page.textpagesection_set.all()
        context["page"] = page

        context["navbar_buttons"] = NavbarButton.objects.all()
        context["navbar_dropdowns"] = NavbarDropdown.objects.all()

        return context

class TextPageView(generic.TemplateView):
    template_name: str = "main/TextPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = get_object_or_404(TextPage, url_path=self.kwargs.get('pk'))
        context["sections"] = page.textpagesection_set.all()
        context["page"] = page

        context["navbar_buttons"] = NavbarButton.objects.all()
        context["navbar_dropdowns"] = NavbarDropdown.objects.all()

        return context

class BlogPostView(generic.TemplateView):
    template_name: str = "main/blogpost.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(BlogPost, url_path=self.kwargs.get('pk'))
        context["post"] = post

        context["navbar_buttons"] = NavbarButton.objects.all()
        context["navbar_dropdowns"] = NavbarDropdown.objects.all()

        return context
    
class BlogListView(generic.TemplateView):
    template_name: str = "main/bloglist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = BlogPost.objects.order_by("-creation_date")
        context["posts"] = posts

        context["navbar_buttons"] = NavbarButton.objects.all()
        context["navbar_dropdowns"] = NavbarDropdown.objects.all()

        return context

class SocialLinks(generic.TemplateView):
    template_name: str = "main/sociallinks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        groups = SocialMediaGroup.objects.all()

        context["groups"] = groups

        context["navbar_buttons"] = NavbarButton.objects.all()
        context["navbar_dropdowns"] = NavbarDropdown.objects.all()

        return context
