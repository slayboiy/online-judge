from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from .forms import SignUp

def signup_view(request):
    if request.method == "POST":
        form = SignUp(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save() 
            login(request, user)
            return redirect("home")

    else:
        form = SignUp()

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "Неправильный логин или пароль"

    return render(request,"accounts/login.html", {"error": error_message})

def logout_view(request):
    logout(request)
    return redirect("home")




