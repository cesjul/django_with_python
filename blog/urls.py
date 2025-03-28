from django.urls import path
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>/', blog_views.post, name='post'),
    path('example/', blog_views.example, name='example'),
    path('', blog_views.blog, name='home'),
]