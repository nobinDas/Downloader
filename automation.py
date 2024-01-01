from selenium import webdriver as wb
from selenium.webdriver.common.action_chains import ActionChains
driver = wb.Firefox(executable_path= r"C:\Users\nirjh\Desktop\geckodriver\geckodriver")


#url = input('What is the url of the video?: ')


driver.get('https://ytmp3.cc/en13/')

searchButton = driver.find_element_by_xpath('//*[@id="input"]')
searchButton.send_keys('https://www.youtube.com/watch?v=8GGGliIxpgc')
clickButton = driver.find_element_by_xpath('//*[@id="submit"]')
clickButton.click()


downloadButton = driver.find_elements_by_xpath('//*[@id="buttons"]/a[1]')
downloadButton.click()



