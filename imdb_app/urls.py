from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('welcome', views.welcome),
    path('movies/new', views.newMovie),
    path('movies/create', views.createMovie),
    path('movies/<movie_id>', views.showMovie),
    path('movies/<movie_id>/edit', views.editMovie),
    path('movies/<movie_id>/update', views.processMovieEdit),

]
