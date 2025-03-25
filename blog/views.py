from django.shortcuts import render



def blog(request):

    context =  {'text': 'On initial blog page',
                'title': 'Blog - ',
                }

    return render(request,
                  'blog/home.html',  context,
    )

def example(request):

    context =  {'text': 'On blog example',
                'title': 'Blog Example - '}

    return render(request,
                  'blog/example.html', context,
    )