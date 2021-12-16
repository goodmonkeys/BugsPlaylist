import json
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

    time.sleep(4)
    elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/nav/ul/li[10]/div/a").click()

    time.sleep(5)
    print("b\nb\nb\nb\n")




    articlebox = driver.find_element_by_id('myAlbumListAjax')
    articles = articlebox.find_elements_by_class_name('albumInfo')
    title = articles[0].find_element_by_class_name('albumTitle')
    print(title.text)

    title.click()

    time.sleep(5)

    titlebox = driver.find_element_by_css_selector('table.list.trackList')
    songtitles = titlebox.find_elements_by_class_name('title')
    for songtitle in songtitles:
        try:
            stitle = songtitle.find_element_by_tag_name('a').text
            print(stitle)
        except:
            pass
            print("오류남 씨바꺼")

    driver.back()
    time.sleep(2)

    articlebox = driver.find_element_by_id('myAlbumListAjax')
    articles = articlebox.find_elements_by_class_name('albumInfo')
    title = articles[1].find_element_by_class_name('albumTitle')
    
    title.click()

    time.sleep(5)

    titlebox = driver.find_element_by_css_selector('table.list.trackList')
    songtitles = titlebox.find_elements_by_class_name('title')
    for songtitle in songtitles:
        try:
            stitle = songtitle.find_element_by_tag_name('a').text
            print(stitle)
        except:
            pass
            print("오류남 씨바꺼")

    driver.back()
    time.sleep(2)
    





except:
    print("fads")





# SCROLL_PAUSE_TIME = 1
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector(".mye4qd").click()
#         except:
#             break
#     last_height = new_height

# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count = 1
# for image in images:
#     try:
#         image.click()
#         time.sleep(2)
#         imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
#         opener=urllib.request.build_opener()
#         opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#         urllib.request.install_opener(opener)
#         urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
#         count = count + 1
#     except:
#         pass
# 
# driver.close()



if input():

    driver.Quit()

while(True):

    pass 