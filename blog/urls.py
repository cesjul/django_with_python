from django.urls import path
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='home'),
    path('example/', blog_views.example, name='example'),
    path('post/<int:id>', blog_views.post, name='post')
]