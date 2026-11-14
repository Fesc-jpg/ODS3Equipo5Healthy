import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
from pathlib import Path

FONDO = "#C2DBFF"
AZUL = "#0047AB"
ROJO_SALIR = "#FF3B3B"

ESTADOS = {
    "completado": {"titulo": "Completado", "bg": "#C6F7E6", "fg": "#007A55", "circulo": "#10BC83", "simbolo": "#9AB93A"},
    "proceso": {"titulo": "En Proceso", "bg": "#FFE6C2", "fg": "#FF914D", "circulo": "#FF914D", "simbolo": "#FF6F1F"},
    "tardio": {"titulo": "Tardío", "bg": "#FFB0B0", "fg": "#C41E32", "circulo": "#FF2A2A", "simbolo": "#C41E32"},
}


def rect_redondeado(c, x1, y1, x2, y2, r, **kw):
    pts = [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2,
           x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


def dibujar_icono(c, estado, cx, cy):
    e = ESTADOS[estado]
    c.create_oval(cx-44, cy-44, cx+44, cy+44, fill=e["circulo"], outline="")
    if estado == "completado":
        c.create_line(cx-30, cy-8, cx-12, cy+26, cx+36, cy-52, fill=e["simbolo"], width=12, smooth=True)
    elif estado == "proceso":
        c.create_text(cx, cy, text="~", fill=e["simbolo"], font=("Verdana", 54, "bold"))
    else:
        c.create_text(cx, cy, text="X", fill=e["simbolo"], font=("Verdana", 72, "bold"))


def tarjeta(parent, estado, hora, medicina, dosis):
    e = ESTADOS[estado]
    c = tk.Canvas(parent, width=750, height=180, bg=FONDO, highlightthickness=0)
    rect_redondeado(c, 2, 2, 748, 178, 24, fill=e["bg"], outline=e["bg"])
    c.create_text(16, 28, text=e["titulo"], anchor="w", fill=e["fg"], font=("Verdana", 18, "bold"))
    fb = ("Verdana", 14, "bold")
    c.create_text(30, 78, text="Tomada:", anchor="w", fill="black", font=fb)
    c.create_text(200, 78, text="Medicina:", anchor="w", fill="black", font=fb)
    c.create_text(400, 78, text="Dosis:", anchor="w", fill="black", font=fb)
    c.create_text(30, 128, text=hora, anchor="w", fill="black", font=fb)
    c.create_text(200, 128, text=medicina, anchor="w", fill="black", font=fb, width=190)
    c.create_text(400, 128, text=dosis, anchor="w", fill="black", font=fb, width=170)
    dibujar_icono(c, estado, 660, 90)
    return c


def boton_redondo(parent, texto, color, comando, ancho, alto, fg="white"):
    c = tk.Canvas(parent, width=ancho, height=alto, bg=FONDO, highlightthickness=0)
    rect_redondeado(c, 2, 2, ancho-2, alto-2, alto//2, fill=color, outline=color)
    c.create_text(ancho/2, alto/2, text=texto, fill=fg, font=("Verdana", 13))
    c.bind("<Button-1>", lambda e: comando())
    return c


def open_win_table(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Tabla (Treeview)")
    win.geometry("1160x660")
    win.configure(bg=FONDO)

    izq = tk.Frame(win, bg=FONDO)
    izq.pack(side="left", fill="both", expand=True, padx=(28, 0), pady=(50, 10))
    der = tk.Frame(win, bg=FONDO)
    der.pack(side="right", fill="y", padx=20, pady=(60, 20))

    registros = []
    ruta = Path(__file__).resolve().parents[2] / "data" / "sample.csv"
    if not ruta.exists():
        messagebox.showwarning("Aviso", f"No se encontró {ruta}. Crea el archivo de ejemplo.")
        win.destroy()
        return

    with open(ruta, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            registros.append((row["nombre"], row["valor1"], row["valor2"]))

    def estado_de(i):
        return ["completado", "proceso", "tardio"][i % 3]

    def dibujar():
        for w in izq.winfo_children():
            w.destroy()
        for i, (hora, med, dosis) in enumerate(registros):
            tarjeta(izq, estado_de(i), hora, med, dosis).pack(pady=6, anchor="w")

    def agregar():
        med = simpledialog.askstring("Agregar", "Medicina:", parent=win)
        if not med:
            return
        hora = simpledialog.askstring("Agregar", "Hora de toma:", parent=win) or ""
        dosis = simpledialog.askstring("Agregar", "Dosis:", parent=win) or ""
        registros.append((hora, med, dosis))
        dibujar()

    boton_redondo(der, "+ Agregar Medicamento", AZUL, agregar, 320, 66).pack(anchor="n")
    boton_redondo(der, "Salir", ROJO_SALIR, win.destroy, 320, 66, fg="#333333").pack(side="bottom")

    dibujar()