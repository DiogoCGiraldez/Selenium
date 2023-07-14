from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
    
class Google:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'INPUT' #nome
        self.btn_search = "gNO89b" #classe
        self.login = "gb_1" # gb_2 gb_8d gb_8c\" #classe
        self.login_email = 'identifierId' #ID
        self.click_email_login = "VfPpkd-vQzf8d" #classe


    def navigate(self):
        self.driver.get(self.url)

    def search_teste(self, nome='None'):
        self.driver.find_element(
            By.TAG_NAME,self.search_bar).send_keys(nome)
        self.driver.find_element(
            By.CLASS_NAME,self.btn_search).submit()
    
    def login_teste(self):
        self.driver.find_element(By.CLASS_NAME,self.login).click()
    
    def logando(self, email='Nome'):
        self.driver.find_element(
            By.ID,self.login_email).send_keys(email + Keys.ENTER)
        #self.driver.find_element(
            #By.CLASS_NAME,self.click_email_login).submit()
    
#id botao recusar W0wltc
# vZr2rb
# \"btnK\" - nome botao search
# gNO89b - classe btn search


#C:\\Python310\\chromedriver-Windows
#ChromeDriverManager().install()
gg = Firefox()
g = Google(gg)
pagina =g.navigate()
#elemento = WebDriverWait(gg, 10).until(EC.presence_of_element_located((By.ID,\"W0wltc\")))

#cancel_button = (\"W0wltc\")
#cancel_button.click()
gg.find_element(By.ID,'W0wltc').click()
g.search_teste('Diogo')
#g.login_teste()
#print(ver)
#gg.find_element(By.TAG_NAME,'INPUT').send_keys('Diogo')