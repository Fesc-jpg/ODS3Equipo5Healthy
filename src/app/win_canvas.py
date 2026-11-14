import tkinter as tk
from datetime import datetime

FONDO = "#C2DBFF"
GRIS_OSCURO = "#64748F"
AZUL_NOCHE = "#1F2A44"
AZUL_SUAVE = "#7B96C8"
CAJA = "#E8E8E8"
TEXTO = "#2B2B2B"
ROJO = "#FF3B3B"

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def rect_redondeado(c, x1, y1, x2, y2, r, **kw):
    pts = [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2,
           x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


def open_win_canvas(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Reloj")
    win.geometry("1160x650")
    win.configure(bg=FONDO)
    win.resizable(False, False)

    c = tk.Canvas(win, width=1160, height=650, bg=FONDO, highlightthickness=0)
    c.pack()

    c.create_text(60, 75, text="RELOJ", anchor="w", font=("Impact", 54), fill=TEXTO)

    rect_redondeado(c, 40, 170, 480, 470, 40, fill=GRIS_OSCURO, outline=GRIS_OSCURO)
    rect_redondeado(c, 65, 195, 455, 445, 28, fill="white", outline="white")
    txt_hora = c.create_text(260, 305, text="", font=("Consolas", 56, "bold"), fill=AZUL_NOCHE)
    txt_ampm = c.create_text(260, 390, text="", font=("Verdana", 22, "bold"), fill=AZUL_SUAVE)

    rect_redondeado(c, 500, 155, 1080, 470, 22, fill=CAJA, outline="black", width=6)
    txt_info = c.create_text(790, 312, text="", width=540, justify="center",
                             font=("Verdana", 28, "bold"), fill=TEXTO)

    rect_redondeado(c, 755, 500, 985, 638, 30, fill=ROJO, outline=ROJO, tags="salir")
    c.create_line(847, 547, 893, 593, fill="white", width=14, capstyle="round", tags="salir")
    c.create_line(893, 547, 847, 593, fill="white", width=14, capstyle="round", tags="salir")
    c.tag_bind("salir", "<Button-1>", lambda e: win.destroy())

    def actualizar():
        if not win.winfo_exists():
            return
        t = datetime.now()
        h12 = t.hour % 12 or 12
        periodo = "mañana" if t.hour < 12 else "tarde" if t.hour < 19 else "noche"
        c.itemconfig(txt_hora, text=f"{h12:02d}:{t.minute:02d}:{t.second:02d}")
        c.itemconfig(txt_ampm, text="a. m." if t.hour < 12 else "p. m.")
        c.itemconfig(txt_info, text=f"Son {h12}:{t.minute:02d} de la {periodo}\n"
                                    f"{DIAS[t.weekday()]} {t.day} de {MESES[t.month - 1]} de {t.year}")
        win.after(1000, actualizar)

    actualizar()