
import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"selenium\chromedriver.exe")
URL = "https://new.land.naver.com/complexes/"


def get_naver_complex(id):
    driver.get(URL + str(id))

    data = []
    try:
        data.append(id)
        category = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "label--category"))).text
        data.append(category)
        title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "complexTitle"))).text
        data.append(title)

        for feature in WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#summaryInfo > .complex_feature > dd"))):
            data.append(feature.text)

        time.sleep(1)
        index = 1
        for region in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "is-selected"))):
            data.append(region.text)
            if index == 3:
                break
            index = index + 1

    except (NoSuchElementException, TimeoutException) as e:
        print(e)
        return -1

    with open('naver.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)

    return 1


failed_id = []
for id in range(1, 20000):
    print(id)
    if get_naver_complex(id) < 0:
        failed_id.append(id)

print(failed_id)



