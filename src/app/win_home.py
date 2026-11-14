import tkinter as tk

if __package__:
    from .win_quien_soy import open_win_quien_soy
else:
    from win_quien_soy import open_win_quien_soy

def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Home / Bienvenida")
    win.geometry("1024x576")
    win.configure(bg="#C9DCF0")

    tk.Label(
        win, text="win_home", bg="#C9DCF0", fg="#2B2B2B", font=("Arial", 9)
    ).place(x=8, y=5)

    frm = tk.Frame(win, bg="#C9DCF0")
    frm.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frm,
        text="BUENAS TARDES, ANA MARÍA LÓPEZ",
        font=("Arial Black", 26, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B",
        padx=35,
        pady=12
    ).pack(pady=8)

    tk.Label(
        frm,
        text="Hoy es martes 12 de noviembre de 2026",
        font=("Segoe UI", 16, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B",
        padx=45,
        pady=8
    ).pack(pady=8)

    tk.Label(
        frm,
        text="Son las 7:51 de la mañana",
        font=("Segoe UI", 15, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B",
        padx=35,
        pady=8
    ).pack(pady=8)

    tk.Button(
        frm,
        text="¿Quién soy?",
        font=("Segoe UI", 16, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B",
        activebackground="#D4D4D4",
        relief="flat",
        cursor="hand2",
        padx=30,
        pady=6,
        command=lambda: open_win_quien_soy(parent)
    ).pack(pady=10)

    tk.Button(
        frm,
        text="Cerrar",
        font=("Segoe UI", 16),
        bg="#E5E5E5",
        fg="#2B2B2B",
        activebackground="#D4D4D4",
        relief="flat",
        cursor="hand2",
        padx=30,
        pady=6,
        command=win.destroy
    ).pack(pady=8)