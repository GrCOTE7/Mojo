#!/bin/bash
TARGET=${1:-main.mojo}
echo "🚀 Lancement de $TARGET avec surveillance des fichiers .mojo"
find . -name "*.mojo" | entr -r pixi run mojo run "$TARGET"

# Fichier cible : argument ou main.mojo par défaut

# Vérifie si on est déjà dans l'environnement pixi
# if [ -z "$IN_PIXI_ENV" ]; then
#     echo "🔄 Pas dans l'environnement pixi, on y entre..."
#     exec env IN_PIXI_ENV=1 pixi run -- bash "$0" "$TARGET"
# fi
# echo "✅ Dans l'environnement pixi"

# Poser dans : ~/.bashrc (Adapter si besoin):
# alias py=python3
# alias run='sh //home/gc7/Mojo/run.sh'

# CTRL + D ou exit pour sortir du shell ( = deactivate de pip venv)
