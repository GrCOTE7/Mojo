from time import perf_counter_ns as top


fn fibonacci(n: Int) -> Int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fn main():
  
    var start = top()  # 👈 début en nanosecondes
    for i in range(41):
        print(i, fibonacci(i), "|", end=" ")
    print("\n")
    var end = top()  # 👈 fin

    var duration = (end - start) / 1e9  # conversion en secondes
    print("Temps d'exécution total :", round(duration,3), "secondes")
