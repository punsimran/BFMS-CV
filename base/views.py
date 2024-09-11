from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def home(request):
    return render(request, "home.html",{})

def authView(request):
    if request.method == "GET":
        # Render the signup form for GET requests
        form = UserCreationForm()  # Initialize an empty form for GET requests
        return render(request, 'registration/signup.html', {"form": form})

    elif request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
         form = UserCreationForm()
         return render(request,"registration/signup.html",{"form": form})
    return render(request, 'registration/signup.html')  # Fallback in case of other methods

