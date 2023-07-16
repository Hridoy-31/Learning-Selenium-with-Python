from selenium import webdriver

# providing the path for geckodriver which is responsible
# for automating firefox
driver = webdriver.Firefox(executable_path="/home/hridoy/BrowserDriver/geckodriver")

driver.get("https://www.github.com")
driver.maximize_window()
print(driver.title)
driver.close()
