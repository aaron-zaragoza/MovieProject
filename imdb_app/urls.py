from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('blogs', views.blogs),
    path('blogs/new', views.newBlog),
    path('blogs/create', views.create),
    path('blogs/<number>', views.show),
    
]
