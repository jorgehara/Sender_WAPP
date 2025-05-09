#pip freeze > requirements.txt
#pip install -r requirements.txt

#crear un entorno virtual
#python -m venv env
#activar el entorno virtual
#env\Scripts\activate
# -*- coding: utf-8 -*-


import pywhatkit as pwk
import pyautogui
import time
import pandas as pd
import os

# Ruta de la imagen a adjuntar
imagen = r"C:\Users\jorge\Sender_WAPP\img\voto11MayoPampa.jpeg"

print("Inicio del proceso...")

# Verificar si la imagen existe
if not os.path.exists(imagen):
    print(f"Error: La imagen '{imagen}' no existe en la ruta especificada")
    exit()

# Leer números desde el archivo Excel al inicio y almacenarlos en una lista
def leer_numeros_desde_excel(nombre_archivo):
    try:
        # Asegurarse de que la ruta sea absoluta
        ruta_absoluta = os.path.abspath(nombre_archivo)
        print(f"Leyendo números desde: {ruta_absoluta}")
        
        # Leer el Excel específicamente la columna A
        df = pd.read_excel(ruta_absoluta, usecols=[0])  # Solo lee la columna A
        
        # Debugging: Muestra el contenido exacto de cada celda
        for idx, valor in df.iloc[:, 0].items():
            print(f"Fila {idx+1}: '{valor}' - Tipo: {type(valor)}")
        
        # Convertir todos los números a string y limpiarlos
        numeros = []
        for idx, valor in df.iloc[:, 0].items():
            if pd.notna(valor):  # Verifica que no sea un valor nulo
                num = str(valor).strip()
                if num.isdigit():  # Verifica que sean solo números
                    numeros.append(num)
        
        # Muestra información detallada
        print(f"Se encontraron {len(numeros)} números en el archivo Excel")
        print("Números encontrados:")
        for i, num in enumerate(numeros, 1):
            print(f"  {i}. {num}")
        
        return numeros
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en el directorio actual.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo Excel: {str(e)}")
        return []

# Mensaje a enviar
mensaje_a_enviar = "🗳️ *¡Chaco Puede! Lista 653 🇦🇷 #Vota653!*\n" \
                   "👋🏼 Querido Vecino\n" \
                   "Este *domingo 11* contamos con vos 🙌🏼\n" \
                   "Acompañanos con la *Lista 653 para seguir ordenando y haciendo crecer a Pampa del Infierno y el Chaco* 🌱\n" \
                   "💖 Con cariño *Glenda Seifert*"

# Nombre del archivo Excel que 
#  los números
nombre_archivo_excel = r"contacts\Prueba2.xlsx"

# Obtiene la lista de números desde el archivo Excel al inicio
numeros_a_enviar = leer_numeros_desde_excel(nombre_archivo_excel)

# Verificación de números antes de enviar
print(f"Total de números a procesar: {len(numeros_a_enviar)}")
print("Números que se procesarán:")
for i, num in enumerate(numeros_a_enviar, 1):
    print(f"{i}. {num}")

# Confirmar envío
input("Presiona Enter para comenzar el envío de mensajes...")

# Función para enviar el mensaje al presionar Enter
def enviar_mensaje_con_enter(numero, mensaje, index):
    try:
        # Asegurarse de que el número tenga el formato correcto
        numero = str(numero).strip()
        if not numero.startswith('+'):
            numero = '+' + numero
        
        print(f"Intentando enviar mensaje a {numero}")
        
        # Adjunta la imagen y escribe el mensaje
        pwk.sendwhats_image(numero, imagen, mensaje, tab_close=False, wait_time=20)  # Aumentamos el wait_time
        
        # Espera más tiempo para asegurar que la imagen se cargó completamente
        time.sleep(8)  # Aumentamos el tiempo de espera después de cargar la imagen
        
        # Múltiples clics para asegurar el foco
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        
        # Aseguramos que el mensaje se envíe
        pyautogui.hotkey('ctrl', 'v')  # Intentamos pegar explícitamente
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)  # Aumentamos el tiempo de espera entre mensajes

        print(f"Mensaje {index + 1}/{len(numeros_a_enviar)} enviado a {numero} - Estado: Enviado")
        
    except Exception as e:
        print(f"Error enviando mensaje a {numero}: {str(e)}")

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
