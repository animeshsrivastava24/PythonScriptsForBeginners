from selenium import webdriver
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("rate", 170)
def youtube_automator():
    engine.say("Enter your youtube search item")
    engine.runAndWait()
    search_item=str(input("Enter what you want to search for:"))
    filtered_search=search_item.replace(' ','+')
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(f"https://www.youtube.com/results?search_query={filtered_search}")
    except:
        print("Failing to perform specific action")