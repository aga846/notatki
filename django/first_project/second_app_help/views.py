from django.shortcuts import render
from django.http import HttpResponse

def help(request):
    d = {"h": "This is help page"}
    return render(request, "second_app_help/help.html", context=d)
