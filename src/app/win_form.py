import tkinter as tk
from tkinter import filedialog, messagebox

def open_win_form(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Formulario")
    win.geometry("1024x576")
    win.configure(bg="#C9DCF0")

    tk.Label(
        win,
        text="FORMULARIO",
        font=("Arial Black", 32, "bold"),
        bg="#C9DCF0",
        fg="#2B2B2B"
    ).pack(pady=(15, 10))

    frm_campos = tk.Frame(win, bg="#C9DCF0")
    frm_campos.pack(fill="x", padx=35)

    def crear_fila(texto_etiqueta, ancho_entry):
        fila = tk.Frame(frm_campos, bg="#C9DCF0")
        fila.pack(fill="x", pady=6)

        tk.Label(
            fila,
            text=texto_etiqueta,
            font=("Segoe UI", 24, "bold"),
            bg="#C9DCF0",
            fg="#2B2B2B"
        ).pack(side="left", padx=(0, 15))

        borde = tk.Frame(fila, bg="#000000", padx=4, pady=4)
        borde.pack(side="left")

        entrada = tk.Entry(
            borde,
            font=("Segoe UI", 18),
            bg="#E5E5E5",
            fg="#111111",
            relief="flat",
            width=ancho_entry
        )
        entrada.pack(ipady=3, padx=4)
        return entrada

    ent_nombre = crear_fila("Nombre:", 34)
    ent_edad = crear_fila("Edad:", 36)
    ent_contacto = crear_fila("Contacto de emergencia:", 20)
    ent_telefono = crear_fila("Telefono del contacto:", 22)
    ent_detalles = crear_fila("Detalles:", 34)

    def validar_y_guardar():
        nombre = ent_nombre.get().strip()
        edad_txt = ent_edad.get().strip()
        contacto = ent_contacto.get().strip()
        telefono = ent_telefono.get().strip()
        detalles = ent_detalles.get().strip()

        if not nombre:
            messagebox.showerror("Error", "El nombre es requerido.")
            return
        if not edad_txt.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Texto", "*.txt")]
        )
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(f"Nombre: {nombre}\n")
                f.write(f"Edad: {edad_txt}\n")
                f.write(f"Contacto de emergencia: {contacto}\n")
                f.write(f"Teléfono del contacto: {telefono}\n")
                f.write(f"Detalles: {detalles}\n")
            messagebox.showinfo("OK", "Datos guardados.")

    frm_botones = tk.Frame(win, bg="#C9DCF0")
    frm_botones.pack(side="bottom", fill="x", padx=150, pady=22)

    tk.Button(
        frm_botones,
        text="✔",
        font=("Segoe UI", 32, "bold"),
        bg="#76E065",
        fg="#FFFFFF",
        activebackground="#5EC74E",
        activeforeground="#FFFFFF",
        relief="flat",
        width=6,
        cursor="hand2",
        command=validar_y_guardar
    ).pack(side="left")

    tk.Button(
        frm_botones,
        text="✖",
        font=("Segoe UI", 32, "bold"),
        bg="#EA3323",
        fg="#FFFFFF",
        activebackground="#C92214",
        activeforeground="#FFFFFF",
        relief="flat",
        width=6,
        cursor="hand2",
        command=win.destroy
    ).pack(side="right")