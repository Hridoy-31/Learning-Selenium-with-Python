from selenium import webdriver

# providing the chromedriver location
driver = webdriver.Chrome(executable_path="/home/hridoy/BrowserDriver/chromedriver")

# providing the url of the website to the browser to go to
# "https" should be provided. !!! MUST !!!
driver.get("https://www.facebook.com")
# printing the title of the website
print(driver.title)
# maximizing the browser window
driver.maximize_window()
# closing the browser
driver.close()
