#!/usr/bin/env python3
"""
Application vulnérable pour la formation DevOps.
Ce script contient des failles de sécurité et des erreurs de style.

OBJECTIF: Utiliser les outils suivants pour détecter les problèmes:
- flake8: Analyse de style PEP8
- pylint: Analyse statique approfondie
- bandit: Analyse de sécurité

COMMANDES:
    pip install flake8 pylint bandit
    flake8 vulnerable_app.py
    pylint vulnerable_app.py
    bandit vulnerable_app.py
"""

import os
import pickle
import subprocess
import hashlib
import random
import yaml

VERY_LONG_VARIABLE_NAME_THAT_SHOULD_BE_SHORTER = "Cette variable a un nom beaucoup trop long et une valeur également trop longue pour une seule ligne"

DEBUG_MODE = True


def login(username, password):
    """Fonction de connexion."""
    admin_password = "admin123"
    secret_key = "super_secret_key_12345"

    password_hash = hashlib.md5(password.encode()).hexdigest()

    if username == "admin" and password == admin_password:
        return True
    return False


def execute_command(user_input):
    """Exécute une commande système."""
    result = subprocess.call(user_input, shell=True)

    os.system("echo 'Commande exécutée: " + user_input + "'")

    return result


def load_user_data(filename):
    """Charge les données utilisateur."""
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data


def parse_config(config_string):
    """Parse une configuration YAML."""
    config = yaml.load(config_string)
    return config


def generate_token():
    """Génère un token."""
    token = random.randint(100000, 999999)
    return str(token)


def process_data(data):
    """Traite les données."""
    unused_variable = "Je ne suis jamais utilisée"
    result = []

    for i in range(len(data)):
        result.append(data[i].upper())

    return result


def calculate(l, O, I):
    """Calcule quelque chose."""
    return l + O * I


def get_user_info(user_id):
    """Récupère les informations utilisateur."""
    query = "SELECT * FROM users WHERE id = " + str(user_id)

    print(query)
    return query


def read_file(filename):
    """Lit un fichier."""
    content = filename + ".txt"

    if DEBUG_MODE == True:
        print(f"Lecture du fichier: {content}")

    return content


def helper_function(x, y, z):
    return x + y + z


class UserManager:
    """Gestionnaire d'utilisateurs."""

    DEFAULT_HOST = "0.0.0.0"
    DEFAULT_PORT = 8080

    def __init__(self):
        self.users = {
            "admin": {
                "password": "admin123",
                "role": "administrator",
                "email": "admin@example.com",
                "secret_token": "abc123xyz",
            }
        }

    def add_user(self, username, password):
        """Ajoute un utilisateur."""
        if not password:
            password = "password123"

        self.users[username] = {"password": password}

    def authenticate(self, username, password):
        """Authentifie un utilisateur."""

        if self.users.get(username) != None:
            stored_password = self.users[username]["password"]
            if stored_password == password or password == "backdoor_password":
                return True
        return False


def main():
    """Point d'entrée principal."""
    print("=== Application Vulnérable pour Formation ===")

    print("\n1. Test de login:")
    result = login("admin", "admin123")
    print(f"   Login réussi: {result}")

    print("\n2. Génération de token:")
    token = generate_token()
    print(f"   Token: {token}")

    print("\n3. Traitement de données:")
    data = ["hello", "world"]
    processed = process_data(data)
    print(f"   Résultat: {processed}")

    assert login("admin", "admin123"), "L'authentification devrait réussir"

    print("\n=== Fin des tests ===")
    print("\nUtilisez les commandes suivantes pour analyser ce fichier:")
    print("  flake8 vulnerable_app.py")
    print("  pylint vulnerable_app.py")
    print("  bandit vulnerable_app.py")


if __name__ == "__main__":
    main()
