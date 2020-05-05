from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup

#Url Which We Are Scraping
url = "https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
session = HTMLSession()
# App Started ...
print("Application Started..........")  
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") 
 
driver.maximize_window()  
#Starting The Session
session.get(url)

driver.get(url)  
#Send Data To The Input DL 
driver.find_element_by_name("form_rcdl:tf_dlNO").send_keys("DL-0420110149646")  
time.sleep(1)  
#Send Data To The Input DOB
driver.find_element_by_name("form_rcdl:tf_dob_input").send_keys("09-02-1976")  
time.sleep(1)  
#Send Data To The Input CAPTCHA
str = input("Enter CaptchaID : ")

driver.find_element_by_name("form_rcdl:j_idt34:CaptchaID").send_keys(str)  
time.sleep(1)  
#Send Data To The Input Button

driver.find_element_by_name("form_rcdl:j_idt46").send_keys(Keys.ENTER)  
time.sleep(1)  

print("Successfully Filled Data.....")

print("Scraping Now .......")

print("\n\n\n")
body = driver.page_source

print(body)