from selenium import webdriver
# importing GeckoDriverManager() from webdriver_manager
# it will manage Gecko driver automatically with the
# correspoding Firefox browser version.
from webdriver_manager.firefox import GeckoDriverManager

# !!! executable_path MUST be provided for GeckoDriverManager() !!!
# using GeckoDriverManager() for automatically check the version and install.
# No need for locally installed gecko driver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.github.com")
driver.maximize_window()
print(driver.title)
driver.close()
