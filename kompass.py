from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
import time
from bs4 import BeautifulSoup
import pandas as pd
import csv
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
pg=1
url="https://us.kompass.com/searchCompanies/scroll?tab=cmp&pageNbre="+"1"+"&token=03AHaCkAbZktep4-sPtEtDbZLsNg5BUE4Y7FJsv-n_U5nXqcHBXGL4PffLYswm4ji1n_EA2297znBnQ8G8XMSEW3YnuL2uy4lWWdaYHjJ47zCjs8Y4WlUmW8xWe46QJe2ISNgYJO0Pgh6jDatFDXgZ14PYadCn6XKMajSYVnsve0AaHp9eLxZzNsKq6W2Hl020aVIWh44MsYAasTth-J0AH135PsDlbDh5HEjLElF9MFtYhOnHCLfnVyIMCZmEgkPpagSjYqqnSNKkjSKwyn3Lp3ZdAvqZkkXCETD_dIvLHlLKlc87Kj-zcI0uL1W_tcQZoA9l8RxltkUltZ9TUnYeOvsW2qzClEIJw2glGKJ3uWDYOYpYlJKK4FzPxDQqdJ-pp3Cnhx8ZZ1hNY4e8DXzLyS1Xb1s9bZKS_Tjqafpl6qWAJtofPZTqHpSzFNU0Oi73HpsD5lQve3H4kAEPSYDyBgVnlanVUiorWQ"
#link=url
chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver =webdriver.Chrome(executable_path=r'C:\Users\DELL\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe')
driver.get(url)
time.sleep(3)

cat="supplier_and_manufacture"
country="usa"

def add_fun(driver):
    if pg>1:
        url="https://us.kompass.com/searchCompanies/scroll?tab=cmp&pageNbre="+str(pg)+"&token=03AHaCkAbZktep4-sPtEtDbZLsNg5BUE4Y7FJsv-n_U5nXqcHBXGL4PffLYswm4ji1n_EA2297znBnQ8G8XMSEW3YnuL2uy4lWWdaYHjJ47zCjs8Y4WlUmW8xWe46QJe2ISNgYJO0Pgh6jDatFDXgZ14PYadCn6XKMajSYVnsve0AaHp9eLxZzNsKq6W2Hl020aVIWh44MsYAasTth-J0AH135PsDlbDh5HEjLElF9MFtYhOnHCLfnVyIMCZmEgkPpagSjYqqnSNKkjSKwyn3Lp3ZdAvqZkkXCETD_dIvLHlLKlc87Kj-zcI0uL1W_tcQZoA9l8RxltkUltZ9TUnYeOvsW2qzClEIJw2glGKJ3uWDYOYpYlJKK4FzPxDQqdJ-pp3Cnhx8ZZ1hNY4e8DXzLyS1Xb1s9bZKS_Tjqafpl6qWAJtofPZTqHpSzFNU0Oi73HpsD5lQve3H4kAEPSYDyBgVnlanVUiorWQ"

    try:
        driver.get(url)
        time.sleep(2)
        modal_diag=driver.find_element_by_class_name("modal-content")
        modal_head=modal_diag.find_element_by_class_name("modal-header")
        modal_head.find_element_by_tag_name("button").click()
    except Exception as e:
        print("NO ADD",e)
    
while True:
    
    elem_list=driver.find_elements_by_class_name("prod_list ")
    for e in elem_list:
        try:
            h2_tag=e.find_element_by_tag_name("h2")
            a_tag=h2_tag.find_element_by_tag_name("a").get_attribute("href")
            print(a_tag)
        except Exception as e:
            print("NO A TAG",p)
    driver.execute_script("window.scrollTo(0,50)")
    try:
        time.sleep(3)
        
        pagination=driver.find_element_by_id("pagination-div-id")
        #print(pagination.text)
        a_tagg=pagination.find_elements_by_tag_name("li")[-1]
        next_page=a_tagg.find_element_by_tag_name("a").get_attribute("href")
        #print(next_page)
       
        if next_page==driver.current_url:
            break
        else:
            pg=pg+1
                 
    except Exception as e:
        print("NO NEXT",e)
        break
