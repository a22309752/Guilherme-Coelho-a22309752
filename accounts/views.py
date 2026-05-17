from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegistoForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("portfolio:home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"Login efetuado com sucesso.")
            return redirect("portfolio:home")
        else:
            messages.error(request,"Username ou password inválidos.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso.")
    return redirect("portfolio:home")


def registo_view(request):
    if request.user.is_authenticated:
        return redirect("portfolio:home")

    if request.method == "POST":
        form = RegistoForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Conta criada com sucesso. Já podes fazer login")
            return redirect("login")

    else:
        form = RegistoForm()

    return render(request, "accounts/registo.html",{"form": form})

