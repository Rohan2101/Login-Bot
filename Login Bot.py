from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# create webdriver object
driver = webdriver.Chrome()

# enter keyword to search


# get geeksforgeeks.org
driver.get("https://wazirx.com")
winHandleBefore = driver.window_handles
print(winHandleBefore)
element = driver.find_element(by='xpath', value="/html/body/div/div/nav/div/div[2]/ul/li[3]/a/div")
winHandleBefore = driver.window_handles
print(winHandleBefore)
element.click()
winHandleBefore = driver.window_handles
print(winHandleBefore)
driver.implicitly_wait(5)

element2 = driver.find_element(by='xpath', value='/html/body/div[1]/div/div[2]/div/div/form/div[1]/div[1]/div/input')
element2.send_keys('rohan2101@protonmail.com')
winHandleBefore = driver.window_handles
print(winHandleBefore)

element3 = driver.find_element(by='xpath', value='/html/body/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/input')
element3.send_keys('Newshit')
winHandleBefore = driver.window_handles
print(winHandleBefore)
element4 = driver.find_element(by='xpath', value="/html/body/div[1]/div/div[2]/div/div/form/button")
element4.click()
winHandleBefore = driver.window_handles
print(winHandleBefore)
driver.implicitly_wait(15)
element9 = driver.find_element(by='xpath', value='/html/body/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/input')
element9.send_keys('ftm')
driver.implicitly_wait(5)
element10 = driver.find_element(by='xpath',value='/html/body/div[2]/div/div[2]/div/div[1]/div/div[2]/a/div[2]/div[1]')
element10.click()
element5 = driver.find_element(by='xpath', value='/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/form/div[2]/div/div/div[2]/span')
element5.click()
element6 = driver.find_element(by='xpath', value='/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/form/div[4]/div/div[1]/input')
element6.send_keys('10000')
element7 = driver.find_element(by='xpath', value='/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div/div[2]/div/form/button/span')
element7.click()
element8 = driver.find_element(by='xpath', value='/html/body/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/button/span')
element8.click()
winHandleBefore = driver.window_handles
print(winHandleBefore)