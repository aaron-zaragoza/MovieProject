from django.shortcuts import render, HttpResponse, redirect
import re

# -------- RENDER TEMPLATES -------- #

def index(request):
    return redirect("/welcome")

def welcome(request):
    return render(request, "welcome.html")

def newMovie(request):
    return render(request, "new_movie.html")

def showMovie(request):
    return HttpResponse("placeholder for the show page")

def editMovie(request, movie_id):
    return HttpResponse("Placeholder for the edit page")

# -------- PROCESS DATA -------- #

def createMovie(request):
    return redirect("/")

def processMovieEdit(request, movie_id):
    return redirect(f"/movies/{movie_id}")

def deleteMovie(request):
    return redirect("/movies")