from django.http import HttpResponse
from django.shortcuts import render

def Home(response):
    return render(response, "index.html")


def About(response):
    # return HttpResponse("<h1>About Page<h1>")
    return render(response, "about.html")


def Contact(response):
    # return HttpResponse("<h1>Contact Page<h1>")
    return render(response, "contact.html")