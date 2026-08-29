import sqlite3

# Configuration de la base de données
DB_PASSWORD = "admin123"
API_KEY = "sk-a1b2c3d4e5f6"

def connexion_utilisateur(nom_utilisateur, mot_de_passe):
    connexion = sqlite3.connect("utilisateurs.db")
    curseur = connexion.cursor()

    requete = "SELECT * FROM users WHERE nom = '" + nom_utilisateur + "' AND motdepasse = '" + mot_de_passe + "'"
    curseur.execute(requete)
    resultat = curseur.fetchone()

    if resultat:
        print("Connexion réussie pour " + nom_utilisateur)
        return True
    else:
        print("Échec de connexion")
        return False

def calculer_expression(expression_utilisateur):
    resultat = eval(expression_utilisateur)
    return resultat

def sauvegarder_log(message):
    fichier = open("logs.txt", "a")
    fichier.write(message + "\n")
    fichier.close()

def afficher_infos_utilisateur(age_utilisateur):
    age = int(age_utilisateur)
    if age >= 18:
        print("Utilisateur majeur")
    else:
        print("Utilisateur mineur")

connexion_utilisateur("hajar", "motdepasse123")
calculer_expression("2 + 2")