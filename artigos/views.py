from django.shortcuts import render, redirect, get_object_or_404
from .models import Artigo, Like
from .forms import ComentarioForm, ArtigoForm
from django.contrib.auth.decorators import login_required


def artigo_view(request):
    artigos = Artigo.objects.all()
    user = request.user

    context = {
        "artigos": artigos,
        "user":user,
        "comentario_form": ComentarioForm(),
    }

    return render(request, "artigos/artigo.html", context)

@login_required
def like_view(request):
    user = request.user
    if request.method == "POST":
        artigo_id = request.POST.get("artigo_id")
        artigo_obj = Artigo.objects.get(id=artigo_id)

        if user in artigo_obj.likes.all():
            artigo_obj.likes.remove(user)
        else:
            artigo_obj.likes.add(user)

        like, created = Like.objects.get_or_create(autor=user, artigo_id=artigo_id)
        
        if not created:
            if like.value == "Like":
                like.value == "Unlike"
            else:
                like.value == "Like"
    return redirect("artigos:artigo")

    
@login_required
def comentar_view(request):
    if request.method == "POST":
        artigo_id = request.POST.get("artigo_id")
        artigo = get_object_or_404(Artigo, id=artigo_id)

        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()

    return redirect("artigos:artigo")


@login_required
def editar_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if artigo.autor != request.user:
        return redirect("artigos:artigo")

    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)

        if form.is_valid():
            form.save()
            return redirect("artigos:artigo")
    else:
        form = ArtigoForm(instance=artigo)

    context = {
        "form": form,
        "artigo": artigo,
    }

    return render(request, "artigos/editar_artigo.html", context)

@login_required
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect("artigos:artigo")

    return render(request, "artigos/novo_artigo.html", {"form": form})