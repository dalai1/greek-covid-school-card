#CHROME DRIVER APO EDO   https://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time
onoma_ma8iti = "ονομα"
eponimo_ma8iti = "ΕΠΙΘΕΤΟ"
mera_gennisis="30"
minas_gen = "12"
etos_gen = "2010"
amka_ma8 = "30121011111"
taxis_user_name = "USER"
taxis_password = "PASSWORD"

today = date.today()


PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get ("https://edupass.gov.gr/schools/")



try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="choice"]/label[1]/span[1]/span[1]/input'))
    )

    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form/div/div/button/span[1]'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div/div/div[2]/button[2]/span[1]'))
    )
    search.click()
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div/div[1]/div[2]/div/div[1]/a/span[1]/div[2]'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div[2]/div[1]/div/div/button/span[1]'))
    )
    search.click()
#taxis net

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="v"]'))
    )

    type.send_keys(taxis_user_name)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="j_password"]'))
    )
    
    type.send_keys(taxis_password)

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="btn-login-submit"]'))
    )
    search.click()



    #ay8entikopoiish TAXIS
    try:
        search1 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="btn-submit"]'))
        )

        search1.click()
    except:
        time.sleep(0)


    # back to gov.gr
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/button/span[1]/div'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/div[1]/div/div/div/div'))
    )
    search.click()

#perifereia 
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')) #.../li[1] ΜΑΚΕΔΟΝΙΑ-ΘΡΑΚΗ  .../li[2] ΑΤΤΙΚΗ  κλπ κλπ
    )
    search.click()

    
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/div[2]/div/div/div/div'))
    )
    search.click()

#perifereiakh enotita 
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[6]')) # .../li[1] ΔΡΑΜΑ .../li[2] ΕΒΡΟΥ ΚΛΠ ΚΛΠ
    )
    search.click()

    #dimos 

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/div[3]/div/div/div/div'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]')) #.../li[1]  ΔΗΜΟΙ 
    )
    search.click()

    #katigoria SXOLEIA
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/div[4]/div/div/div/div'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]'))  # .../li[1] ΔΗΜΟΤΗΚΑ-ΓΥΜΝΑΣΙΑ ΚΛΠ
    )
    search.click()

    #typos sxoleiou
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/div[5]/div/div/div/div'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')) # .../li[1] ΤΥΠΟΣ ΣΧΟΛΕΙΟΥ 
    )
    search.click()
    #sxoleio 
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[3]/div/div/div[6]/div/div/div/div'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[6]')) # .../li[1] 1ο 2ο ΔΗΜΟΤΙΚΟ ΣΧΟΛΕΙΟ ΚΛΠ 
        
    )
    search.click()
# SIMPLIROSI KARTELAS COVID
    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[4]/div[1]/div/div/div/input'))
    )
    type.send_keys(onoma_ma8iti)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[4]/div[2]/div/div/div/input'))
    )
    type.send_keys(eponimo_ma8iti)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[4]/div[3]/div/div/div[1]/div/div/input'))
    )
    type.send_keys(mera_gennisis)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[4]/div[3]/div/div/div[2]/div/div/input'))
    )
    type.send_keys(minas_gen)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[4]/div[3]/div/div/div[3]/div/div/input'))
    )
    type.send_keys(etos_gen)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[4]/div[4]/div/div/div/input'))
    )
    type.send_keys(amka_ma8)


    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mui-component-select-can_use_amka"]'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-can_use_amka"]/div[3]/ul/li'))
    )
    search.click()


    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[5]/div[1]/div/div/div[1]/div/div/input'))
    )
    type.send_keys(today.day)


    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[5]/div[1]/div/div/div[2]/div/div/input'))
    )
    type.send_keys(today.month)

    type = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[5]/div[1]/div/div/div[3]/div/div/input'))
    )
    type.send_keys(today.year)

    #apotelesma self test

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mui-component-select-self_test_result"]'))
    )
    search.click()

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-self_test_result"]/div[3]/ul/li[1]'))
    )
    search.click()
    #APOSTOLH (ANENERGH GIA NA KANΟ ELENXO Ή ΑΛΛΑΓΕΣ)
    #search = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div/form/div/div/div[6]/div/div/div/button/span[1]/div'))
    #)
    #search.click()


except:
    time.sleep(1)
