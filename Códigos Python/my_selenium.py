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
driver.get("http://www.google.com")
# assert "Python" in driver.title
elem = driver.find_element_by_name("q")
#elem = driver.find_element_by_name("q").send_keys("pyplan" + Keys.RETURN)
# elem.clear()
elem.send_keys("pyplan")
elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
time.sleep(1)
driver.close()