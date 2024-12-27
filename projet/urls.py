from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_projets, name='liste_projets'),
    path('projets/creer/', views.creer_projet, name='creer_projet'),
    path('projets/modifier/<int:pk>/', views.modifier_projet, name='modifier_projet'),
    path('projets/supprimer/<int:pk>/', views.supprimer_projet, name='supprimer_projet'),
    path('roles/', views.liste_roles, name='liste_roles'),
    path('roles/creer/', views.creer_role, name='creer_role'),
    path('roles/modifier/<int:pk>/', views.modifier_role, name='modifier_role'),
    path('roles/supprimer/<int:pk>/', views.supprimer_role, name='supprimer_role'),
    path('taches/', views.liste_taches, name='liste_taches'),
    path('taches/creer/', views.creer_tache, name='creer_tache'),
    path('taches/modifier/<int:pk>/', views.modifier_tache, name='modifier_tache'),
    path('taches/supprimer/<int:pk>/', views.supprimer_tache, name='supprimer_tache'),
    path('commentaires/', views.liste_commentaires, name='liste_commentaires'),
    path('commentaires/creer/', views.creer_commentaire, name='creer_commentaire'),
    path('commentaires/modifier/<int:pk>/', views.modifier_commentaire, name='modifier_commentaire'),
    path('commentaires/supprimer/<int:pk>/', views.supprimer_commentaire, name='supprimer_commentaire'),
]
