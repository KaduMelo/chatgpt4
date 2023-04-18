# Importar os pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Criar a variável driver
driver = webdriver.Chrome()

# Acessar a página
driver.get('https://www.amazon.com/dp/1789346347/ref=cm_sw_r_as_gl_api_gl_i_HFYB8PHAX05B8ERE4TC6?linkCode=ml1&tag=meucamdesan-20')

# Aguardar 5 segundos
sleep(5)

# Localizar o elemento
element = driver.find_element(By.ID, 'price')

# Obter o texto do elemento
price = element.text

# Converter o texto em float
price = float(price.replace('$', ''))
print(price)
# Verifique se o preço é menor que 40
if price < 40:
    print("Comprar o livro")
else:
    print("O preço do livro é igual a " + str(price))

# Feche o navegador
driver.quit()