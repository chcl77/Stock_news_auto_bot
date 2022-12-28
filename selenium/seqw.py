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
options = webdriver.ChromeOptions()
options.add_argument("headless")

adse = []

driver = webdriver.Chrome(ChromeDriverManager().install()  , options = options)                 #97
driver.get("https://finance.naver.com/item/sise.naver?code=005930")
time.sleep(1) 
table = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[4]/div/div[2]/div/table")
tbody = table.find_element_by_tag_name("tbody")
tr = tbody.find_elements_by_tag_name('td')
# ds = table.find_elements_by_class_name('num')[1]
for i in tr : 
    print(i.text)
    

# d = driver.find_elements_by_class_name("tah.p11")[0]
# print(d.text)

