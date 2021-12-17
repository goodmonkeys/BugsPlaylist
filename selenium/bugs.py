
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


    articlebox = driver.find_element_by_id('myAlbumListAjax')
    articles = articlebox.find_elements_by_class_name('albumInfo')
    title = articles[0].find_element_by_class_name('albumTitle')
    print(title.text)

    title.send_keys(Keys.CONTROL + "\n")

    print(driver.window_handles)

    # 새로운 탭으로 초점을 전환
    # driver.switch_to_window(driver.window_handles[-1])
    driver.switch_to.window(driver.window_handles[-1])
    # 현재 탭 종료driver.close()
    # 첫번째 탭으로 전환
    # driver.switch_to_window(driver.window_handles[0])

    # 모든 탭 종료
    # driver.quit()
    





    time.sleep(2)

    titlebox = driver.find_element_by_css_selector('table.list.trackList')
    songtitles = titlebox.find_elements_by_class_name('title')
    for songtitle in songtitles:
        try:
            stitle = songtitle.find_element_by_tag_name('a').text
            print(stitle)
        except:
            pass
            print("오류남 씨바꺼")








# 첫번째 앨범에서 제목 가져옴

    # driver.back()
    # time.sleep(2)

    # articlebox = driver.find_element_by_id('myAlbumListAjax')
    # articles = articlebox.find_elements_by_class_name('albumInfo')
    # title = articles[1].find_element_by_class_name('albumTitle')
    
    # title.click()

    # time.sleep(5)

    # titlebox = driver.find_element_by_css_selector('table.list.trackList')
    # songtitles = titlebox.find_elements_by_class_name('title')
    # for songtitle in songtitles:
    #     try:
    #         stitle = songtitle.find_element_by_tag_name('a').text
    #         print(stitle)
    #     except:
    #         pass
    #         print("오류남 씨바꺼")





except:
    print("fads")







if input():

    driver.Quit()

while(True):

    pass 