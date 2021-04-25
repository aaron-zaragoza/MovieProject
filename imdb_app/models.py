from django.db import models
import re

# -------- MODEL MANAGERS -------- #

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

class Movie(models.Model):
    title = models.CharField(max_length = 99)
    desc = models.TextField(max_length= 1000)
    duration = models.IntegerField()

class Actor(models.Model):
    firstName = models.CharField(max_length= 45)
    lastName = models.CharField(max_length= 45)
    movies = models.ManyToManyField(Movie, related_name="actors")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Director (models.Model):
    firstName = models.CharField(max_length= 45)
    lastName = models.CharField(max_length= 45)
    movies = models.ManyToManyField(Movie, related_name="movies")

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)