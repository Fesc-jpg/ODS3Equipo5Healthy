import tkinter as tk

def open_win_quien_soy(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("¿Quién soy?")
    win.geometry("1024x576")
    win.configure(bg="#C9DCF0")

    tk.Label(
        win,
        text="¿QUIÉN SOY?",
        font=("Arial Black", 24, "bold"),
        bg="#C9DCF0",
        fg="#2B2B2B"
    ).place(x=25, y=20)

    tarjeta = tk.Frame(win, bg="#E5E5E5", padx=55, pady=35)
    tarjeta.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        tarjeta,
        text="Tu eres Ana María López",
        font=("Segoe UI", 22, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B"
    ).pack(pady=(5, 10))

    tk.Label(
        tarjeta,
        text="Tienes 82 años",
        font=("Segoe UI", 22, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B"
    ).pack(pady=(0, 65))

    tk.Label(
        tarjeta,
        text="Tu familiar es Luis (hijo)",
        font=("Segoe UI", 22, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B"
    ).pack(pady=(0, 15))

    tk.Label(
        tarjeta,
        text="Su teléfono es: 477 123 4567",
        font=("Segoe UI", 22, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B"
    ).pack(pady=(0, 20))

    tk.Label(
        tarjeta,
        text="Estás a salvo.",
        font=("Segoe UI", 22, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B"
    ).pack(pady=(0, 35))

    borde_btn = tk.Frame(tarjeta, bg="#E094A8", padx=3, pady=3)
    borde_btn.pack()

    tk.Button(
        borde_btn,
        text="Entendido",
        font=("Segoe UI", 20, "bold"),
        bg="#E5E5E5",
        fg="#2B2B2B",
        activebackground="#D4D4D4",
        relief="flat",
        padx=30,
        pady=2,
        cursor="hand2",
        command=win.destroy
    ).pack()