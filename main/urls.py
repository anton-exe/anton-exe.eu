from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sociallinks', views.SocialLinks.as_view(), name='sociallinks'),
    path('sociallinks.html', views.SocialLinks.as_view(), name='sociallinks'),
    path('<str:pk>', views.TextPageView.as_view(), name='textPage'),
]

