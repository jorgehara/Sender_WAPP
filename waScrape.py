from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

# Ruta al ejecutable de ChromeDriver
chrome_driver_path = r'C:\Users\Usuario\Documents\chromedriver_win32\chrome.exe'

# Configura Selenium para usar ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Abre una URL en Chrome
URL = "https://web.whatsapp.com/"
driver.get(URL)

# Espera hasta que aparezca el código QR (puede requerir ajustes)
wait = WebDriverWait(driver, 30)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//canvas[@aria-label="Código QR de WhatsApp"]')))

# Una vez que el código QR ha sido escaneado y la sesión iniciada, puedes continuar con el análisis de la página
# Puedes agregar más código aquí para interactuar con la página como lo necesites

# Obtén el contenido de la página una vez que los elementos estén presentes
page_content = driver.page_source

# Continúa con el análisis de la página como lo hiciste antes
soup = bs(page_content, "html.parser")
contacts_containers = soup.find_all("div", class_="_11JPr")

# Imprime los contenedores de contactos
for contact in contacts_containers:
    print(contact)

# Cierra el navegador al finalizar
# driver.quit()
