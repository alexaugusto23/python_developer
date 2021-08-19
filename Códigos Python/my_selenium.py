from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 

# Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:	https://github.com/mozilla/geckodriver/releases
# Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
# Variaveis de sistema no cmd echo %path%
# https://sites.google.com/a/chromium.org/chromedriver/

# print( os.getcwd)
# print( os.system('cd ..'))
# print( os.chdir('C:/'))
print( os.getcwd)

# driver = webdriver.Chrome(executable_path=r'C:/chromedriver/chromedriver.exe')
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()