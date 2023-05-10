"""This is a bot program for cookie clicker that I'm making to learn how to use Selenium."""

from time import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

### I need to program the bot to click as fast as possible
# Every 5 seconds, the bot should check to see which upgrades it can afford.
# The more expensive upgrade should be purchased.###

money = int(driver.find_element(By.CSS_SELECTOR, "[id='money']").text)
cookie = driver.find_element(By.CSS_SELECTOR, "[id='cookie']")
cursor = driver.find_element(By.CSS_SELECTOR, "[id='buyCursor']")
cursor_text = int((cursor.find_element(By.TAG_NAME, "b").text).split(" ")[2])
grandma = driver.find_element(By.CSS_SELECTOR, "[id='buyGrandma']")
grandma_text = int((grandma.find_element(By.TAG_NAME, "b").text).split(" ")[2])
shipment = driver.find_element(By.CSS_SELECTOR, "[id='buyShipment']")
shipment_text = (shipment.find_element(By.TAG_NAME, "b").text).split(" ")[2]
shipment_text = int(shipment_text.replace(",", ""))
alchemy_lab = driver.find_element(By.CSS_SELECTOR, "[id='buyAlchemy lab']")
alchemy_lab_text = (alchemy_lab.find_element(By.TAG_NAME, "b").text).split(" ")[3]
alchemy_lab_text = int(alchemy_lab_text.replace(",", ""))
# alchemy_lab_text = alchemy_lab_text.replace(",", "")
print(cursor_text)
print(grandma_text)
print(shipment_text)
print(alchemy_lab_text)
# I skipped factory and mine

def run_game():
    """This function has all the procedural code and the AI for the bot."""
    number_of_seconds = 5
    start_time = time()
    while time() - start_time < number_of_seconds:
        cookie.click()
    
    run_game()

driver.quit()
# run_game()
