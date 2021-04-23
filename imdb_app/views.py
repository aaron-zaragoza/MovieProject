from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect("/blogs")

def blogs(request):
    return HttpResponse("hello world")

def newBlog(request):
    return HttpResponse("Place holder for a new blog form")

def create(request):
    return redirect("/")

def show(request):
    return HttpResponse("placeholder for the show page")

def edit(request):
    return HttpResponse("placeholder for the edit page")

def delete(request):
    return redirect("/blogs")