from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from time import sleep
    
class Google:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'https://curso-python-selenium.netlify.app/aula_03.html#'
        

    def navigate(self):
        self.driver.get(self.url)

  

gg = Firefox()
g = Google(gg)
pagina =g.navigate()
sleep(2)

for click in range(10):
    p = gg.find_elements(By.TAG_NAME,'p')
    a = gg.find_element(By.ID,'ancora').click()
    pprint(f'valor de p ={p[-1].text} e valor do click={click}')
    pprint(f'Os valore são Iguais: {p[-1].text == str(click)}')


