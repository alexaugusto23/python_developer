from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from credenciais import usuario, senha
import scrapy
import time

chromepatah = "C:/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromepatah)
driver.get("https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/taxas-de-cri-e-cra/taxas-de-cri-e-cra.htm")

# Pelo path html
elem = driver.find_element_by_xpath('/html/body/div[5]/div/main/div[2]/div/form/input[14]')

time.sleep(10)

elem.click()

time.sleep(1)
driver.close()

'''
[17:36] THAUAN AUGUSTO DIAS DE QUEIROZ FONSECA
    https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/taxas-de-cri-e-cra/taxas-de-cri-e-cra.htm
​[17:36] THAUAN AUGUSTO DIAS DE QUEIROZ FONSECA
    https://www.btgpactualdigital.com/renda-fixa/debentures/produtos
BTG Pactual digital: Invista em Tesouro Direto, CDB e LCIAbra sua conta e invista de forma simples em Fundos de Investimento, LCI, Tesouro Direto, CDB, COE e Previdência Privada com o BTG Pactual digital!www.btgpactualdigital.com​[17:39] THAUAN AUGUSTO DIAS DE QUEIROZ FONSECA
    thauan.fonseca@modal.com.br


'''