from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('movies/new', views.newMovie),
    path('movies/create', views.create),
    path('movies/<number>', views.showMovie),
    path('movies/<number>/edit', views.edit)
]
