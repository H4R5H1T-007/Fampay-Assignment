# from django.http import request
from django.shortcuts import render
from .fetch import youtube_search
from .models import Youtube_data

def home(request):
    temp = youtube_search({
        "query":"Google",
        "max_result":25,
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
    context = {
        "posts" : Youtube_data.objects.all(),
    }
    return render(request, 'main/home.html', context=context)