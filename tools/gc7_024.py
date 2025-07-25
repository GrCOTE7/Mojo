from datetime import datetime as dt

import locale
import time as time
import flet as ft

# [ ] //2fix Cf. utilisation locale dans APK...
# locale.setlocale(locale.LC_ALL, "fr_FR")
THEME_MODE = ft.ThemeMode.DARK

# v0.00.004a

EC = "\033[1;36m"  # En gras Cyan - Bold
EW = "\033[1m"     # En gras - Bold
ER = "\033[1;31m"  # En gras Rouge - Bold
EN = "\033[0m"     # Normal


def nf(f, dec=2, lang="fr_FR.UTF-8"):
    """Format number with grouping and decimal precision, locale-aware."""
    try:
        locale.setlocale(locale.LC_ALL, lang)
    except locale.Error:
        pass  # Ignore if locale not available
    # If not already installed, in linux (Or WSL):
    # sudo locale-gen fr_FR.UTF-8
    # sudo update-locale

    try:
        f = float(f)
        fmt = "%.{0}f".format(dec)
        return locale.format_string(fmt, f, grouping=True)
    except Exception as e:
        return str(f)  # Fallback: return unformatted


def nf_ori(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    try:
        f = float(f)
        return locale.format_string(f"%.{dec}f", f, grouping=True)
    except ValueError:
        src = caller_info()
        # print(src)
        print(
            f"⚠️ Errorfor nf() in main_tools:\n\033[1;31mBad data type ({type(f).__name__}) -> {f} (Line {src[2]} in {src[0]}){EB}"
        )
        return str(f)


def flet_window_position(page):
    page.theme_mode = "dark"
    screen_width = 1920 # 1920
    window_width = 1920 # 520
    page.window.top = 3
    # page.window.left = screen_width - window_width
    page.window.left = 0
    page.window.height = 505 # 1005
    page.window.width = window_width - 15
    page.window.width = 100
    page.window.resizable = False
    # page.update()


def themed_border_color(dark: bool) -> ft.Colors:
    return ft.colors(141, 145, 153) if dark else ft.colors(115, 119, 127)


def rawStrLength(s: str) -> tuple:
    """Lenght without color codes ou {sb} or {eb}\n
    Return (tuple) Length without color codes, length of color codes)
    Sum of these data is complete length
    """
    import re

    s_ori = len(s)
    # matches = list(re.finditer(r"\b", s))
    # subantislashb = len(matches)
    # Regex pour supprimer les séquences \033[...m et {EC}, {EN}
    cleanedStr = len(re.sub(r"\033\[[0-9;]*m|{EC}|{EW}|{ER}|{EN}", "", s))
    return (cleanedStr, s_ori - cleanedStr)


def btn(label, action=None, btnWidth=None):
    return ft.OutlinedButton(
        label,
        on_click=action,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=7),
            padding=ft.padding.symmetric(horizontal=10, vertical=7),
            color="cyan",
        ),
        width=btnWidth or 100,
        height=40,
    )


def theTime(page=None):
    now = dt.now()
    theTime = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    # print(theTime, page.route)
    return theTime


# def nf(f, dec=2):
#     "Number Format 123456789 → 123 456,79"
#     try:
#         f = float(f)
#         return locale.format_string(f"%.{dec}f", f, grouping=True)
#     except ValueError:
#         src = caller_info()
#         # print(src)
#         print(
#             f"⚠️ Errorfor nf() in main_tools:\n\033[1;31mBad data type ({type(f).__name__}) -> {f} (Line {src[2]} in {src[0]}){EB}"
#         )
#         return str(f)


def toggleTheme(page: ft.Page) -> ft.IconButton:
    """
    Retourne un bouton animé qui change le thème clair/sombre
    et affiche un SnackBar flottant avec l'info.
    """
    # Déclaration du bouton AVANT la fonction pour qu'on puisse le modifier depuis toggle()
    theme_btn = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        icon_color="gold",
        icon_size=32,
        tooltip="Changer le thème",
        on_click=None,
    )

    def toggle(e):
        is_light = page.theme_mode == ft.ThemeMode.LIGHT
        page.theme_mode = ft.ThemeMode.DARK if is_light else ft.ThemeMode.LIGHT

        # Met à jour l'icône du bouton
        theme_btn.icon = ft.Icons.LIGHT_MODE if is_light else ft.Icons.DARK_MODE
        # theme_btn.icon_color = "gold" if is_light else "lightblue"

        # Affiche une SnackBar
        snackbar = ft.SnackBar(
            content=ft.Text(
                f"{'🌙' if is_light else '🌞'} Thème {'sombre' if is_light else 'clair'} activé",
                color="cyan",
            ),
            bgcolor="black" if not is_light else "white",
            behavior=ft.SnackBarBehavior.FLOATING,
            duration=2000,
        )
        page.overlay.append(snackbar)
        snackbar.open = True
        page.update()

    theme_btn.on_click = toggle

    return theme_btn


import os, shutil, subprocess


def reset_venv(requirements_file="requirements.txt"):
    """
    Supprime et recrée venv, puis installe les dépendances.
    """
    print("🔧 [gc7] Réinitialisation de l'environnement virtuel...")

    if os.path.isdir("venv"):
        shutil.rmtree("venv")
        print("🗑️ venv supprimé.")
    else:
        print("💡 Aucun venv existant.")

    os.system("python -m venv .venv")
    print("✅ Nouveau venv créé.")

    pip_path = os.path.join("venv", "Scripts", "pip.exe")

    if os.path.isfile(requirements_file):
        subprocess.run([pip_path, "install", "-r", requirements_file])
        print(f"📦 Dépendances installées depuis {requirements_file}.")
    else:
        subprocess.run([pip_path, "install", "flet"])
        print("📦 Flet installé par défaut.")

    print("🚀 Environnement prêt !")


def chrono(function):
    """Décorateur: Calcule le temps en secondes que met une fonction à s'executer.\n
    Placer @ chrono dans la ligne précédent le def de la fonction."""

    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # (Le temps "epoch").
        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans "start", et celui qui sera gardé dans "end". ;)
        wrapper.duration = end - start

        # print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")
        # print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")

        return result

    wrapper.__doc__ = function.__doc__
    return wrapper
