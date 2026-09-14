# 📧 Aplicación de Envío de Correos (Tkinter + SMTP)

Aplicación de escritorio en Python para gestionar y enviar correos electrónicos a través del servidor SMTP de Gmail, equipada con una interfaz gráfica interactiva, sonidos dinámicos y soporte para múltiples cuentas.

---

## 🚀 Novedades y Últimas Actualizaciones

* **Soporte UTF-8 Completo:** Solución definitiva al error de codificación ASCII. Ahora es posible incluir letras **Ñ**, tildes, signos de apertura (`¿`, `¡`) y caracteres especiales tanto en el asunto como en el cuerpo del mensaje.
* **Efectos de Sonido Interactivos:** 
  * Feedback sonoro en tiempo real tipo máquina de escribir al presionar cualquier tecla (`winsound`).
  * Sonidos diferenciados para clics en botones y confirmación de envío exitoso o errores.
* **Gestión Multi-Remitente:** Menú desplegable para seleccionar desde qué cuenta emites el correo, configurado mediante un diccionario estructurado de credenciales.
* **Envío Múltiple a Destinatarios:** Capacidad para enviar un mismo correo a varias direcciones simultáneamente escribiéndolas separadas por comas en el campo de entrada manual.
* **Diseño Compacto y Tema Oscuro:** Interfaz optimizada (`380x580 px`) en tono azul oscuro (`#2C3E50`) con contraste claro para reducir la fatiga visual.

---

## 🛠️ Requisitos Previos

1. **Python 3.x** instalado.
2. Sistema operativo **Windows** (requerido para los efectos de sonido de `winsound`).
3. **Contraseñas de aplicación de Google:** Es necesario activar la verificación en dos pasos en cada cuenta de Gmail remitente y generar una contraseña de aplicación de 16 caracteres.

---

## ⚙️ Configuración e Instalación

1. Clona o descarga este repositorio.
2. Abre el archivo principal en tu editor de código.
3. Actualiza el diccionario `CUENTAS_REMITENTES` con tus correos y contraseñas de aplicación:

```python
CUENTAS_REMITENTES = {
    "tu_correo@gmail.com": "tu_contraseña_de_aplicacion",
    "otro_correo@gmail.com": "segunda_contraseña_de_aplicacion"
}
