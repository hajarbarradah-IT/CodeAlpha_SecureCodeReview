import sqlite3
import os
import bcrypt
from ast import literal_eval

DB_PASSWORD = os.environ.get("DB_PASSWORD", "valeur_par_defaut_si_non_definie")
API_KEY = os.environ.get("API_KEY", "valeur_par_defaut_si_non_definie")

def hacher_mot_de_passe(mot_de_passe):
    # Convertit le mot de passe en bytes, puis le hache avec un "sel" généré automatiquement
    return bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())

def verifier_mot_de_passe(mot_de_passe_tape, hachage_stocke):
    # Compare le mot de passe tapé (re-haché en interne) avec le hachage stocké
    return bcrypt.checkpw(mot_de_passe_tape.encode('utf-8'), hachage_stocke)

def connexion_utilisateur(nom_utilisateur, mot_de_passe):
    connexion = sqlite3.connect("utilisateurs.db")
    curseur = connexion.cursor()

    requete = "SELECT motdepasse FROM users WHERE nom = ?"
    curseur.execute(requete, (nom_utilisateur,))
    resultat = curseur.fetchone()

    if resultat and verifier_mot_de_passe(mot_de_passe, resultat[0]):
        print("Connexion réussie pour " + nom_utilisateur)
        return True
    else:
        print("Échec de connexion")
        return False

def calculer_expression(expression_utilisateur):
    try:
        resultat = literal_eval(expression_utilisateur)
        return resultat
    except (ValueError, SyntaxError):
        print("Erreur : expression invalide")
        return None

def sauvegarder_log(message):
    fichier = open("logs.txt", "a")
    fichier.write(message + "\n")
    fichier.close()

def afficher_infos_utilisateur(age_utilisateur):
    try:
        age = int(age_utilisateur)
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide pour l'âge")
        return

    if age >= 18:
        print("Utilisateur majeur")
    else:
        print("Utilisateur mineur")

def preparer_base_de_donnees():
    connexion = sqlite3.connect("utilisateurs.db")
    curseur = connexion.cursor()
    curseur.execute("CREATE TABLE IF NOT EXISTS users (nom TEXT, motdepasse TEXT)")

    # On vérifie si l'utilisateur existe déjà, pour ne pas le recréer à chaque lancement
    curseur.execute("SELECT * FROM users WHERE nom = 'hajar'")
    if not curseur.fetchone():
        mot_de_passe_hache = hacher_mot_de_passe("motdepasse123")
        curseur.execute("INSERT INTO users VALUES (?, ?)", ("hajar", mot_de_passe_hache))

    connexion.commit()
    connexion.close()


preparer_base_de_donnees()

print("--- Test 1 : Connexion normale ---")
connexion_utilisateur("hajar", "motdepasse123")

print("--- Test 2 : Calcul normal ---")
resultat = calculer_expression("2 + 2")
print("Résultat :", resultat)

print("--- Test 3 : Âge valide ---")
afficher_infos_utilisateur("25")

print("--- Test 4 : Âge invalide ---")
afficher_infos_utilisateur("vingt-cinq")