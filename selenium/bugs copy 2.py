
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import urllib.request
# python -m venv selenium
# cd selenium\Scripts
# activate
# pip install selenium





driver = webdriver.Chrome(r"selenium\chromedriver.exe")
driver.get("https://id.payco.com/oauth2.0/authorize?isBackButton=false&response_type=code&client_id=3RDtEDzmjKV9oZ7VFhSy&serviceOfferYn=Y&serviceClientId=3RDtEDzmjKV9oZ7VFhSy&viewType=&serviceProviderCode=FRIENDS&scope=&state=state&termsYN=N&autoOauthYn=N&redirect_uri=https%3A%2F%2Fsecure.bugs.co.kr%2Fmember%2Fpayco%2Fcallback")

try:


        

    elem = driver.find_element_by_id("id")
    elem.send_keys("goodmonkeys@naver.com")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_name("pw")
    elem.send_keys("dlfjs1818")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_id("birthday")
    elem.send_keys("19980923")
    elem.send_keys(Keys.RETURN)

    time.sleep(1)
    elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/nav/ul/li[10]/div/a").click()

    time.sleep(1)
    print("b\nb\nb\nb\n")

# 로그인 완료


    # articlebox = driver.find_element_by_id('myAlbumListAjax')
    # articles = articlebox.find_elements_by_class_name('albumInfo')


    # for article in articles:
    #     title = article.find_element_by_class_name('albumTitle')
    #     print(title.text)
       
    for feature in WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "albumTitle"))):
        print(feature.text)

        





except:
    print("fads")







if input():

    driver.Quit()

while(True):

    pass 