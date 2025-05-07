import pywhatkit as pwk
import pandas as pd
import pyautogui
import time
import json

# Función para enviar el mensaje al presionar Enter
def enviar_mensaje_con_enter(numero, nombre, mensaje):
    try:
        # Abre la ventana de WhatsApp Web (asegúrate de tener WhatsApp Web abierta antes de ejecutar el código)
        pwk.open_web()
        time.sleep(5)  # Espera 5 segundos para que WhatsApp Web se cargue completamente

        # Escribe el mensaje con el nombre
        mensaje_completo = f"Hola🙋‍♂️ {nombre}, {mensaje}"
        pwk.sendwhatmsg_instantly(numero, mensaje_completo)

        # Espera 6 segundos antes de enviar el siguiente mensaje
        time.sleep(6)

        # Simula presionar la tecla Enter
        pyautogui.press('enter')
        pyautogui.press('enter')

        # Agrega el número a la lista de números enviados si el mensaje se envió correctamente
        numeros_enviados.append(numero)
    except Exception as e:
        print(f"No se pudo enviar el mensaje a {nombre} ({numero}): {str(e)}")
        # Agrega el número a la lista de números no enviados si ocurrió una excepción
        numeros_no_enviados.append(numero)

# Leer números y nombres desde el archivo Excel
def leer_numeros_y_nombres_desde_excel():
    try:
        # Lee el archivo Excel sin encabezado
        df = pd.read_excel('Prueba1.xlsx', header=None)  # Reemplaza 'Prueba1.xlsx' con el nombre de tu archivo

        # Accede a la primera columna (sin nombre) que contiene los números
        numeros = df.iloc[:, 0]

        # Accede a la segunda columna (sin nombre) que contiene los nombres
        nombres = df.iloc[:, 1]

        # Convierte los números en la columna en cadenas de texto y agrega el código de país
        lista_de_numeros = ["+549" + str(numero) for numero in numeros]

        # Convierte los nombres en la columna en una lista de nombres
        lista_de_nombres = [str(nombre) for nombre in nombres]

        return lista_de_numeros, lista_de_nombres
    except FileNotFoundError:
        print("El archivo 'Prueba1.xlsx' no se encontró en el directorio actual.")
        return [], []

# Mensaje a enviar
mensaje_a_enviar = "📢 Este sábado, 9 de septiembre a las 10:00 a. m., tienes una cita en el Taller de Excel Fundamentos Básicos en la Cámara de Comercio de San Bernardo. Confirma tu asistencia y elige entre llevar tu laptop 🖥️, tu celular 📱 o simplemente papel y lápiz 📝 para aprovechar al máximo los consejos e información que se compartirán. ¡Te esperamos con entusiasmo! 😃✨"

# Obtiene la lista de números y nombres desde el archivo Excel
numeros_a_enviar, nombres_a_enviar = leer_numeros_y_nombres_desde_excel()

# Listas para almacenar números enviados y no enviados
numeros_enviados = []
numeros_no_enviados = []

# Envía el mensaje a cada número con el nombre correspondiente
for numero, nombre in zip(numeros_a_enviar, nombres_a_enviar):
    enviar_mensaje_con_enter(numero, nombre, mensaje_a_enviar)

# Guardar los números enviados en un archivo JSON
with open('numeros_enviados.json', 'w') as file:
    json.dump(numeros_enviados, file)

# Guardar los números no enviados en un archivo JSON
with open('numeros_no_enviados.json', 'w') as file:
    json.dump(numeros_no_enviados, file)
