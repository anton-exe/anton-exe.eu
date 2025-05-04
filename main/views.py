from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import TextPage, SocialMediaGroup, NavbarButton, NavbarDropdown

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

class SocialLinks(generic.TemplateView):
    template_name: str = "main/sociallinks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        groups = SocialMediaGroup.objects.all()

        context["groups"] = groups

        context["navbar_buttons"] = NavbarButton.objects.all()
        context["navbar_dropdowns"] = NavbarDropdown.objects.all()

        return context
