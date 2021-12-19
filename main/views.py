# from django.http import request
from django.shortcuts import redirect, render
import threading
import time
from .fetch import youtube_search
from .models import Youtube_data
from asgiref.sync import sync_to_async

# @sync_to_async(thread_sensitive=False)
def fetch_data():
    temp = youtube_search({
        'query':'code',
        'max_result':25,
    })
    for keys, items in temp.items():
        if(not Youtube_data.objects.filter(id=keys).exists()):
            mod = Youtube_data(
                id = keys,
                title = items['title'],
                description = items['description'],
                date_posted = items['publishedAt'],
                thumbnail = items['thumbnail'],
                video_url = items['video_url'],
            )
            mod.save()

def run_func(func):
    while(True):
        func()
        time.sleep(10)

def fetch(request):
    t = threading.Thread(target=run_func, kwargs={'func':fetch_data}, daemon=True)
    t.start()
    return redirect('home-page')

def home(request):
    # fetch()
    context = {
        "posts" : Youtube_data.objects.all(),
    }
    return render(request, 'main/home.html', context=context)