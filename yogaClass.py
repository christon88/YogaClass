# -*- coding: utf-8 -*-

#Importing and initializing stuff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Importing personal stuff
adress = open("private_info/adress.txt").read()
user = open("private_info/user.txt").read()
password = open("private_info/password.txt").read()

driver = webdriver.Firefox()
driver.get(adress)
wait = WebDriverWait(driver, 2)
driver.implicitly_wait(2) # seconds

def interact(function_name):
    refresh_check = driver.find_element_by_css_selector('div.dayName')
    print(refresh_check.text)
    function_name
    wait.until(EC.staleness_of(refresh_check))                                      

assert "Timeplan" in driver.title

login = driver.find_element_by_css_selector('i.fa-sign-in')

login.click()

#Log in
input_username = driver.find_element_by_css_selector('input#username')
input_username.clear()
input_username.send_keys(user)

input_password = driver.find_element_by_css_selector('input#password')
input_password.send_keys(password)
input_password.send_keys(Keys.RETURN)

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop')))
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-backdrop')))

#Find correct date
next_button = driver.find_element_by_css_selector('#next')

while driver.find_element_by_css_selector('div.dayName').text == "I DAG":
    next_button.click()
    

classes = driver.find_elements_by_css_selector('div.instance')


                                                  
interact(next_button.click())



#next_button.click()

#refresh()


#classes = driver.find_elements_by_css_selector('p.name')
classes = driver.find_elements_by_css_selector('div.instance')

for i in classes: 
    print(i.text)

#driver.close()