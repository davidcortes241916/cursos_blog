from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "main.html") #luego agregar los post :V