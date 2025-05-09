#en excel para filtra los numeros enviados de los que faltan
#=SI(CONTAR.SI($B$1:$B$862;A2)=0;"Pendiente";"Ya enviado")
# Script para filtrar números de teléfono únicos de un archivo de texto
# O la forma más fácil:
#Copia todos los números originales en la Columna A
#Copia todos los números enviados en la Columna B
#En la Columna C usa esta fórmula simple:

import re

try:
    # Lee el archivo con codificación UTF-8
    with open('PyWhatKit_DB.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # Encuentra todos los números de teléfono que comienzan con +549
    phone_numbers = re.findall(r'\+549\d+', content)

    # Elimina duplicados convirtiendo a set y vuelve a lista
    unique_numbers = list(set(phone_numbers))

    # Guarda los números únicos en un nuevo archivo
    with open('numeros_unicos.txt', 'w', encoding='utf-8') as file:
        for number in unique_numbers:
            file.write(number + '\n')

    print(f"Se encontraron {len(unique_numbers)} números únicos y se guardaron en 'numeros_unicos.txt'")

except UnicodeDecodeError:
    # Si UTF-8 falla, intenta con otra codificación
    with open('PyWhatKit_DB.txt', 'r', encoding='latin-1') as file:
        content = file.read()
        
    phone_numbers = re.findall(r'\+549\d+', content)
    unique_numbers = list(set(phone_numbers))
    
    with open('numeros_unicos.txt', 'w', encoding='utf-8') as file:
        for number in unique_numbers:
            file.write(number + '\n')
    
    print(f"Se encontraron {len(unique_numbers)} números únicos y se guardaron en 'numeros_unicos.txt'")

except Exception as e:
    print(f"Ocurrió un error: {str(e)}")