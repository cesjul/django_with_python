from django.shortcuts import render



def blog(request):
    return render(request,
                  'blog/home.html')

def example(request):
    return render(request,
                  'blog/example.html')