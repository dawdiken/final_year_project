from django.shortcuts import render
from django.http import HttpResponse
 
def foo(request):
    return HttpResponse("Py server running on pi"
            "With PostgreSQL database in the background\n\nWhooooop")

