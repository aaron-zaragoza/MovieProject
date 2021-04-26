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
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        
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

        return errors

class ActorManager(models.Manager):
    def validate_actor(self, postData):
        errors = {}

        return errors

class DirectorManager(models.Manager):
    def validate_director(self, postData):
        errors = {}

        return errors

# -------- MODELS -------- #

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Movie(models.Model):
    title = models.CharField(max_length = 99)
    desc = models.TextField(max_length = 1000)
    duration = models.IntegerField()

class Actor(models.Model):
    firstName = models.CharField(max_length = 45)
    lastName = models.CharField(max_length = 45)
    movies = models.ManyToManyField(Movie, related_name ="actors")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Director (models.Model):
    firstName = models.CharField(max_length= 45)
    lastName = models.CharField(max_length= 45)
    movies = models.ManyToManyField(Movie, related_name="movies")

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)