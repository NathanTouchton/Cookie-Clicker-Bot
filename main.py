"""This is a bot program for cookie clicker that I'm making to learn how to use Selenium."""

# from pprint import pprint
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.python.org/")
# Extract date and name of upcoming events and print them to a nested dict

element = driver.find_element(By.CLASS_NAME, "event-widget")
times = element.find_elements(By.TAG_NAME, "time")
event_names = element.find_elements(By.CSS_SELECTOR, "a:not([title='More Events'])")

for e in event_names:
    print(e.text)

driver.quit()

###CLass: medium-widget event-widget last
# I need to find the timedate value and text from the time tags.###
