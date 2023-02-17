from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request, "login.html", {
                    "error": "Неправильный логин или пароль.",
                },
            )
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            error = "Пароли не совпадают"
            return render(request, "register.html", {"error": error})

        user = User.objects.create_user(username, password=password)

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("main")

    return render(request, "register.html")
