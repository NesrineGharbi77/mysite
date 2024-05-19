# mysite
 
### README

# Application Web E-commerce avec Django

## Description

Ce projet est une application web full stack de commerce électronique, développée dans le cadre du module "Langage de programmation" du Master Data Science pour l’Économie et la Finance à l'Université Abdelmalek Essaâdi, Faculté des Sciences Juridiques, Économiques et Sociales de Tanger. Le but est de mettre en pratique les compétences en développement web à l'aide du framework Django.

## Fonctionnalités Principales

- **Gestion des utilisateurs**
  - Inscription, connexion et gestion des profils utilisateurs.
  
- **Gestion des produits**
  - Affichage des catégories et des produits.
  - Détails des produits avec images, descriptions, et prix.

- **Panier**
  - Ajout, modification, et suppression d'articles dans le panier.
  - Vue du contenu actuel du panier.

- **Paiement**
  - Intégration de l'API Stripe pour les transactions sécurisées.
  - Processus de checkout avec gestion des commandes.

- **Recherche**
  - Barre de recherche pour filtrer les produits.

- **Sécurité**
  - Implémentation de jeton CSRF pour protéger contre les attaques CSRF.

## Technologies Utilisées

- **Backend :** Django
- **Frontend :** HTML, CSS, JavaScript
- **Base de données :** SQLite
- **Paiement :** API Stripe

## Installation

1. **Cloner le dépôt**
   ```sh
   git clone https://github.com/username/project.git
   cd project
   ```

2. **Créer un environnement virtuel**
   ```sh
   python -m venv env
   source env/bin/activate  # Sur Windows: env\Scripts\activate
   ```

3. **Installer les dépendances**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**
   - Créer un fichier `.env` et ajouter les clés API Stripe :
     ```env
     STRIPE_PUB_KEY=your_public_key
     STRIPE_SECRET_KEY=your_secret_key
     ```

5. **Appliquer les migrations**
   ```sh
   python manage.py migrate
   ```

6. **Lancer le serveur**
   ```sh
   python manage.py runserver
   ```

## Utilisation

- Accéder à l'application via `http://127.0.0.1:8000/`
- Inscription et connexion pour gérer votre compte.
- Parcourir les produits, ajouter au panier et procéder au paiement.

## Contributions

Les contributions sont les bienvenues. Veuillez soumettre une pull request pour toute amélioration ou nouvelle fonctionnalité.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

Développé par **Nesrine Gharbi** sous la supervision de **Pr. Lotfi Elaachak** pour l'année universitaire 2023/2024.
