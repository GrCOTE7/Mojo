#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("langages1/count/n.txt");
    if (!file) {
        std::cerr << "❌ Erreur : Le fichier 'n.txt' est introuvable\n";
        return 1;
    }

    std::string line;
    if (!std::getline(file, line)) {
        std::cerr << "❌ Erreur : Impossible de lire le fichier 'n.txt'\n";
        return 1;
    }

    try {
        long long n = std::stoll(line) + 1;
        for (long long i = 1; i < n; ++i) {
            if (i < 4) {
                std::cout << i << ", ";
            }
        }
        std::cout << "\n";
    } catch (...) {
        std::cerr << "❌ Erreur : Le fichier 'n.txt' ne contient pas un entier valide\n";
        return 1;
    }

    return 0;
}
