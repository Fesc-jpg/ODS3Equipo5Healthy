import tkinter as tk
from tkinter import messagebox

if __package__:
    from .win_home import open_win_home
    from .win_form import open_win_form
    from .win_list import open_win_list
    from .win_table import open_win_table
    from .win_canvas import open_win_canvas
else:
    from win_home import open_win_home
    from win_form import open_win_form
    from win_list import open_win_list
    from win_table import open_win_table
    from win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Menú Principal - Memoria")
    root.geometry("1024x576")
    root.configure(bg="#C9DCF0")

    header_frame = tk.Frame(root, bg="#C9DCF0")
    header_frame.place(x=25, y=15)

    fila_titulo = tk.Frame(header_frame, bg="#C9DCF0")
    fila_titulo.pack(anchor="w")

    tk.Label(
        fila_titulo,
        text="MENU PRINCIPAL",
        font=("Arial Black", 26, "bold"),
        bg="#C9DCF0",
        fg="#2B2B2B"
    ).pack(side="left")

    tk.Label(
        header_frame,
        text="Apoyo a las personas con alzheimer",
        font=("Segoe UI", 18),
        bg="#C9DCF0",
        fg="#2B2B2B"
    ).pack(anchor="w", padx=(65, 0))

    menu_frame = tk.Frame(root, bg="#C9DCF0")
    menu_frame.place(relx=0.5, rely=0.53, anchor="center")

    opciones = [
        ("1) Home", lambda: open_win_home(root)),
        ("2) Formulario", lambda: open_win_form(root)),
        ("3) Recordatorios 💡", lambda: open_win_list(root)),
        ("4) Medicinas 💊", lambda: open_win_table(root)),
        ("5) Reloj ⏰", lambda: open_win_canvas(root)),
    ]

    for texto, comando in opciones:
        borde = tk.Frame(menu_frame, bg="#000000", padx=4, pady=4)
        borde.pack(pady=6)

        tk.Button(
            borde,
            text=texto,
            font=("Segoe UI", 17),
            bg="#E5E5E5",
            fg="#111111",
            activebackground="#D4D4D4",
            relief="flat",
            width=36,
            pady=4,
            cursor="hand2",
            command=comando
        ).pack()

    bottom_frame = tk.Frame(root, bg="#C9DCF0")
    bottom_frame.pack(side="bottom", fill="x", padx=30, pady=22)

    borde_emergencia = tk.Frame(bottom_frame, bg="#000000", padx=4, pady=4)
    borde_emergencia.pack(side="left")

    tk.Button(
        borde_emergencia,
        text="EMERGENCIA",
        font=("Segoe UI", 18),
        bg="#EA3323",
        fg="#FFFFFF",
        activebackground="#C92214",
        activeforeground="#FFFFFF",
        relief="flat",
        width=32,
        pady=6,
        cursor="hand2",
        command=lambda: messagebox.showwarning("EMERGENCIA", "¡Llamando a contacto de emergencia!")
    ).pack()

    borde_salir = tk.Frame(bottom_frame, bg="#000000", padx=4, pady=4)
    borde_salir.pack(side="right")

    tk.Button(
        borde_salir,
        text="Salir",
        font=("Segoe UI", 18),
        bg="#E5E5E5",
        fg="#111111",
        activebackground="#D4D4D4",
        relief="flat",
        width=22,
        pady=6,
        cursor="hand2",
        command=root.destroy
    ).pack()

    root.mainloop()

if __name__ == "__main__":
    main()