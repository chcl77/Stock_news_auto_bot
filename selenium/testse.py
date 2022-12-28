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

driver = webdriver.Chrome(ChromeDriverManager().install() )                 #97
driver.get("https://finance.naver.com/item/sise.naver?code=005930")
time.sleep(1) #pgRR
table = driver.find_element_by_class_name("type2")
tbody = table.find_element_by_tag_name("tbody")
for tr in tbody.find_elements_by_tag_name("tr"):
    td =  tr.find_elements_by_tag_name("td")
    tse = tr.text
    adse = tse.split("\n")
    print(adse)
    
    
    
print("\n")
print(adse[0])

# d = driver.find_elements_by_class_name("tah.p11")[0]
# print(d.text)









 