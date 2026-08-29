# CodeAlpha - Secure Code Review

## 📌 Description
Audit de sécurité d'une application Python de gestion de connexion utilisateur, réalisé dans le cadre du stage virtuel CodeAlpha en cybersécurité (Task 3).

## 🛠 Technologies utilisées
- Python 3
- SQLite3
- bcrypt

## 📂 Contenu du dépôt
- `app_a_auditer.py` — code original, contenant volontairement 5 vulnérabilités
- `app_corrigee.py` — version corrigée, sécurisée
- `RAPPORT_AUDIT.md` — rapport détaillé de l'audit (failles, gravité, recommandations)

## 🔍 Méthodologie
Revue de code manuelle (analyse statique), recherche de vulnérabilités courantes selon les principes de l'OWASP.

## 🎓 Failles identifiées et corrigées
1. Identifiants codés en dur → variables d'environnement
2. Injection SQL → requêtes préparées
3. Usage dangereux de `eval()` → `ast.literal_eval()`
4. Absence de validation des entrées → gestion d'erreurs `try/except`
5. Mots de passe en clair → hachage avec `bcrypt`

Voir `RAPPORT_AUDIT.md` pour le détail complet.

## ⚠️ Note
Projet réalisé dans le cadre du stage virtuel CodeAlpha en cybersécurité.