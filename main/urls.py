from django.urls import path

from . views import *
# app_name='main'

app_name = 'main'

urlpatterns = [
# path('post_view/', post_view, name='post_view'),
path('signIn/', signIn_views),
path('signIn/signOut/', signOut_views),
]

 