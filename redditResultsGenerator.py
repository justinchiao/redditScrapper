import requests
import string
import re
import csv
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time 

def scrapeComments(url):
    '''outputs all comment text from URL as a list of strings with only english characters and arabic numbers'''
    # instantiate options 
    options = webdriver.ChromeOptions() 
    # run browser in headless mode 
    options.headless = True 
    driver = webdriver.Chrome(service=ChromeService( 
	    ChromeDriverManager().install()), options=options) 

    # get the entire website content 
    driver.get(url)
    with open('readme.txt', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    
    items = [] 
    # instantiate height of webpage 
    last_height = driver.execute_script('return document.body.scrollHeight') 
 
    # set target count 
    itemTargetCount = 2
 
    # scroll to bottom of webpage 
    #while itemTargetCount > len(items): 
        #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #time.sleep(5)
        
        #new_height = driver.execute_script('return document.body.scrollHeight') 
 
        #if new_height == last_height: 
            #break 
        
        #last_height == new_height 
 
	    # select elements by XPath
        #elements = driver.find_elements(By.XPATH, "//div[@class='_2i5O0KNpb9tDq0bsNOZB_Q']/div/div/a/div/h3")
        #h3_texts = [element.text for element in elements]
        #items = items + h3_texts

    while itemTargetCount > len(items): 
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)
        
        new_height = driver.execute_script('return document.body.scrollHeight') 
 
        if new_height == last_height: 
            break 
        
        last_height == new_height 
 
	    # select elements by XPath
        elements = driver.find_elements(By.XPATH, "//div[@class='_2i5O0KNpb9tDq0bsNOZB_Q']/div/div/a")
        h3_texts = [element.text for element in elements]
        items = items + h3_texts
    print(items)
    print(len(items))
    #items = items[0:itemTargetCount]
    #urls=[]
    #for i in range(len(items)):
        #print(driver.find_element(By.LINK_TEXT, //a/div/h3[text()=items[i]]).text)

    #print(urls)
    