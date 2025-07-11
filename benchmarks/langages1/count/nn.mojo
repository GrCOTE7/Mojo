from time import monotonic_seconds  # si disponible dans ta build

def main():
    let f = open("apps/count/n.txt")
    let n = parse_int(f.read())

    let start = monotonic_seconds()
    var count = 0
    for i in range(n):
        count += 1
    let duration = monotonic_seconds() - start

    print("✅ Mojo → Counted to", count)
    print("⏱️ Duration:", duration)
