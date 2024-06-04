import os
import subprocess
import sys

def install_requests():
    try:
        import requests
    except ImportError:
        print("Le module 'requests' n'est pas installé. Installation en cours...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests

install_requests()

import requests

def clear_screen():
    try:
        if os.name == 'nt':
            subprocess.run('cls', shell=True)
        else:
            subprocess.run('clear', shell=True)
    except Exception as e:
        print(f"Erreur lors du nettoyage de l'écran : {e}")

def afficher_menu():
    clear_screen()
    print("\033[94m" + """
 ██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝
██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗
██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                    insérez 1 pour lancer le webhook
                    insérez 2 pour protéger un token
                    insérez 0 pour quitter
""" + "\033[0m")

def confirmer_execution():
    while True:
        confirm = input("Êtes-vous sûr de vouloir exécuter ? (O/N) : ").upper()
        if confirm == "O":
            return True
        elif confirm == "N":
            return False
        else:
            print("Choix invalide. Veuillez entrer O ou N.")

def envoyer_message(url_webhook, message, nombre):
    for i in range(nombre):
        response = requests.post(url_webhook, json={"content": message})
        if response.status_code == 204:
            print(f"Message {i+1} envoyé avec succès.")
        else:
            print(f"Échec de l'envoi du message {i+1}. Code d'état HTTP : {response.status_code}, Réponse : {response.text}")

def lancer_webhook():
    url_webhook = input("Entrez l'URL du webhook : ")
    if confirmer_execution():
        message = input("Entrez le message à envoyer : ")
        try:
            nombre = int(input("Entrez le nombre de messages à envoyer : "))
            if nombre <= 0:
                print("Veuillez entrer un nombre positif.")
            else:
                envoyer_message(url_webhook, message, nombre)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    else:
        print("Opération annulée.")

def proteger_token():
    token = input("Entrez le token à protéger : ")
    token_protege = token[:-3] + "***"
    print(f"Token protégé : {token_protege}")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            lancer_webhook()
        elif choix == "2":
            proteger_token()
        elif choix == "0":
            print("Quitter...")
            break
        else:
            print("Option invalide. Veuillez choisir à nouveau.")

        input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
        input("Appuyez sur Entrée pour fermer le programme...")
