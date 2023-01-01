from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.homepage, name = 'homepage'),
    path('page_1', Main.page, name = 'page_1'),
    path('page_2', Main.page, name = 'page_2'),
    path('page_3', Main.page, name = 'page_3'),
    path('page_4', Main.page, name = 'page_4'),
    path('page_5', Main.page, name = 'page_5'),
]
