from django.urls import path
from blog import views as blog_views

# def home(request):
#     return HttpResponse('This is the home page')

# def my_view(request):
#     return HttpResponse('This tab has succefully opened!')

urlpatterns = [
    path('', blog_views.blog),
    path('example/', blog_views.example),
]