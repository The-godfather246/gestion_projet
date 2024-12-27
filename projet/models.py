from django.db import models
from django.contrib.auth.models import User

class Projet(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    createur_projet = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projets_crees')

    def __str__(self):
        return self.nom

class Role(models.Model):
    role_nom = models.CharField(max_length=50)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.role_nom

class Tache(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_limite = models.DateField()
    assigner_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taches_assignees')
    terminer = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.utilisateur.username} sur {self.tache.nom}"
