from django.shortcuts import render, HttpResponse, redirect

# -------- RENDER VIEWS -------- #

def index(request):
    return redirect("/home")

def home(request):
    return render(request, "home.html")

def newMovie(request):
    return render(request, "new_movie.html")

def showMovie(request):
    return HttpResponse("placeholder for the show page")

def editMovie(request, movie_id):
    return HttpResponse("Placeholder for the edit page")

# -------- PROCESS DATA -------- #

def create(request):
    return redirect("/")

def processMovieEdit(request, movie_id):
    return redirect(f"/movies/{movie_id}")

def deleteMovie(request):
    return redirect("/movies")