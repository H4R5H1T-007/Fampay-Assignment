# from django.http import request
from django.shortcuts import render

def home(request):
    context = {
        "posts" : "",
    }
    return render(request, 'main/home.html', context=context)