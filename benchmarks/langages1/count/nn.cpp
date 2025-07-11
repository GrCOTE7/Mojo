#include <iostream>
#include <fstream>
#include <chrono>

int main() {
    std::ifstream file("apps/count/n.txt");
    long long n;
    file >> n;

    auto start = std::chrono::steady_clock::now();
    volatile long long count = 0;
    for (long long i = 0; i < n; ++i) {
        count++;
    }
    auto end = std::chrono::steady_clock::now();
    double duration = std::chrono::duration<double>(end - start).count();

    std::cout << "✅ C++ → Counted to " << count << " in " << duration << "s\n";
}
