from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from credenciais import usuario, senha
import scrapy
import time

chromepatah = "C:/chromedriver/chromedriver.exe"

# Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:	https://github.com/mozilla/geckodriver/releases
# Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
# Variaveis de sistema no cmd echo %path%
# https://sites.google.com/a/chromium.org/chromedriver/


driver = webdriver.Chrome(executable_path=chromepatah)
driver.get("https://e-decision.wca-ec.com.br/login.aspx")

# # Pela tag
# elem = driver.find_element_by_name("FormLayout$txtLogin")
# elem.send_keys(usuario)
# elem = driver.find_element_by_name("FormLayout$txtPassword")
# elem.send_keys(senha)

# Pelo path html
elem = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td/input")
elem.send_keys(usuario)
elem = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[1]/td[2]/div/table/tbody/tr[3]/td/div/table/tbody/tr/td[1]/table/tbody/tr/td/input")
elem.send_keys(senha)

elem.send_keys(Keys.RETURN)

time.sleep(1)
driver.close()


# # Encontrando elemento pelo CSS + comandos
# driver.find_element_by_css_selector('button[type=submit]').click()
# assert "Python" in driver.title
#elem = driver.find_element_by_name("q").send_keys("pyplan" + Keys.RETURN)
# assert "No results found." not in driver.page_source
# elem.clear()