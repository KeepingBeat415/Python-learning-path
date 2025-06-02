from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import requests

service = Service()

def get_driver():
    # set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    #     options.add_experimental_option("prefs", {
    #     "credentials_enable_service": False,
    #     "profile.password_manager_enabled": False
    # })
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # macOS Chrome path
    # block white screen
    options.add_argument("--headless")  # Don't use this unless necessary


    driver = webdriver.Chrome(service=service,options=options)
    driver.get("http://automated.pythonanywhere.com")
    #driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    
    # grab static value
    #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    
    count = 0
    with open('scrap_msg.txt', 'w') as file:
        
        while count < 5:
        #grab dynamic value
            time.sleep(2)
            element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
            
            # Get current system time in seconds since epoch (float)
            timestamp = time.time()

            # Convert to readable format
            local_time = time.ctime(timestamp)
            file.write(f"{local_time} -- {clean_text(element)} \n")
            count += 1    
    
    #login
    # driver.find_element(by="id", value="id_username").send_keys("automated")
    # time.sleep(2)
    # driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    # time.sleep(2)
    # # driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    # # print(driver.current_url)
    
    # driver.find_element(by='xpath', value="/html/body/nav/div/a").click()
    # time.sleep(2)
    
    # text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    # return clean_text(text)
    
    # #return element.text

# selenium
 print(main())
 
# beautiful Soup

