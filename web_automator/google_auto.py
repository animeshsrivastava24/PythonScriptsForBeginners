from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("rate", 170)
def google_automator():
    engine.say("Enter your search items")
    engine.runAndWait()
    search_item=str(input("Enter what you want to search for:"))
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://google.com")
        search=driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        search.send_keys(search_item)
        search.send_keys(Keys.ENTER)
    except:
        print("Failing to perform specific action")