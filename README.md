# Gestion de Projet

Ce projet est une application de gestion de projet développée avec Django. Elle permet de gérer des projets, des rôles, des tâches et des commentaires.

## Table des Matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Prérequis

- Python 3.x
- Django 3.x ou supérieur
- Git

## Installation

1. **Cloner le dépôt**

  
   git clone https://github.com/The-godfather246/gestion_projet.git
   cd gestion_projet
 

2. **Créer et activer un environnement virtuel**

  
   python -m venv env
 

   - Sur Windows:
    
     .\env\Scripts\activate
   
   - Sur macOS/Linux:
    
     source env/bin/activate
    

3. **Installer les dépendances**

   
   pip install -r requirements.txt
  

4. **Appliquer les migrations**

 
   python manage.py migrate


## Configuration

1. **Configurer les paramètres de la base de données**

   Modifiez le fichier `gestion_projet/settings.py` pour configurer les paramètres de votre base de données.

2. **Créer un superutilisateur**


   python manage.py createsuperuser


## Utilisation

1. **Lancer le serveur de développement**

 
   python manage.py runserver


2. **Accéder à l'application**

   Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/`.

3. **Naviguer dans l'application**

   - **Projets**: Liste, création, modification et suppression des projets.
   - **Rôles**: Liste, création, modification et suppression des rôles.
   - **Tâches**: Liste, création, modification et suppression des tâches.
   - **Commentaires**: Liste, création, modification et suppression des commentaires.

## Contribuer

Les contributions sont les bienvenues! Pour contribuer, suivez ces étapes:

1. **Forker le dépôt**

   Forker le dépôt sur GitHub.

2. **Créer une branche**

   ```bash
   git checkout -b ma-branche
   ```

3. **Faire des modifications**

   Apportez vos modifications et commitez-les.

   ```bash
   git add .
   git commit -m "Description de la modification"
   ```

4. **Pousser les modifications**

   ```bash
   git push origin ma-branche
   ```

5. **Ouvrir une Pull Request**

   Ouvrez une Pull Request sur GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

N'hésitez pas à ouvrir une issue ou à contacter le mainteneur du projet si vous avez des questions ou des suggestions.

Merci de contribuer à ce projet!


