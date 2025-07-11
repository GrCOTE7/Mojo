# Test rapide Py (flet run tp.py)

import flet as ft
import tools.gc7 as gc7
from time import time
from tools.gc7 import EC, EW, ER, EN


def app(page: ft.Page):
    page.title = "Flet App"
    gc7.flet_window_position(page)

    txt = "Ready21."
    t = ft.Text(txt, size=24, color=ft.Colors.ORANGE_500)
    page.add(t)
    main(page)
    print(gc7.theTime())


def main(page):
    line = "Ok 12345"
    length = len(line)
    print("-" * length)
    print(line)
    page.add(ft.Text(f"{line}"))
    print("-" * length)


if __name__ == "__main__":
    # main()
    pass

ft.app(target=app)
