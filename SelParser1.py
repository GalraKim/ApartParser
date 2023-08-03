from selenium import webdriver
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import csv




service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
  driver.get("https://tomsk.cian.ru/snyat-kvartiru/")
  driver.implicitly_wait(7)

  actions = ActionChains(driver)
  actions.move_to_element(driver.find_element(By.CSS_SELECTOR, '[class="button-root-10-1-1 button-root--primary-outline-10-1-1 button-root--medium-10-1-1 button-root--type-button-reset-10-1-1 button-root--fluid-10-1-1"]'))
  actions.perform()
  wait = WebDriverWait(driver, timeout=6)
  
  while True:
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="button-root-10-1-1 button-root--primary-outline-10-1-1 button-root--medium-10-1-1 button-root--type-button-reset-10-1-1 button-root--fluid-10-1-1"]'))).click()
    wait = WebDriverWait(driver, timeout=3)

except Exception as ex:
  print(f'Error: {ex}')

html = driver.page_source
driver.quit()



# try:
#     final_result = []
#     soup = BeautifulSoup(html, 'html5lib')
    
#     divs = soup.select_one("div.sc-26679455-1.gGStFX")
    
#     for div in divs:
#       name = div.select_one("h2.sc-d9406361-0.hdfxoN").text
#       target = div.select_one("span.sc-96470d6e-2.jsNMaY").text
#       code = div.select_one("p.sc-d9406361-0.cCQtSh").text[4:]
#       notebook = {
#         "Name": name, 
#         "Target": target,
#         "Code": code
#       }
#       final_result.append(notebook)


# except HTTPError as ht:
#   print(f"ERROR: {ht}")
# except Exception as ex:
#   print(f"ERROR: {ex}")

# with open("task2_2.csv", "w",  encoding="utf-8") as f:
#   writer = csv.DictWriter(f, final_result[0].keys())
#   writer.writeheader()
#   for r in final_result:
#     writer.writerow(r)
