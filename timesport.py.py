from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time
import pymongo
driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://timesofindia.indiatimes.com/explainers/sports")

y=3000
for i in range(10):
    driver.execute_script(f"window.scrollTo(0, {y} )") 
    y+=2000
    time.sleep(2)


data = driver.page_source
alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')
Link=[]
Paragrap=[]
Date=[]
Head=[]
head=driver.find_elements('//*[@id="app"]/div/div[5]/div/div[2]/div/div/div/div[1]/div[2]/ul/li/a/div/h5/text()')
date=soup.find_all('span',class_="_2vAWf")
link=driver.find_elements(By.XPATH,"//*[@id='app']/div/div[5]/div/div[2]/div/div/div/div[1]/div[2]/ul/li/a")
cem=""
for a in range(10):
    Head.append(head[a].text)
    print(Head[0])
    break
    
for b in range(10):
    Date.append(date[b].string)



for l in range(10):
    Link.append(link[l].get_attribute('href'))


    
print(len(Paragrap))
print(len(Date))
print(len(Head))
print(len(Link))
print('hey')
client =pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db = client['TIMES12']
collection =db ['project12']
for i in range(10):
    dictionary = {"HEAD":Head,'LINK':Link[i],'DATE':Date[i]}
    collection.insert_one(dictionary)
