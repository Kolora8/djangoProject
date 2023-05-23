from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('',index),
    path('home/',index, name='home'),
    path('about/', about, name='home')

]