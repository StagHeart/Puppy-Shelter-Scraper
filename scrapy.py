import mechanize
import urllib2
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import os
import re
import datetime

import smtplib


mail = smtplib.SMTP('smtp.gmail.com', 587)
myEmail = "your_email"

# Function Send Puppies name to my email
def sendEmail(str):
    mail.starttls()
    mail.ehlo()
    mail.login("your_email",'your_password')
    mail.sendmail("your_email","your_email", str)
    mail.close()

# Function get to Puppy Page
def getToPuppies():
    elem = browser.find_element_by_class_name("default")
    time.sleep(3)
    for x in range(0, 10):
        elem.send_keys(Keys.ARROW_DOWN)
        time.sleep(.2)

    elem.send_keys(Keys.RETURN) 
    return;

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]

browser = webdriver.Firefox()
browser.get("website_for_puppies")

getToPuppies()

storageList = []
i = 0

timesLooped = 0

elemTwo = browser.find_elements_by_class_name("animal-name")

for name in elemTwo:
    storageList.append(name.text)
    print name.text + " Successfuly storage = " + storageList[i]
    i += 1

while(True):
    browser.refresh()
    getToPuppies()

    print "Refresh Success"

    elemThree = browser.find_elements_by_class_name("animal-name")
    time.sleep(1)

    newPuppies = []

    for name in elemThree:
        
        nameIsAlreadyStored = False
        for item in storageList:
            
            print "COMPARING " + name.text + " & " + item
            if name.text == item:
                nameIsAlreadyStored = True
        
        if nameIsAlreadyStored == False:

            storageList.append(name.text)
            newPuppies.append(name.text)
        
        else:
            
            print name.text + " is already Stored"
    
    if newPuppies:
        
        content = " THERE'S NEW PUPPIES!: " +  ', '.join(newPuppies)
        print content
        print datetime.datetime.now()
        sendEmail(content)
        time.sleep(300)
    
    if not newPuppies:
        
        print " No new puppies"
        print  datetime.datetime.now()

    timesLooped += 1
    print "Times Looped: " , timesLooped
    
    time.sleep(900)




