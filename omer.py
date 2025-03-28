import random
import string
from colorama import Fore, Style, init

init()

def print_centered(text, decoration=False):
    """Affiche le texte centré dans la console, avec option de décoration."""
    width = 80
    if decoration:
        print("─" * width)
    print(text.center(width))
    if decoration:
        print("─" * width)

def generate_random_string():
    """Génère une chaîne aléatoire composée de lettres, chiffres et symboles."""
    length = random.randint(5, 20)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string

def encoder(message):
    """Encode chaque lettre du message avec des chaînes aléatoires."""
    encoded_message = []
    decryption_key = ""
    for char in message:
        if char in string.ascii_letters: 
            encoded_char = ""
            for _ in range(3):
                multiplier = random.randint(1, 10000)
                random_part = generate_random_string()
                number = random.randint(1, 9)
                encoded_char += f"{char}{random_part}{number}x{multiplier}"
            encoded_message.append(encoded_char)
            decryption_key += "1"
        else:
            encoded_message.append(char)
            decryption_key += "0"
    return " ".join(encoded_message), decryption_key

def decoder(encoded_message, decryption_key):
    """Décode le message encodé en utilisant la clé binaire."""
    encoded_parts = encoded_message.split(" ")
    decoded_message = ""
    
    for part, key in zip(encoded_parts, decryption_key):
        if key == "1":
            decoded_message += part[0]
        elif key == "0":
            decoded_message += part
    
    return decoded_message

def main():
    print_centered(Fore.GREEN + "░░░░░▄▄▄▄███▄▄▄▄░░░░░░░░░░░░░ ")
    print_centered(Fore.GREEN + "░░░▄▄█▀░░░░░░░░░▀▀▄▄░░░░░░░░░░")
    print_centered(Fore.GREEN + "░█▀░░░░░░░░░░░░░░░░░░█▄░░░░░░░")
    print_centered(Fore.GREEN + "██░░░░░░░░░░░░░░░░░░░░█▄░░░░░░")
    print_centered(Fore.GREEN + "█░░░░░░░░░░░░░░░░░░░░░░█▄░░░░░")
    print_centered(Fore.GREEN + "██░░░░░░░░░░░░▄▄▄▄▄█▀▀▀██▄░░░░")
    print_centered(Fore.GREEN + "▀█░░░░░░░░░▄█▀▀░░▀▀█▄░░░░█▄░░░")
    print_centered(Fore.GREEN + "░█▄░▄░░░░░▄█░░░░░░░░█▄░█░░█░░░")
    print_centered(Fore.GREEN + "░▄█▄██▄░░░█▄░░██░░░░██▄▄▄██░░░")
    print_centered(Fore.GREEN + "░████░▀▀░░░█▄░░░░░░▄█░░░░░██░░")
    print_centered(Fore.GREEN + "░█░░██▄▄░░░░▀██▄▄██▀▄▄▄▄▄▄█░░░")
    print_centered(Fore.GREEN + "░░▄█▀░░░░░░░░▄▄██▀▀▀▀▀▀▀░▀█▄░")
    print_centered(Fore.GREEN + "░░▀█░░░░░░░▄█▀▀░░░░░░░░░░░░░█▄")
    print_centered(Fore.GREEN + "░░░▀█▄▄█▀░█▀░░░░░░░░░░░░░░░▄█▀")
    print_centered(Fore.GREEN + "░░░░░░██░▄█░░░█▀██▀▀█▀██▀▀▀▀░░")
    print_centered(Fore.GREEN + "░░░░░▄█░░▀█░░▀█░█░░██░██░░░░░░")
    print_centered(Fore.GREEN + "░░░░██▀█▄░▀█▄░▀▀████▀▀██░░░░░░")
    print_centered(Fore.GREEN + "░░░░█░░░▀▀█▄▀█▄▄▄▄▄▄▄▄██▄░░░░")
    print_centered(Fore.GREEN + "Omer")
    print_centered(Fore.GREEN + "By Gweltaz" + Style.RESET_ALL, decoration=True)

    print_centered(Fore.CYAN + "[1] Encoder", decoration=True)
    print_centered(Fore.CYAN + "[2] Décoder" + Style.RESET_ALL, decoration=True)

    choice = input(Fore.YELLOW + "Choisissez une option : " + Style.RESET_ALL)
    if choice == "1":
        print_centered(Fore.BLUE + ">> ENCODAGE <<", decoration=True)
        message = input(Fore.GREEN + "Entrez le message à encoder : " + Style.RESET_ALL)
        encoded_message, decryption_key = encoder(message)
        print_centered(Fore.GREEN + "\nMessage encodé :", decoration=True)
        print_centered(Fore.GREEN + encoded_message + Style.RESET_ALL)
        print_centered(Fore.GREEN + "\nClé de déchiffrement :", decoration=True)
        print_centered(Fore.GREEN + decryption_key + Style.RESET_ALL)
    elif choice == "2":
        print_centered(Fore.BLUE + ">> DÉCODAGE <<", decoration=True)
        encoded_message = input(Fore.GREEN + "Entrez le message encodé : " + Style.RESET_ALL)
        decryption_key = input(Fore.GREEN + "Entrez la clé de déchiffrement (binaire) : " + Style.RESET_ALL)
        decoded_message = decoder(encoded_message, decryption_key)
        print_centered(Fore.GREEN + "\nMessage décodé :", decoration=True)
        print_centered(Fore.GREEN + decoded_message + Style.RESET_ALL)
    else:
        print_centered(Fore.RED + "Option invalide. Veuillez choisir 1 ou 2." + Style.RESET_ALL, decoration=True)

def decoder(encoded_message, decryption_key):
    """Décode le message encodé en utilisant la clé binaire."""
    encoded_parts = encoded_message.split(" ")
    decoded_message = ""
    
    for part, key in zip(encoded_parts, decryption_key):
        if key == "1" and part:
            decoded_message += part[0]
        elif key == "0" and part:
            decoded_message += part
        else:
            decoded_message += ""
    
    return decoded_message


if __name__ == "__main__":
    main()
