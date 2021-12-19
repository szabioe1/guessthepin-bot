from selenium import webdriver
import random
import string


nums = string.digits
length = 4
driver = webdriver.Chrome("C:/Users/Szabi/Documents/chromedriver.exe")
url = "https://www.guessthepin.com"
driver.get(url)
attempt = ( ''.join(random.choice(nums) for i in range(length)))
    
driver.find_element_by_id("pin").send_keys(str(attempt))
driver.find_element_by_css_selector("#container > form > input:nth-child(4)").click()


while True:
    nums = string.digits
    length = 4
    attempt = ( ''.join(random.choice(nums) for i in range(length)))
    driver.find_element_by_id("pin").send_keys(str(attempt))
    driver.find_element_by_css_selector("#container > form > input:nth-child(5)").click()


#container > form > input:nth-child(4)
#container > form > input:nth-child(5)