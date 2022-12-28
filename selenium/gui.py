from asyncio.windows_events import NULL
import tkinter.messagebox as msg
import time
import tkinter.ttk as ttk
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
root.title("주식 기사 크롤링 프로그램")

def post_message(token, channel, text):
    global response
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

    
myToken = "xoxb-2258436223106-2258492177138-9QoJUrMEJQerhHIG1IbBTD4O"

def info():
    msg.showinfo("알림", "크롤링 한 정보를 slack 메신저로 전송했습니다.")

def warn():
    msg.showwarning("경고", "현재 경고를 알림 중입니다")


def crawling(): 
    global nm 
    global cse 
    # nm = ent.get()
    # cse = ent1.get()
    nm = ent.get()
    cse = ent1.get()
    cse = int(cse)
    driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
    driver.get("https://news.naver.com/")
    time.sleep(1) # step 1
    for i in  range(1, 21): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()
    dsw = driver.find_element_by_css_selector(".Nicon_search")
    dsw.click()

    time.sleep(1) # step 2
    for i in  range(21, 41): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()

    dsq = driver.find_element_by_name("query")
    dsq.send_keys(nm)
    time.sleep(1) # step 3
    for i in  range(41, 61): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()
    dsq.send_keys(Keys.ENTER)
    time.sleep(1) # step 4
    for i in  range(61, 81): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()
    driver.switch_to_window(driver.window_handles[1])

    time.sleep(3)
    dst = 10 / cse
    for i in  range(81, 91): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()
        
    for i in range(0, cse):       # 0 ~ cse - 1  => cse                                            # 90 ~ 100                 d = 10 / cse           n =   i + 1          2n +89     
        a = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("title")
        b = driver.find_elements_by_css_selector(".thumb.api_get")[i].get_attribute("src")
        c = driver.find_elements_by_css_selector(".news_tit")[i].get_attribute("href")
        
        
        
        
        
        post_message(myToken,"stock-selling",a) 
        # post_message(myToken,"stock-selling",b) 
        post_message(myToken,"stock-selling",c)
    
    for i in  range(91, 101): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()
        
    info()


def first_stock(): 
    list_file.delete(0, END)
    driver1 = webdriver.Chrome(ChromeDriverManager().install(), options = options )
    driver1.get("https://m.stock.naver.com/")
    time.sleep(1)
    dsewqr = []
    
    
    for i in range(0, 10):
        dsq = driver1.find_elements_by_class_name("CommTable_name__1LjLZ")[3 * i].text
        dsewqr.append(dsq)
        list_file.insert(i , "{0}. ".format(i + 1) + dsewqr[i])
        print(dsewqr[i])

def first_stock1(): 
    list_file.delete(0, END)
    driver1 = webdriver.Chrome(ChromeDriverManager().install() , options=options)
    driver1.get("https://m.stock.naver.com/")
    time.sleep(1)
    dsewqr = []
    
    
    for i in range(1, 6):
        dsq = driver1.find_elements_by_class_name("CommTable_name__1LjLZ")[3 * i + 27].text
        dsewqr.append(dsq)
        list_file.insert(i - 1 ,  "{0}. ".format(i) + dsewqr[i - 1])
        print(dsewqr[i - 1])


# 30
def first_stock2(): 
    sewasq = []
    list_file.delete(0, END)
    driver1 = webdriver.Chrome(ChromeDriverManager().install() , options=options )
    driver1.get("https://m.stock.naver.com/")
    time.sleep(1)
    dsewqr = []
    
    
    for i in range(1, 6):
        dsq = driver1.find_elements_by_class_name("CommTable_name__1LjLZ")[3 * i + 42].text #57
        dse = driver1.find_elements_by_class_name("CommTable_code__2vSjg")[3 * i + 27].text
        dsewqr.append(dsq)
        sewasq.append(dse)
        list_file.insert(i - 1 , "{0}. ".format(i) + dsewqr[i - 1] + " " +  sewasq[i - 1])
        print(dsewqr[i - 1])


def first_stock3(): 
    sewasq = []
    list_file.delete(0, END)
    driver1 = webdriver.Chrome(ChromeDriverManager().install() , options=options  )                   #60
    driver1.get("https://m.stock.naver.com/")
    time.sleep(1)
    dsewqr = []
    
    
    for i in range(1, 11):
        dsq = driver1.find_elements_by_class_name("CommTable_name__1LjLZ")[3 * i + 57].text
        
        dsewqr.append(dsq)
        
        list_file.insert(i - 1 , "{0}. ".format(i) +  dsewqr[i - 1] )
        print(dsewqr[i - 1])

def first_stock4(): 
    list_file.delete(0, END)
    driver1 = webdriver.Chrome(ChromeDriverManager().install() , options=options)
    driver1.get("https://m.stock.naver.com/domestic/upper/KOSPI")
    time.sleep(1)
    dsewqr = []
    
    
    for i in range(0, 15):
        dsq = driver1.find_elements_by_class_name("CommTable_name__1LjLZ")[i].text
        
        dsewqr.append(dsq)
        list_file.insert(i , "{0}. ".format(i + 1) + dsewqr[i])
        print(dsewqr[i])

# 기사 제목 , 기사 수 받는 엔트리

stock_frame = LabelFrame(root, text = "주식 기사 정보 입력창")
stock_frame.pack(fill = "x" ,padx=5, pady=5)
ent = Entry(stock_frame)
ent.pack(fill = "x" ,padx = 5 , pady = 5)
ent.insert(END , "검색어를 입력하십시오")
ent1 = Entry(stock_frame)
ent1.pack(fill = "x" ,padx = 5 , pady = 5)
ent1.insert(END , "기사의 수를 입력하십시오")

list_frame = Frame(root)
list_frame.pack(fill = "y" ,padx=5, pady=5)

global list_file 
list_file = Listbox(list_frame, selectmode = "extended" , height = 10 ,width = 50 )
list_file.pack(side = "left", fill = "y", expand = True)



btn1 = Button(list_frame, text = "실시간 인기 종목" , command = first_stock, width = 12 , height = 2)
btn1.pack(padx = 5 , pady = 5)
btn2 = Button(list_frame, text = "국내 TOP 종목" , command = first_stock1, width = 12 , height = 2)
btn2.pack(padx = 5 , pady = 5)
btn3 = Button(list_frame, text = "해외 TOP 종목" , command = first_stock2, width = 12 , height = 2)
btn3.pack(padx = 5 , pady = 5)
btn4 = Button(list_frame, text = "HOT 랭킹"  , command = first_stock3,   width = 12, height = 2)
btn4.pack(padx = 5 , pady = 5)
btn5 = Button(list_frame, text = "Lee sam's Pick" , command = first_stock4, width = 12, height = 2)
btn5.pack(padx = 5 , pady = 5)

frame_progress = LabelFrame(root , text = "진행상황")
frame_progress.pack(fill = "x" , padx=5, pady=5)
p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progress , maximum = 100 , length = 200 , variable = p_var)
progressbar.pack(fill = "x" , padx=5, pady=5)

frame_lastButton = Frame(root)
frame_lastButton.pack(fill = "x")


btns1 = Button(frame_lastButton , text = "닫기" , width = 10)
btns1.pack(side = "right" ,padx=5, pady=5)
btns = Button(frame_lastButton , text = "크롤링 시작" , command = crawling,  width = 10 )
btns.pack(side = "right" ,padx=5, pady=5)



root.resizable(False, False)
root.mainloop()
