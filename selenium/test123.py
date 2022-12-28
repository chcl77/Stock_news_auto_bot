from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os 
import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2258436223106-2258492177138-9QoJUrMEJQerhHIG1IbBTD4O"


nm = input("검색어 설정 \n")
n = input("기사의 갯수 \n")
n = int(n)
nm = str(nm)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://news.naver.com/")
time.sleep(1)
dsw = driver.find_element_by_css_selector(".Nicon_search")
dsw.click()

time.sleep(1)
dsq = driver.find_element_by_name("query")
dsq.send_keys(nm)
time.sleep(1)
dsq.send_keys(Keys.ENTER)
time.sleep(1)
driver.switch_to_window(driver.window_handles[1])




time.sleep(5)


for i in range(0, n):
    a = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("title")
    b = driver.find_elements_by_css_selector(".thumb.api_get")[i].get_attribute("src")
    c = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("href")
    
    post_message(myToken,"stock-selling",a) 
    # post_message(myToken,"stock-selling",b) 
    post_message(myToken,"stock-selling",c)   
    

# driver.find_element_by_css_selector(".Nicon_search").click()

# d =  driver.find_element_by_name("query")
# time.sleep(1)
# d.send_keys(nm)
# time.sleep(1)
# d.send_keys(Keys.ENTER)




# time.sleep(1)
# for  i in range(0, n) :
#     a = driver.find_elements_by_css_selector(".news_tit")[i]
#     c = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("title")
#     b = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("href")
#     # post_message(myToken,"stock-selling",c)
#     post_message(myToken,"stock-selling",b)  