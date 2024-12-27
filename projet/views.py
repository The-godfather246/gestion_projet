from django.shortcuts import render, get_object_or_404, redirect
from .models import Projet, Role, Tache, Commentaire
from .forms import ProjetForm, RoleForm, TacheForm, CommentaireForm

# Vues pour les projets
def liste_projets(request):
    projets = Projet.objects.all()
    return render(request, 'projet/liste_projets.html', {'projets': projets})

def creer_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm()
    return render(request, 'projet/creer_projet.html', {'form': form})

def modifier_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'projet/modifier_projet.html', {'form': form})

def supprimer_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        projet.delete()
        return redirect('liste_projets')
    return render(request, 'projet/supprimer_projet.html', {'projet': projet})

# Vues pour les rôles
def liste_roles(request):
    roles = Role.objects.all()
    return render(request, 'projet/liste_roles.html', {'roles': roles})

def creer_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_roles')
    else:
        form = RoleForm()
    return render(request, 'projet/creer_role.html', {'form': form})

def modifier_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('liste_roles')
    else:
        form = RoleForm(instance=role)
    return render(request, 'projet/modifier_role.html', {'form': form})

def supprimer_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('liste_roles')
    return render(request, 'projet/supprimer_role.html', {'role': role})

# Vues pour les tâches
def liste_taches(request):
    taches = Tache.objects.all()
    return render(request, 'projet/liste_taches.html', {'taches': taches})

def creer_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_taches')
    else:
        form = TacheForm()
    return render(request, 'projet/creer_tache.html', {'form': form})

def modifier_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('liste_taches')
    else:
        form = TacheForm(instance=tache)
    return render(request, 'projet/modifier_tache.html', {'form': form})

def supprimer_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        tache.delete()
        return redirect('liste_taches')
    return render(request, 'projet/supprimer_tache.html', {'tache': tache})

# Vues pour les commentaires
def liste_commentaires(request):
    commentaires = Commentaire.objects.all()
    return render(request, 'projet/liste_commentaires.html', {'commentaires': commentaires})

def creer_commentaire(request):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_commentaires')
    else:
        form = CommentaireForm()
    return render(request, 'projet/creer_commentaire.html', {'form': form})

def modifier_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('liste_commentaires')
    else:
        form = CommentaireForm(instance=commentaire)
    return render(request, 'projet/modifier_commentaire.html', {'form': form})

def supprimer_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    if request.method == 'POST':
        commentaire.delete()
        return redirect('liste_commentaires')
    return render(request, 'projet/supprimer_commentaire.html', {'commentaire': commentaire})
