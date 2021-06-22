from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import Konstante
import Lokatori
import time


driver=webdriver.Chrome()
driver.get(f"{Konstante.BASE_URL}")
driver.maximize_window()
driver.implicitly_wait(8)

dugmeprijavitese=driver.find_element_by_css_selector(Lokatori.header_button_login_page_css_selector)
dugmeprijavitese.click()

imejlpolje=driver.find_element_by_css_selector(Lokatori.login_page_page_email_css_selector)
imejlpolje.send_keys('sapna2661@gmail.com')

sifrapolje=driver.find_element_by_css_selector(Lokatori.login_page_password_css_selector)
sifrapolje.send_keys('Sap937rattu')


dugmelogujtese=driver.find_element_by_css_selector(Lokatori.login_page_button_css_selector)
dugmelogujtese.click()

time.sleep(1)

dugmeizlogujtese = driver.find_element_by_css_selector(Lokatori.logout_page_button_css_selector)
dugmeizlogujtese.click()

time.sleep(2)
driver.quit()




