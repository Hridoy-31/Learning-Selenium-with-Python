from selenium import webdriver
# importing ChromeDriverManager() from webdriver_manager
# it will manage Chrome driver automatically with the
# correspoding Chrome browser version.
from webdriver_manager.chrome import ChromeDriverManager

# replacing the executable_path with the ChromeDriverManager()
# for automatically check the version and install.
# No need for locally installed chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.github.com")
print(driver.title)
driver.maximize_window()
driver.close()

