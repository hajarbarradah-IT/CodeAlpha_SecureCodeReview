# Rapport d'audit de sécurité — Application de connexion utilisateur

## 🎯 Objectif
Audit de sécurité d'une application Python de gestion de connexion utilisateur, réalisé dans le cadre du stage CodeAlpha (Cybersecurity Internship - Task 3).

## 🔍 Méthodologie
Revue de code manuelle (analyse statique), ligne par ligne, à la recherche de vulnérabilités connues (OWASP Top 10 et bonnes pratiques de sécurisation du code).

## 📊 Failles identifiées

### 1. Identifiants codés en dur — Gravité : Élevée
**Description :** des secrets (mot de passe DB, clé API) étaient écrits directement dans le code source.
**Risque :** exposition immédiate si le code est partagé ou publié.
**Correction :** migration vers des variables d'environnement (`os.environ.get()`).

### 2. Injection SQL — Gravité : Critique
**Description :** la requête SQL était construite par concaténation directe des entrées utilisateur.
**Risque :** un attaquant peut manipuler la requête pour contourner l'authentification ou accéder à des données non autorisées.
**Correction :** utilisation de requêtes préparées avec paramètres (`?`).

### 3. Usage dangereux de eval() — Gravité : Critique
**Description :** la fonction `eval()` exécutait n'importe quelle entrée comme du code Python.
**Risque :** exécution de code arbitraire par un attaquant.
**Correction :** remplacement par `ast.literal_eval()`, qui n'autorise que des valeurs simples.

### 4. Absence de validation des entrées — Gravité : Moyenne
**Description :** aucune vérification avant la conversion d'une entrée en nombre.
**Risque :** plantage du programme (déni de service basique) sur une entrée invalide.
**Correction :** ajout d'un bloc `try/except`.

### 5. Mots de passe stockés en clair — Gravité : Élevée
**Description :** les mots de passe étaient stockés tels quels dans la base de données.
**Risque :** exposition totale des identifiants en cas de fuite de la base de données.
**Correction :** hachage avec `bcrypt` (fonction à sens unique, avec sel).

## ✅ Conclusion
Sur 5 vulnérabilités identifiées, 5 ont été corrigées dans la version finale du code (`app_corrigee.py`). Ces corrections suivent les bonnes pratiques standards de développement sécurisé (OWASP).