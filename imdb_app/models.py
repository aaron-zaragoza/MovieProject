from django.db import models
import re

# -------- MODEL MANAGERS -------- #

class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be longer than 1 character'
        
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be longer than 1 character'
            
        if len(postData['username']) < 6:
            errors['username'] = 'Username must be at least 6 characters long'
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Must use valid email address"
        
        user_list = User.objects.filter(email = postData['email'])

        if len(user_list) > 0:
            errors['email_duplicate'] = 'Email already exists; please use another'
        
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        
        if postData['password'] != postData['confirm_password']:
            errors['math_password'] = 'Your passwords do not match'
            
        return errors

class MovieManager(models.Manager):
    def validate_movie(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = 'Title must be at least 1 character long'

        if len(postData['desc']) < 30:
            errors['desc'] = 'Description must be at least 30 characters long'

        return errors

class ActorManager(models.Manager):
    def validate_actor(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be longer than 1 character'
        
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be longer than 1 character'

        return errors

class DirectorManager(models.Manager):
    def validate_director(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be longer than 1 character'
        
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be longer than 1 character'

        return errors

# -------- MODELS -------- #

class User(models.Model):
    # --- BASIC ATTRIBUTES --- #
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)

    # --- IMPORT MANAGER --- #
    objects = UserManager()

    # --- CREATE/UPDATE --- #
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Movie(models.Model):
    # --- BASIC ATTRIBUTES --- #
    title = models.CharField(max_length = 100)
    release_date = models.DateField()
    desc = models.TextField(max_length = 2000)
    duration = models.IntegerField()

    # --- RELATIONSHIPS ---#
    added_by = models.ForeignKey(User, related_name = 'movies', on_delete = models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name = 'favorite_movies')

    # --- IMPORT MANAGER --- #
    objects = MovieManager()

    # --- CREATE/UPDATE --- #
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Actor(models.Model):
    # --- BASIC ATTRIBUTES --- #
    firstName = models.CharField(max_length = 45)
    lastName = models.CharField(max_length = 45)
    bio = models.CharField(max_length=2000, blank=True, default='')
    # ---- RELATIONSHIPS ---- #
    featured_movies = models.ManyToManyField(Movie, related_name ="actors")

    # --- IMPORT MANAGER --- #
    objects = ActorManager()

    # --- CREATE/UPDATE --- #
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Director (models.Model):
    # --- BASIC ATTRIBUTES --- #
    firstName = models.CharField(max_length= 45)
    lastName = models.CharField(max_length= 45)
    bio = models.CharField(max_length=2000, blank=True, default='')

    # ---- RELATIONSHIPS ---- #
    movies_directed = models.ManyToManyField(Movie, related_name="directors")

    # --- IMPORT MANAGER --- #
    objects = DirectorManager()

    # --- CREATE/UPDATE --- #
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)