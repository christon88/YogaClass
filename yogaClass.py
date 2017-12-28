# -*- coding: utf-8 -*-

#Importing and initializing stuff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

def class_booking(class_name):
    #Importing personal stuff
    adress = open("private_info/adress.txt").read()
    user = open("private_info/user.txt").read()
    password = open("private_info/password.txt").read()
    
    driver = webdriver.Firefox()
    driver.get(adress)
    wait = WebDriverWait(driver, 5)
    
    assert "Timeplan" in driver.title
    
    #Log in
    login = driver.find_element_by_css_selector('i.fa-sign-in')
    login.click()
    
    input_username = driver.find_element_by_css_selector('input#username')
    input_username.clear()
    input_username.send_keys(user)
    
    input_password = driver.find_element_by_css_selector('input#password')
    input_password.send_keys(password)
    input_password.send_keys(Keys.RETURN)
    
    close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close")))
    close_button = driver.find_element_by_css_selector('button.close')
    close_button.click()
    
    time.sleep(3) #This is dumb, but it works
    
    #Find correct date 
    
    next_button = wait.until(EC.element_to_be_clickable((By.ID, "next")))
    next_button = driver.find_element_by_css_selector('#next')
    
    classes = driver.find_elements_by_css_selector('div.instance')
    
    def next():
        refresh_check = driver.find_element_by_css_selector('div.dayName')
        #print(refresh_check.text)
        next_button.click()
        wait.until(EC.staleness_of(refresh_check))
        print("interacted successfully")                                     
    
    next()                                                
    next()
    
    
    classes = driver.find_elements_by_css_selector('div.instance')
    
    for i in classes: 
        if class_name in i.text:
            target_class = i
            
    target_class.find_element_by_css_selector('button.bookButton').click()
    #driver.close()
    

schedule.every().thursday.at("17:11").do(class_booking, "R.O.P.E")   
#schedule.every().sunday.at("22:01").do(class_booking, "R.O.P.E")

while True:
    schedule.run_pending()
    time.sleep(60)