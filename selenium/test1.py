
from tkinter import * 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys, os 
import requests

options = webdriver.ChromeOptions()
options.add_argument("headless")

root = Tk()
root.title("stock_crawling")
root.geometry("640x480")

def post_message(token, channel, text):
    global response
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)


myToken = "xoxb-2258436223106-2258492177138-9QoJUrMEJQerhHIG1IbBTD4O"

def show(sew): 
    
    
    global label23 , label231 , label232 , label233 , label234
    label23 = Label(root, text = sew[0] )
    label23.pack()
    label23.place(x = 50 , y = 270)
    label231 = Label(root, text = sew[1] )
    label231.pack()
    label231.place(x = 50 , y = 310)
    label232 = Label(root, text = sew[2] )
    label232.pack()
    label232.place(x = 50 , y = 350)
    label233 = Label(root, text = sew[3] )
    label233.pack()
    label233.place(x = 50 , y = 390)
    label234 = Label(root, text = sew[4] )
    label234.pack()
    label234.place(x = 50 , y = 430)
   

def first_stock(): 
    driver1 = webdriver.Chrome(ChromeDriverManager().install() , options=options)
    driver1.get("https://m.stock.naver.com/")
    time.sleep(1)
    dsewqr = []
    
    
    for i in range(0, 5):
        dsq = driver1.find_elements_by_class_name("CommTable_name__1LjLZ")[3 * i].text
        dsewqr.append(dsq)
        print(dsewqr[i])
    show(dsewqr)

def clear():
    print(ent.get())
    global nm 
    global cse 
    nm = ent.get()
    cse = ent1.get()
    cse = int(cse)
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
    for i in range(0, cse):
        a = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("title")
        b = driver.find_elements_by_css_selector(".thumb.api_get")[i].get_attribute("src")
        c = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("href")
        
        post_message(myToken,"stock-selling",a) 
        # post_message(myToken,"stock-selling",b) 
        post_message(myToken,"stock-selling",c)  
    

         
        

    

label1 = Label(root, text = "주식 크롤링 프로그램")
label1.pack()
label1.place(x=265, y = 10)
btn3 = Button(root, text = "시작" , width= 10 , command = clear)

btn3.pack()
btn3.place(x=540, y=95)

btn1_1 = Button(root, text = "국내 TOP 종목", width= 10 , command = first_stock    )
btn1_1.pack()
btn1_1.place(x = 30 , y = 200)

btn1_2 = Button(root, text = "글로벌 TOP 종목", width= 12 , command = show    )
btn1_2.pack()
btn1_2.place(x = 265 , y = 200)

btn1_3 = Button(root, text = "HOT 랭킹", width= 10 , command = show    )
btn1_3.pack()
btn1_3.place(x = 510 , y = 200)
# txt = Text(root , width = 50)
# txt.pack()
ent = Entry(root , width = 70)
ent.pack()
ent.place(x=10, y=100)
ent.insert(END,  "검색어를 입력하십시오")

ent1 = Entry(root , width = 70)
ent1.pack()
ent1.place(x=10, y=130)
ent1.insert(END,  "기사의 갯수를 입력하십시오")

root.mainloop()