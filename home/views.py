from django.shortcuts import render


def index(request):

    context =  {'text': 'On home page',
                'title': 'Home - '}

    return render(
        request, 'home/home.html',
        context,
)