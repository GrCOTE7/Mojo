#include <iostream>
#include <fstream>

int main() {
    std::ifstream file("apps/count/n.txt");
    long long n;
    file >> n;

    volatile long long count = 0;
    for (long long i = 0; i < n; ++i) {
        count += 1;
    }

    std::cout << "C++ counted to " << count << std::endl;
    return 0;
}
// ⚠️ Le mot-clé volatile empêche le compilateur d’optimiser la boucle en la supprimant
