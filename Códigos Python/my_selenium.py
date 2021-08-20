from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:	https://github.com/mozilla/geckodriver/releases
# Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
# Variaveis de sistema no cmd echo %path%
# https://sites.google.com/a/chromium.org/chromedriver/


driver = webdriver.Chrome(executable_path=r'C:/chromedriver/chromedriver.exe')
driver.get("https://e-decision.wca-ec.com.br/login.aspx")
elem = driver.find_element_by_name("FormLayout$txtLogin")
elem.send_keys("alexsandro.ignacio@wca-ec.com.br")
elem = driver.find_element_by_name("FormLayout$txtPassword")
elem.send_keys("wca2021@")
elem = driver.find_element_by_xpath("FormLayout$txtPassword")
elem.send_keys(Keys.RETURN)

time.sleep(1)
driver.close()

# assert "Python" in driver.title
#elem = driver.find_element_by_name("q").send_keys("pyplan" + Keys.RETURN)
# assert "No results found." not in driver.page_source
# elem.clear()