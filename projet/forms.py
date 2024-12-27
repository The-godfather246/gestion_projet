from django import forms
from .models import Projet, Role, Tache, Commentaire

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'description', 'date_debut', 'date_fin', 'createur_projet']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_nom', 'projet', 'utilisateur']

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['projet', 'nom', 'description', 'date_limite', 'assigner_a']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['tache', 'utilisateur', 'contenu']
