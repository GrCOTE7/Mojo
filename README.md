# Mojo - Installation

## 1. Si projet non Mojo: VIRTUALENV suffit

### Crée l'environement virtuel

```bash
python -m venv .venv
```
### Activer l'environement virtuel (Ne sert alors que pour python)

* Windows (Note: Mojo ne marche pas sous windows
  ou alors, avec **WSL**)

```bash
.venv/Scripts/activate
```
  
* **Linux**/**MacOSX** (Ou **WSL**):

```bash
source ./.venv/bin/activate
```

### 3. Installe les dépendances

```bash
pip install -r requirements.txt
```

(*requirements.txt* généré par:)
```bash
pip freeze > requirements.txt
```

N.B.: Si **pip** absent:

```bash
python -m pip install --upgrade pip
```

Et si ça ne marche pas:

```bash
py tools/get-pip_basic.py
```

### Si juste flet pour avoir le hot-reload

```bash
flet run -r
```

### Divers tips

* Installer un 'vieux' python dans une venv

```bash
virtualenv .venv --python="D:\chemin\vers\python310\python.exe"
```

## 2. Pour MOJO (Linux ou WSL) - Remplace Virtualenv

### Installe pixi:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
export PATH="$HOME/.pixi/bin:$PATH"
source ~/.bashrc

pixi --version

pixi shell # Entre dans l'environnement & deactivate pour en sortir
```

### Puis créee le projet Mojo:

```bash
pixi init mojo-projet \
  -c https://conda.modular.com/max-nightly/ \
  -c conda-forge
cd mojo-projet
pixi add modular
pixi run mojo --version

pixi add moduleName
```

### Exécute le programme avec hot-leload

```bash
ls *.mojo | entr -r pixi run mojo run hello.mojo
```
