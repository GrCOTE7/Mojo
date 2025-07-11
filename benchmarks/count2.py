from pathlib import Path
import os, subprocess, sys, time

sys.path.append(str(Path(__file__).resolve().parent.parent))

import tools.gc7 as gc7
from tools.gc7 import EC, EW, ER, EN  # En Cyan, Rouge, En Normal

# Configuration
langs = ["python", "mojo", "cpp"] # Langages testés
script_dir = Path("langages1/count") # Dossier contenant les scripts à chronométrer
nb_values = [7, 77_777, 1e7, 2.7773e7, 1e8, 1e9, 1e10, 1e11, 1e12][:-3]  # valeurs de tests

results = []
# Fonction de benchmark
def run_script(lang, n):
    with open(script_dir / "n.txt", "w") as f:
        f.write(str(int(n)))

    time.sleep(0.5)  # Laisse le temps au fichier d'être écrit

    start = time.time()
    
    if lang == "python":
        subprocess.run(["python", script_dir / "n.py"], stdout=subprocess.DEVNULL)
        
    elif lang == "mojo":
        subprocess.run(["mojo", "run", script_dir / "n.mojo"], stdout=subprocess.DEVNULL)
        
    elif lang == "cpp":
        # Compile si nécessaire
        exe = script_dir / "n_cpp"
        if not exe.exists():
            subprocess.run(["g++", "-O2", "-o", exe, script_dir / "n.cpp"])
        subprocess.run([exe], stdout=subprocess.DEVNULL)
        
    end = time.time()

    return end - start

# Lancement des benchmarks
no_tested = '-' + ' '*2
for nb in nb_values:
    row = {"nb": int(nb)}
    for lang in langs:
        if lang == "python" and nb > 1e10: # 1e10
            row[lang] = no_tested
        else:
            duration = run_script(lang, nb)
            row[lang] = f"{duration:.2f}"
        
        print (f"{lang.capitalize()} {row[lang]:>6} | ", end='') 
        
    results.append(row)
    print(f"{gc7.nf(nb,0):>16} / {gc7.nf(nb_values[-1],0):>17}")

# Affichage du tableau
print("\n📊 Résultats du benchmark (Tps en secondes) :\n")
header = f"{'n':^19} | {'Python':^7} | {'Mojo':^7} | {'C++':^7}"
print(header)
print("-" * (len(header)+1))

for row in results:
    nb = f"{row['nb']:,}".replace(",", " ")
    py, mj, cp = [row[i] for i in langs]
    print(f"{nb:>17} | {py:>7} | {mj:>7} | {cp:>7}")

print("\n✅ Fini à", time.strftime("%H:%M:%S"))
