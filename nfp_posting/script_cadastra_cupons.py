from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class CadastramentodeCupons():
 
  def execute(self, driver):
    # Test name: Cadastramento de Cupons
    # Step # | name | target | value | comment
    # 1 | open | /principal.aspx |  | 
    #driver.get("https://www.nfp.fazenda.sp.gov.br/principal.aspx")
    # 2 | setWindowSize | 1936x1056 |  | 
    driver.set_window_size(1936, 1056)
    # 3 | click | linkText=Entidades |  | 
    driver.find_element(By.LINK_TEXT, "Entidades").click()
    # 4 | click | linkText=Cadastramento de Cupons |  | 
    driver.find_element(By.LINK_TEXT, "Cadastramento de Cupons").click()
    # 5 | click | id=ctl00_ConteudoPagina_btnOk |  | 
    driver.find_element(By.ID, "ctl00_ConteudoPagina_btnOk").click()
    # 6 | click | id=ddlEntidadeFilantropica |  | 
    driver.find_element(By.ID, "ddlEntidadeFilantropica").click()
    # 7 | select | id=ddlEntidadeFilantropica | label=GACC GRUPO DE ASSISTENCIA A CRIANCA COM CANCER | 
    dropdown = driver.find_element(By.ID, "ddlEntidadeFilantropica")
    dropdown.find_element(By.XPATH, "//option[. = 'GACC GRUPO DE ASSISTENCIA A CRIANCA COM CANCER']").click()
    # 8 | click | id=ddlEntidadeFilantropica |  | 
    driver.find_element(By.ID, "ddlEntidadeFilantropica").click()
    # 9 | click | id=ctl00_ConteudoPagina_btnNovaNota |  | 
    driver.find_element(By.ID, "ctl00_ConteudoPagina_btnNovaNota").click()
    # 10 | click | css=#divDocComChave > fieldset |  | 
    driver.find_element(By.CSS_SELECTOR, "#divDocComChave > fieldset").click()
    # 11 | click | id=btnSalvarNota |  | 
    driver.find_element(By.ID, "btnSalvarNota").click()
  
