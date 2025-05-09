from django.urls import path

from . import views
from antonexe.feeds import BlogRSS

app_name = "main"
urlpatterns = [
    path('',                 views.IndexView.as_view(),    name='index'),
    path('sociallinks',      views.SocialLinks.as_view(),  name='sociallinks'),
    path('sociallinks.html', views.SocialLinks.as_view(),  name='sociallinks'),
    path('blog.xml',         BlogRSS(),                    name='blogrss'),
    path('blog',             views.BlogListView.as_view(), name='bloglist'),
    path('blog/<str:pk>',    views.BlogPostView.as_view(), name='blogpost'),
    path('<str:pk>',         views.TextPageView.as_view(), name='textpage'),
]

