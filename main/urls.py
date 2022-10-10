from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sociallinks', views.render_template, {"template_name": "main/sociallinks.html"}, "sociallinks"),
    path('<str:pk>', views.TextPageView.as_view(), name='textPage'),
]