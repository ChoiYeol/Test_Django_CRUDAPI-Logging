from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from main.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('post_view/', post_view, name='post_view'),
    path('post_view/post_view_insert/', post_view_insert, name='post_view_insert'),
    path('blog/',blog, name="blog"),
    path('blog/new_post/',new_post, name="new_post"), 
    path('blog/<int:pk>/',posting, name="posting"),
    path('blog/<int:pk>/remove/', remove_post),
    path('auth/', include('main.urls')),
    # path('signOut/',signOut_views, name="signOut"), 
]   
 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)