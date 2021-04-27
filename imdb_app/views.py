from django.shortcuts import render, HttpResponse, redirect
from .models import User, Movie, Actor, Director
from django.contrib import messages
import bcrypt

# -------- RENDER -------- #

def index(request):
    return redirect("/welcome")

def home(request):
    return render(request, 'home_page.html')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/home')
    context = {
        'logged_in_user' : User.objects.get(id = request.session['user_id']),
        'all_books' : Movie.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def newMovie(request):
    return render(request, "new_movie.html")

def showMovie(request):
    return HttpResponse("placeholder for the show page")

def editMovie(request, movie_id):
    return HttpResponse("Placeholder for the edit page")

# -------- PROCESS -------- #

def processRegistration(request):
    # 1. GET INPUTS VALIDATE
    errors = User.objects.validate_register(request.POST)
    # VALIDATIONS DO NOT PASS
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print("***********************************")
        print("REGISTRATION ERRORS FOUND")
        print("***********************************")
        return redirect("/home")
    # VALIDATIONS DO PASS
    else:
        # HASH THE PASSWORD
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        # GET INPUTS AND CREATE USER
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = hash_pw
        )
        # STORE NEW USER ID INSIDE OF SESSION
        request.session['new_user'] = new_user
        request.session['user_id'] = new_user.id
        print("***********************************")
        print(f"NEW USER CREATED: {new_user.username}")
        print("***********************************")
    return redirect("/dashboard")


def createMovie(request):
    return redirect("/")

def processMovieEdit(request, movie_id):
    return redirect(f"/movies/{movie_id}")

def deleteMovie(request):
    return redirect("/movies")