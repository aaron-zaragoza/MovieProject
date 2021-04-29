from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.login),
    path('logout', views.logout),
    path('process_registration', views.processRegistration),
    path('dashboard', views.dashboard),
    path('movies/processNewMovie', views.processNewMovie),
    path('movies/all', views.showAllMovies),
    path('movies/<movie_id>', views.showMovie),
    path('movies/<movie_id>/edit', views.editMovie),
    path('movies/<movie_id>/update', views.processMovieEdit),

]
