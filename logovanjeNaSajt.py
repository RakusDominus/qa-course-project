from selenium import webdriver
import time
import Konstante
import Lokatori
import MockedData

def TestLogin(email, password):
    driver = webdriver.Chrome()
    driver.get(f"{Konstante.BASE_URL}")
    driver.maximize_window()
    driver.implicitly_wait(8)

    dugmeprijavitese=driver.find_element_by_css_selector(Lokatori.header_button_login_page_css_selector)
    dugmeprijavitese.click()

    emailField = driver.find_element_by_css_selector(Lokatori.login_page_page_email_css_selector)
    passwordField = driver.find_element_by_css_selector(Lokatori.login_page_password_css_selector)

    logInButton = driver.find_element_by_css_selector(Lokatori.login_page_button_css_selector)

    emailField.send_keys(email)
    passwordField.send_keys(password)

    logInButton.click()

    #dugmenovimeme=driver.find_element_by_css_selector(Lokatori.mem_button_css_selektor)
    #if dugmenovimeme is not None:
        #dugmenovimeme.click()
    
    time.sleep(2)
    driver.quit()

for podatak in MockedData.TEST_DATA:
    TestLogin(podatak["email"],podatak["password"])



