from pathlib import Path
import os, subprocess, sys, time

sys.path.append(str(Path(__file__).resolve().parent.parent))

import tools.gc7 as gc7
from tools.gc7 import EC, EW, ER, EN  # En Cyan, Rouge, En Normal

# Py VS Mojo (Nb itérations transmis par fichier)

@gc7.chrono
def run_script(lang):
    n_txt_path = from_root("benchmarks", "langages1", "count", "n.txt")
    if lang == "python":
        subprocess.run(["python", from_root("benchmarks", "langages1", "count", "n.py")])
    else:
        subprocess.run(["mojo", "run", from_root("benchmarks", "langages1", "count", "n.mojo"), "--", str(n_txt_path)])

# def run_script(lang):
#     (
#         subprocess.run(["python", from_root("benchmarks", "langages1", "count", "n.py")])
#         if lang == "python"
#         else subprocess.run(["mojo", "run",  from_root("benchmarks", "langages1", "count", "n.mojo")])
#     )

def from_root(*parts):
    return Path(__file__).resolve().parent.parent.joinpath(*parts)
  
langs = ["python", "mojo"]
for n in [7, 77_777, 1e7, 2.7773e7, 1e8, 1e9, 1e12][:2]:  # [:5] pour test
    with open(from_root("benchmarks","langages1", "count", "n.txt"), "w") as f:
        f.write(str(int(n)))
    time.sleep(1)
    for lang in langs:
        if not (lang == "python" and n > 1e11):
            run_script(lang)
            line = f"\b\b... J'ai compté jusqu'à {EC}{gc7.nf(n,0):>17}{EN} en {EW}{lang[0].upper() + lang[1:].lower():^6}{EN} → ⏱️ : {ER}{gc7.nf(run_script.duration,2):>9}{EN} secondes"
            print(line)
    print("─" * (gc7.rawStrLength(line)[0] + 4))
print("Fini:", gc7.theTime())
