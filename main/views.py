# from django.http import request
from django.core import paginator
from django.shortcuts import redirect, render
import threading
import time
from django.core.paginator import Paginator
from .fetch import youtube_search
from .models import Youtube_data

# @sync_to_async(thread_sensitive=False)
def fetch_data():
    temp = youtube_search({
        'query':'football',
        'max_result':40,
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
                channel_title = items['channelTitle'],
                is_live = items['isLive'],
                channel_url = items['channel_url'],
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
    all_data = Youtube_data.objects.all().order_by('-date_posted')
    paginator = Paginator(all_data, 10)
    pg_no = request.GET.get('page')
    page_obj = paginator.get_page(pg_no)
    context = {
        "posts" : page_obj,
        "page_obj":page_obj,
        "is_paginated":True,
    }
    return render(request, 'main/home.html', context=context)