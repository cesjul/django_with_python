from django.urls import path
from home import views as home_views


# def home(request):
#     return HttpResponse('This is the home page')

# def my_view(request):
#     return HttpResponse('This tab has succefully opened!')

urlpatterns = [
    path('', home_views.index),
    
    
]