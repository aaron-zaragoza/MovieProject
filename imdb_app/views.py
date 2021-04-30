from django.shortcuts import render, HttpResponse, redirect
from .models import User, Movie, Actor, Director
from django.contrib import messages
import bcrypt

# -------- RENDER -------- #

def index(request):
    return redirect("/home")

def home(request):
    return render(request, 'home_page.html')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/home')
    context = {
        'logged_in_user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'dashboard.html', context)

def login(request):
    # 1. CHECK TO SEE IF THE USERNAME EXISTS WITHIN DB
    user_list = User.objects.filter(username = request.POST['username'])
    # IF USERNAME DOESN'T EXIST WITH DB, REDIRECT WITH ERROR MESSAGE
    if len(user_list) == 0:
        messages.error(request, "Incorrect Username")
        return redirect("/home")
    # If email exists, check password
    logged_user = user_list[0]
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        # PASSWORD MATCHES
        request.session['user_id'] = logged_user.id
        print("******************************")
        print("SUCCESSFULLY LOGGED IN USER")
        print("******************************")
        return redirect("/dashboard")
    else:
        # PASSWORD DOES NOT MATCH
        messages.error(request, "Invalid Credentials")
        return redirect("/home")

def logout(request):
    request.session.clear()
    return redirect('/')

def newMovie(request):
    return render(request, "new_movie.html")

def showMovie(request, movie_id):
    context = {
        'logged_in_user' : User.objects.get(id = request.session['user_id']),
        'this_movie' : Movie.objects.get(id = movie_id),
    }
    return render(request, 'movie_details.html', context)

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
        # request.session['new_user'] = new_user
        request.session['user_id'] = new_user.id
        print("***********************************")
        print(f"NEW USER CREATED: {new_user.username}")
        print("***********************************")
    return redirect("/dashboard")

def processNewMovie(request):
    # validate new movie
    errors = Movie.objects.validate_movie(request.POST)
    # validations did not pass
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    # process new movie
    # validations pass
    newMovie = Movie.objects.create(
        title = request.POST['title'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc'],
        duration = request.POST['duration'],
        added_by = User.objects.get(id =  request.session['user_id']),
    )
    newMovie.favorited_by.add(User.objects.get(id =  request.session['user_id']))

    print('******************************************')
    print(newMovie, 'has just been created')
    print('******************************************')
    print(newMovie.favorited_by)
    return redirect('/movies/all')

def showAllMovies(request):
    context = {
        'logged_in_user' : User.objects.get(id = request.session['user_id']),
        'all_movies' : Movie.objects.all(),
    }
    return render(request, 'all_movies.html', context)

def processMovieEdit(request, movie_id):
    return redirect(f"/movies/{movie_id}")

def deleteMovie(request, movie_id):
    movie_to_delete = Movie.objects.get(id = movie_id)
    movie_to_delete.delete()
    return redirect("/movies/all")