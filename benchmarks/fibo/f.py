from time import perf_counter_ns as top


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":

    start = top()  # 👈 début en nanosecondes
    for i in range(41):
        print(i, fibonacci(i), "|", end=" ")
    end = top()  # 👈 fin

    duration = (end - start) / 1e9  # conversion en secondes
    print("\n\nTemps d'exécution total :", round(duration, 3), "secondes")
