# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

# Configuracion del correo electronico
EMAIL_REMITENTE = "ismaafuentes.26@gmail.com"
PASSWORD_REMITENTE = "thqh ggyg mnfr nlvy"

def enviar_correo():
    destinatario = variable_destino.get()
    
    if destinatario == "Otro (Escribir manual)":
        destinatario = entry_manual.get().strip()
    
    asunto = entry_asunto.get().strip()
    mensaje_cuerpo = text_mensaje.get("1.0", tk.END).strip()

    if not destinatario or not asunto or not mensaje_cuerpo:
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_REMITENTE, PASSWORD_REMITENTE)

        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMITENTE
        msg['To'] = destinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje_cuerpo, 'plain'))

        servidor.sendmail(EMAIL_REMITENTE, destinatario, msg.as_string())
        servidor.quit()

        messagebox.showinfo("Éxito", f"¡Correo enviado a {destinatario}!")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo:\n{e}")

root = tk.Tk()
root.title("TP Laboratorio 2 - Interfaz Gráfica")
root.geometry("450x650")
root.config(bg="#f0f0f0")

# Inserción de imagen personalizada
# Asegúrate de tener una imagen llamada 'logo.png' en la misma carpeta
try:
    imagen_logo = tk.PhotoImage(file="logo.png")
    label_img = tk.Label(root, image=imagen_logo, bg="#f0f0f0")
    label_img.pack(pady=10)
except Exception:
    label_img = tk.Label(root, text="[Coloca una imagen llamada 'logo.png']", bg="#f0f0f0", fg="red")
    label_img.pack(pady=10)

tk.Label(root, text="Asunto:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(anchor="w", padx=30)
entry_asunto = tk.Entry(root, width=40, font=("Arial", 10))
entry_asunto.pack(pady=5, padx=30)

# Menú desplegable OptionMenu con los correos indicados
tk.Label(root, text="Seleccionar Destinatario:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(anchor="w", padx=30)

opciones_destinatarios = [
    "ismaafuentes.26@gmail.com",
    "lafortaleza246@gmail.com",
    "fjcoronati@gmail.com", # Docente (Profesor del TP)
    "segundo_docente_prog@gmail.com", # Docente 2 de programación
    "tercer_docente_prog@gmail.com", # Docente 3 de programación
    "Otro (Escribir manual)"
]

variable_destino = tk.StringVar(root)
variable_destino.set(opciones_destinatarios[0])

menu_desplegable = tk.OptionMenu(root, variable_destino, *opciones_destinatarios)
menu_desplegable.config(width=35, font=("Arial", 9))
menu_desplegable.pack(pady=5, padx=30)

tk.Label(root, text="Si elegiste 'Otro', escribe el correo aquí:", bg="#f0f0f0", font=("Arial", 9)).pack(anchor="w", padx=30)
entry_manual = tk.Entry(root, width=40, font=("Arial", 10))
entry_manual.pack(pady=5, padx=30)

tk.Label(root, text="Mensaje:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(anchor="w", padx=30)
text_mensaje = tk.Text(root, width=38, height=8, font=("Arial", 10))
text_mensaje.pack(pady=5, padx=30)

btn_enviar = tk.Button(root, text="Enviar Correo Electrónico", command=enviar_correo, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_enviar.pack(pady=15)

root.mainloop()