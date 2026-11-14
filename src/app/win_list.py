import tkinter as tk
from tkinter import simpledialog, messagebox

MORADO = "#8B52FF"
AZUL_CLARO = "#4F6FFF"
AZUL_OSCURO = "#0047AB"
ROJO = "#FF2A2A"


def rect_redondeado(c, x1, y1, x2, y2, r, **kw):
    pts = [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2,
           x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


class BotonRedondo(tk.Canvas):
    def __init__(self, parent, texto, color, comando, ancho, alto=52, bg=None):
        super().__init__(parent, width=ancho, height=alto, bg=bg, highlightthickness=0)
        rect_redondeado(self, 2, 2, ancho-2, alto-2, 18, fill=color, outline=color)
        self.create_text(ancho/2, alto/2, text=texto, fill="white", font=("Verdana", 13, "bold"))
        self.bind("<Button-1>", lambda e: comando())


def open_win_list(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Lista (CRUD básico)")
    win.geometry("700x430")
    win.configure(bg="#EEEEEE")

    panel = tk.Frame(win, bg=MORADO)
    panel.pack(fill="both", expand=True, padx=4, pady=4)
    tk.Label(panel, text="Recordatorios", font=("Verdana", 20, "bold"), bg=MORADO, fg="white").pack(anchor="w", padx=12)

    cuerpo = tk.Frame(panel, bg=MORADO)
    cuerpo.pack(fill="both", expand=True, padx=8, pady=(0, 8))
    cuerpo.columnconfigure(0, weight=1, uniform="a")
    cuerpo.columnconfigure(1, weight=1, uniform="a")
    cuerpo.rowconfigure(1, weight=1)

    tk.Label(cuerpo, text="Actividades del día:", font=("Verdana", 12, "bold"),
             bg=AZUL_OSCURO, fg="white", pady=10).grid(row=0, column=0, sticky="ew")
    tk.Label(cuerpo, text="Escribe una nueva actividad:", font=("Verdana", 12, "bold"),
             bg=AZUL_OSCURO, fg="white", pady=10).grid(row=0, column=1, sticky="ew")

    izq = tk.Frame(cuerpo, bg=AZUL_CLARO)
    izq.grid(row=1, column=0, sticky="nsew")
    der = tk.Frame(cuerpo, bg=AZUL_OSCURO)
    der.grid(row=1, column=1, sticky="nsew")

    items = []
    estado = {"sel": None}

    def dibujar():
        for w in izq.winfo_children():
            w.destroy()
        for i, it in enumerate(items):
            c = tk.Canvas(izq, width=300, height=40, bg=AZUL_CLARO, highlightthickness=0)
            c.pack(pady=(14, 0), padx=14, anchor="w")
            borde = "white" if estado["sel"] == i else ROJO
            rect_redondeado(c, 2, 2, 298, 38, 14, fill=ROJO, outline=borde, width=2)
            c.create_rectangle(10, 8, 32, 32, fill="#C8D0DC", outline="")
            if it["hecho"]:
                c.create_text(21, 20, text="✔", fill="#0B5A0B", font=("Verdana", 18, "bold"))
            c.create_text(155, 20, text=it["texto"], fill="white", font=("Verdana", 13, "bold"))
            c.bind("<Button-1>", lambda e, k=i: seleccionar(k))

    def seleccionar(i):
        estado["sel"] = i
        dibujar()

    def agregar():
        v = simpledialog.askstring("Nueva actividad", "Escribe una nueva actividad:", parent=win)
        if v and v.strip():
            items.append({"texto": v.strip(), "hecho": False})
            dibujar()
        elif v is not None:
            messagebox.showwarning("Aviso", "Escribe un texto para agregar.")

    def realizada():
        i = estado["sel"]
        if i is not None and i < len(items):
            items[i]["hecho"] = not items[i]["hecho"]
            dibujar()

    def eliminar():
        i = estado["sel"]
        if i is not None and i < len(items):
            items.pop(i)
            estado["sel"] = None
            dibujar()

    def limpiar():
        items.clear()
        estado["sel"] = None
        dibujar()

    for txt, cmd in [("Agregar actividad", agregar), ("Actividad Realizada", realizada),
                     ("Eliminar lo seleccionado", eliminar), ("Limpiar todo", limpiar)]:
        BotonRedondo(der, txt, MORADO, cmd, 300, bg=AZUL_OSCURO).pack(pady=(14, 0), padx=14)

    BotonRedondo(der, "Salir", MORADO, win.destroy, 150, bg=AZUL_OSCURO).pack(side="bottom", anchor="e", padx=14, pady=14)

    items.extend([{"texto": "Desayunar", "hecho": True},
                  {"texto": "Cita con el doctor", "hecho": False},
                  {"texto": "Llamar a familiar", "hecho": False}])
    dibujar()