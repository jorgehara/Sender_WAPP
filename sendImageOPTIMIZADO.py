import pywhatkit as pwk
import pyautogui
import time
import pandas as pd
import os

# Ruta de la imagen a adjuntar
imagen = r"C:\Users\JorgeHaraDevs\Desktop\wasapp-contacts-newversionPampa\img\voto11MayoPampa.jpeg"

print("Inicio del proceso...")

# Verificar si el archivo Excel existe
if not os.path.exists(nombre_archivo_excel):
    print(f"Error: El archivo '{nombre_archivo_excel}' no existe en la ruta especificada")
    exit()

# Leer números desde el archivo Excel al inicio y almacenarlos en una lista
def leer_numeros_desde_excel(nombre_archivo):
    try:
        df = pd.read_excel(nombre_archivo)
        return df.iloc[:, 0].astype(str).tolist()
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en el directorio actual.")
        return []

# Mensaje a enviar
mensaje_a_enviar = "¡🗳️💪 Chaco Puede. Lista 653. 🇦🇷 #Vota653!"

# Nombre del archivo Excel que 
#  los números
nombre_archivo_excel = r"contacts\Prueba2.xlsx"

# Obtiene la lista de números desde el archivo Excel al inicio
numeros_a_enviar = leer_numeros_desde_excel(nombre_archivo_excel)

# Función para enviar el mensaje al presionar Enter
def enviar_mensaje_con_enter(numero, mensaje, index):
    try:
        numero = "+" + str(numero)
        
        # Adjunta la imagen y escribe el mensaje
        pwk.sendwhats_image(numero, imagen, mensaje)

        # Espera 4 segundos antes de enviar el siguiente mensaje
        time.sleep(4)

        # Simula presionar la tecla Enter
        pyautogui.press('enter')

        print(f"Mensaje {index + 1}/{len(numeros_a_enviar)} enviado a {numero} - Estado: Enviado")
    except Exception as e:
        print(f"Mensaje {index + 1}/{len(numeros_a_enviar)} no se pudo enviar a {numero}: {str(e)}")

# Registra el tiempo de inicio del proceso
tiempo_inicio = time.time()

# Envía el mensaje a cada número
for index, numero in enumerate(numeros_a_enviar):
    enviar_mensaje_con_enter(numero, mensaje_a_enviar, index)

# Registra el tiempo de finalización del proceso
tiempo_final = time.time()

# Calcula el tiempo transcurrido
tiempo_transcurrido = tiempo_final - tiempo_inicio

# Muestra el mensaje de inicio y finalización del proceso, y el tiempo transcurrido
print("Finalización del proceso...")
print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
