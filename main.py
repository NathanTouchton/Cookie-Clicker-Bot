"""This is a bot program for cookie clicker that I'm making to learn how to use Selenium."""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.python.org/")
# Extract date and name of upcoming events and print them to a nested dict

thing = driver.find_element(by="class name", value="mw-page-title-main")
print(thing.text)

driver.quit()
