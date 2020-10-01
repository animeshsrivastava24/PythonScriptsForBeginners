from selenium import webdriver
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("rate", 170)
def facebook_automator():
    engine.say("Enter your Facebook email or phone Number")
    engine.runAndWait()
    Email_or_Phone=str(input("Enter your facebook email or phoneNumber : "))
    engine.say("Enter your Facebook password")
    engine.runAndWait()
    Password=str(input("Enter your facebook password : "))
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://facebook.com")
        Email_input=driver.find_element_by_xpath('//*[@id="email"]')
        Password_input=driver.find_element_by_xpath('//*[@id="pass"]')
        Email_input.send_keys(Email_or_Phone)
        Password_input.send_keys(Password)
        Login=driver.find_element_by_xpath('//*[@id="u_0_b"]')
        Login.click()
    except:
        print("Failing to perform specific action")