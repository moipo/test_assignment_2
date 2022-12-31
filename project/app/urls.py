from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.main, name = 'main'),
    path('page/<int:page_num>', Main.page, name = 'page'),
]
