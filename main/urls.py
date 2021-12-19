from django.urls import path, include
from .views import *

urlpatterns = [
    path("fetch-api-from-youtube/", fetch, name='fetch-data'),
    path("", home, name='home-page'),
]
