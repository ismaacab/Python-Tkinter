import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import tkinter as tk
from tkinter import messagebox
import winsound

# ---------------------------------------------------------
# 1. CONFIGURACIÓN DE CUENTAS REMITENTES (Las que envían)
# IMPORTANTE: Reemplaza los textos por las contraseñas reales.
# ---------------------------------------------------------
CUENTAS_REMITENTES = {
    "ismaafuentes.26@gmail.com": "",
    "mario.ismael.canevari@gmail.com": "CONTRASENA_AQUI_2",
    "fjcoronati@gmail.com": "CONTRASENA_AQUI_3",
    "cuenta4@gmail.com": "CONTRASENA_4"
}

def sonido_tecla(event):
    try:
        winsound.MessageBeep(-1)
    except:
        pass

def sonido_boton():
    try:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
    except:
        pass

def sonido_exito():
    try:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
    except:
        pass

def enviar_correo():
    sonido_boton()

    remitente = variable_remitente.get()
    password = CUENTAS_REMITENTES.get(remitente, "")

    destinatario = variable_destinatario.get()
    if destinatario == "Otro (Escribir manual)":
        destinatario = entry_manual.get()

    asunto = entry_asunto.get()
    mensaje = text_mensaje.get("1.0", tk.END).strip()

    if not destinatario or not asunto or not mensaje or not password:
        messagebox.showwarning("Advertencia", "Faltan campos o la cuenta seleccionada no tiene contraseña configurada.")
        return

    try:
        # Permite usar tildes y la letra Ñ sin errores
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = Header(asunto, 'utf-8')
        msg.attach(MIMEText(mensaje, 'plain', 'utf-8'))

        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario.split(","), msg.as_string())
        servidor.quit()

        sonido_exito()
        messagebox.showinfo("Éxito", "¡Correo enviado con éxito!")
        
        entry_asunto.delete(0, tk.END)
        text_mensaje.delete("1.0", tk.END)
        entry_manual.delete(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar:\n{e}")

# ---------------------------------------------------------
# INTERFAZ GRÁFICA
# ---------------------------------------------------------
root = tk.Tk()
root.title("Envío de Correos")
root.geometry("380x580") 

root.bind("<Key>", sonido_tecla)

COLOR_FONDO = "#2C3E50"
COLOR_TEXTO = "#ECF0F1"
root.config(bg=COLOR_FONDO)

tk.Label(root, text="Enviado desde (Remitente):", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 9, "bold")).pack(anchor="w", padx=20, pady=(10,0))

opciones_remitentes = list(CUENTAS_REMITENTES.keys())
variable_remitente = tk.StringVar(root)
variable_remitente.set(opciones_remitentes[0])

menu_remitente = tk.OptionMenu(root, variable_remitente, *opciones_remitentes)
menu_remitente.config(width=35, font=("Arial", 8), bg="#34495E", fg="white")
menu_remitente.pack(padx=20, pady=2)

tk.Label(root, text="Para (Destinatario):", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 9, "bold")).pack(anchor="w", padx=20, pady=(10,0))

opciones_destinatarios = [
    "ismaafuentes.26@gmail.com",
    "lafortaleza246@gmail.com",
    "fjcoronati@gmail.com", 
    "mfedullo@gmail.com",
    "mario.ismael.canevari.09@gmail.com",
    "Otro (Escribir manual)"
]

variable_destinatario = tk.StringVar(root)
variable_destinatario.set(opciones_destinatarios[0]) 

menu_destinatario = tk.OptionMenu(root, variable_destinatario, *opciones_destinatarios)
menu_destinatario.config(width=35, font=("Arial", 8), bg="#34495E", fg="white")
menu_destinatario.pack(padx=20, pady=2)

tk.Label(root, text="Si elegiste 'Otro' (puedes separar varios con coma):", bg=COLOR_FONDO, fg="#BDC3C7", font=("Arial", 8)).pack(anchor="w", padx=20)
entry_manual = tk.Entry(root, width=42, font=("Arial", 9), bg="#ecf0f1")
entry_manual.pack(padx=20, pady=2)

tk.Label(root, text="Asunto:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 9, "bold")).pack(anchor="w", padx=20, pady=(10,0))
entry_asunto = tk.Entry(root, width=42, font=("Arial", 9), bg="#ecf0f1")
entry_asunto.pack(padx=20, pady=2)

tk.Label(root, text="Mensaje:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 9, "bold")).pack(anchor="w", padx=20, pady=(10,0))
text_mensaje = tk.Text(root, width=42, height=6, font=("Arial", 9), bg="#ecf0f1")
text_mensaje.pack(padx=20, pady=2)

btn_enviar = tk.Button(root, text="Enviar Correo", command=enviar_correo, 
                       bg="#27AE60", fg="white", font=("Arial", 10, "bold"), 
                       activebackground="#2ECC71", activeforeground="white",
                       relief="raised", borderwidth=2)
btn_enviar.pack(pady=15)

root.mainloop()
