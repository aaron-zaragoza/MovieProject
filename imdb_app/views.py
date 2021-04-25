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

# -------- PROCESS DATA -------- #

def create(request):
    return redirect("/")

def edit(request):
    return HttpResponse("placeholder for the edit page")

def delete(request):
    return redirect("/blogs")