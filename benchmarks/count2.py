from pathlib import Path
import os, subprocess, sys, time

sys.path.append(str(Path(__file__).resolve().parent.parent))

import tools.gc7 as gc7
from tools.gc7 import EC, EW, ER, EN  # En Cyan, Rouge, En Normal

# Py VS Mojo VS C++ (Nb itérations transmis par fichier)

# Configuration
langs = ["python", "mojo", "cpp", "rust"]  # Langages testés
script_dir = Path("langages1/count")  # Dossier contenant les scripts à chronométrer
nb_values = [7, 77_777, 1e7, 2.7773e7, 1e8, 1e9, 1e10, 1e11, 1e12][:-1] # valeurs de tests

results = []
# Fonction de benchmark
langs_O = ["python", "mojo", "cpp", "rust"]  # Langages testés

LANGS = {
    "python": {
        "src": "n.py",
        "run": lambda src, exe: ["python", src],
    },
    "mojo": {
        "src": "n.mojo",
        "exe": "n_mojo",
        "build": lambda src, exe: ["mojo", "build", src, "-o", exe],
        "run": lambda src, exe: [exe],
    },
    "cpp": {
        "src": "n.cpp",
        "exe": "n_cpp",
        "build": lambda src, exe: ["g++", "-O3", "-o", exe, src],
        "run": lambda src, exe: [exe],
    },
    "rust": {
        "src": "n.rs",
        "exe": "n_rs",
        "build": lambda src, exe: ["rustc", "-C", "opt-level=3", "-o", exe, src],
        "run": lambda src, exe: [exe],
    },
}


def run_script(lang, n):
    lang_data = LANGS[lang]
    src = script_dir / lang_data["src"]
    exe = script_dir / lang_data.get("exe", "") if lang_data.get("exe") else None

    # 🔧 Compilation si nécessaire
    if exe:
        if not exe.exists() or os.path.getmtime(exe) < os.path.getmtime(src):
            subprocess.run(lang_data["build"](src, exe))

    # 🚀 Lancement
    start = time.time()
    # Pour ne pas avoir les sorties des subprocesses:
    subprocess.run(lang_data["run"](src, exe), stdout=subprocess.DEVNULL)
    # Pour avoir la sortie des subprocesses:
    # subprocess.run(lang_data["run"](src, exe))
    end = time.time()

    return end - start

    # elif lang == "java":
    #     class_file = script_dir / "N.class"
    #     if not class_file.exists():
    #         subprocess.run(["javac", script_dir / "N.java"])
    #     subprocess.run(["java", "-cp", script_dir, "N"], stdout=subprocess.DEVNULL)


# Lancement des benchmarks
no_tested = "-" + " " * 2

n_path = script_dir / "n.txt"
if n_path.exists():
    n_path.unlink()

for nb in nb_values:
    row = {"nb": int(nb)}

    with open(script_dir / "n.txt", "w") as f:
        f.write(str(int(nb)))

    time.sleep(0.5)  # Laisse le temps au fichier d'être écrit
    for lang in langs:
        if lang == "python" and nb > 1e7:  # 1e10
            row[lang] = no_tested
        else:
            duration = run_script(lang, nb)
            row[lang] = f"{duration:.2f}"

        print(f"{lang.capitalize()} {row[lang]:>6} | ", end="")

    results.append(row)
    print(f"{gc7.nf(nb,0):>16} / {gc7.nf(nb_values[-1],0):>17}")

# Affichage du tableau
print("\n📊 Résultats du benchmark (Tps en secondes) :\n")
header = f"{'n':^17} | {'Python':^7} | {'Mojo':^7} | {'C++':^7} | {'RustC':^7}"
print(header)
print("-" * (len(header) + 1))

for row in results:
    nb = f"{row['nb']:,}".replace(",", " ")
    py, mj, cp, rs = [row[i] for i in langs]
    print(f"{nb:>17} | {py:>7} | {mj:>7} | {cp:>7} | {rs:>7}")

print("\n✅ Fini à", time.strftime("%H:%M:%S"))
