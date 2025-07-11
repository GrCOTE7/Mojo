from pathlib import Path

def main():
    try:
        n_path = Path(__file__).resolve().parent / "n.txt"
        with open(n_path, "r") as file:
            n = int(file.read().strip()) + 1
        for i in range(1, n):
            if i < 4:
                print(i, end=", ")
    except ValueError:
        print("❌ Erreur : Le fichier 'n.txt' ne contient pas un entier valide")
    except FileNotFoundError:
        print("❌ Erreur : Le fichier 'n.txt' est introuvable")
main()
