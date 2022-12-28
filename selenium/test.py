from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os 
import getpass


    


# a = input("Please enter Id \n")
# b = getpass.getpass("Please enter password \n")
# print(b)

 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://news.kbs.co.kr/news/view.do?ncd=5455455&ref=A")

b = driver.find_element_by_class_name("detail-body font-size").find_elements_by_tag_name("br")[2]



time.sleep(3)


print(b)


