from django.shortcuts import render
from django.http import HttpRequest
from blog.data import posts
from typing import Any

def blog(request):

    context =  {'text': 'On initial blog page',
                'title': 'Blog - ',
                'posts': posts,
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

def post(request: HttpRequest, post_id: int): 
    found_post:dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post == None:
        raise Exception('Post not founded')

    context =  {'text': 'On initial blog page',
                'title': found_post['title'] + ' - ',
                'post': found_post,
                }

    return render(request,
                  'blog/post.html',  context,
    )