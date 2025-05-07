import pywhatkit as pwk
import pyautogui
import time
import json
import openpyxl

# Ruta de la imagen a adjuntar
imagen = r"C:\Users\Usuario\Desktop\wasapp-contacts\imagen1.png"

print("Inicio del proceso...")

# Leer números desde el archivo Excel al inicio y almacenarlos en una lista
def leer_numeros_desde_excel(nombre_archivo):
    try:
        numeros = []
        wb = openpyxl.load_workbook(nombre_archivo)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True):  # Lee solo la columna A
            numero = str(row[0])
            if numero.strip():  # Verifica si la celda no está vacía
                numeros.append(numero)
        return numeros
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en el directorio actual.")
        return []

# Mensaje a enviar
mensaje_a_enviar = "¡Hola, soy Glenda Seifert! 👋 Este domingo 17, acompáñanos con tu voto. Con Leandro Zdero Gobernador, vamos a Seguir Cambiando la realidad de Pampa del Infierno y del Chaco. 🗳️💪 Juntos por el Cambio. Lista 653. 🇦🇷 #Vota653"

# Nombre del archivo Excel que contiene los números
nombre_archivo_excel = "Prueba2.xlsx"

# Obtiene la lista de números desde el archivo Excel al inicio
numeros_a_enviar = leer_numeros_desde_excel(nombre_archivo_excel)

# Listas para almacenar números enviados y no enviados
numeros_enviados1 = []
numeros_no_enviados1 = []

# Función para enviar el mensaje con imagen
def enviar_mensaje_con_imagen(numero, mensaje, imagen):
    try:
        # Agrega el "+" como prefijo al número de contacto
        numero = "+" + numero

        # Abre WhatsApp Web (asegúrate de tenerlo abierto)
        # pwk.open_web()
        time.sleep(5)  # Espera 5 segundos para que WhatsApp Web se cargue completamente

        # Envía el mensaje con la imagen adjunta
        pwk.sendwhats_image(numero, imagen, mensaje)
        time.sleep(5)  # Espera 5 segundos después de enviar el mensaje

        # Agrega el número a la lista de números enviados si el mensaje se envió correctamente
        numeros_enviados1.append(numero)
        print(f"Mensaje a {numero} enviado correctamente.")
    except Exception as e:
        print(f"No se pudo enviar el mensaje a {numero}: {str(e)}")
        # Agrega el número a la lista de números no enviados si ocurrió una excepción
        numeros_no_enviados1.append(numero)
        print(f"Mensaje a {numero} no enviado.")

# Envía el mensaje a cada número
for numero in numeros_a_enviar:
    enviar_mensaje_con_imagen(numero, mensaje_a_enviar, imagen)

# Guardar los números enviados y no enviados en archivos JSON
with open('numeros_enviados.json', 'w') as file:
    json.dump(numeros_enviados1, file)

with open('numeros_no_enviados.json', 'w') as file:
    json.dump(numeros_no_enviados1, file)

# Muestra el mensaje de finalización del proceso
print("Finalización del proceso.")
