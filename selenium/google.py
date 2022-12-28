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

driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+")
time.sleep(1)
d = driver.find_elements_by_css_selector(".info_variation")[0]
e = driver.find_elements_by_css_selector(".info_variation")[1]
f = driver.find_elements_by_css_selector(".info_variation")[2]
g = driver.find_elements_by_css_selector(".info_variation")[3]
time.sleep(3)
yesterday_confirmed_case = driver.find_element_by_xpath('//*[@id="target2"]/dl/div[6]/dd[1]/span/span')

se = yesterday_confirmed_case.text

se = se.replace(",","")
se = int(se)


time.sleep(1)
print("확진환자 : " + d.text)
print("격리해제 : " + e.text)
print("사망자 : " + f.text)
print("검사진행 : " + g.text)
d= d.text
d = d.replace(",","")
d = int(d)
print(d)
print(se)
print(d)
if d > se :
    avd = d - se
    print(avd)
    print("오늘의 코로나 확진 환자는 전날에 비해"  + str(avd) + "만큼 더 많습니다")
elif d < se  :
    avde = se - d 
    print(avde)
    print("오늘의 코로나 확진 환자는 전날에 비해"+ str(avde) + "만큼 줄었습니다")
# driver.quit()
driver.find_elements_by_css_selector(".tab")[1].click()
time.sleep(1)
print("\n")
print("코로나 관련 뉴스 \n")
for i  in range(10):
    print(driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("title") + driver.find_elements_by_css_selector(".info")[i].text)
    print(driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("href"))
    print("\n")


# os.system('pause')


# elem = driver.find_element_by_name("j_username")
# elem.send_keys(a)
# time.sleep(1)
# elem = driver.find_element_by_name("j_password")
# elem.send_keys(b)
# time.sleep(1)
# elem.send_keys(Keys.RETURN)
# time.sleep(1)
# driver.get("https://ccb.ebsoc.co.kr/student/home")

# time.sleep(1)
# d = driver.find_element_by_css_selector(".tah.p11")
# time.sleep(1)
# print(d.text)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()