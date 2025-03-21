from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse('This tab has succefully opened!')

def example(request):
    return HttpResponse('This is a example of nested urls')