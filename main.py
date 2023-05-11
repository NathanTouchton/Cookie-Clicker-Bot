"""This is a bot program for cookie clicker that I'm making to learn how to use Selenium."""

from time import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")
body = driver.find_element(By.TAG_NAME, "body")
### I need to program the bot to click as fast as possible
# Every 5 seconds, the bot should check to see which upgrades it can afford.
# The more expensive upgrade should be purchased.###

cookie = driver.find_element(By.CSS_SELECTOR, "[id='cookie']")
cursor = driver.find_element(By.CSS_SELECTOR, "[id='buyCursor']")
cursor_text = (cursor.find_element(By.TAG_NAME, "b").text).split(" ")[2]
grandma = driver.find_element(By.CSS_SELECTOR, "[id='buyGrandma']")
grandma_text = (grandma.find_element(By.TAG_NAME, "b").text).split(" ")[2]
factory = driver.find_element(By.CSS_SELECTOR, "[id='buyFactory']")
factory_text = (factory.find_element(By.TAG_NAME, "b").text).split(" ")[2]
mine = driver.find_element(By.CSS_SELECTOR, "[id='buyMine']")
mine_text = (mine.find_element(By.TAG_NAME, "b").text).split(" ")[2]
mine_text = mine_text.replace(",", "")
shipment = driver.find_element(By.CSS_SELECTOR, "[id='buyShipment']")
shipment_text = (shipment.find_element(By.TAG_NAME, "b").text).split(" ")[2]
shipment_text = shipment_text.replace(",", "")
alchemy_lab = driver.find_element(By.CSS_SELECTOR, "[id='buyAlchemy lab']")
alchemy_lab_text = (alchemy_lab.find_element(By.TAG_NAME, "b").text).split(" ")[3]
alchemy_lab_text = alchemy_lab_text.replace(",", "")

upgrades = {
    alchemy_lab_text: alchemy_lab,
    shipment_text: shipment,
    mine_text: mine,
    factory_text: factory,
    grandma_text: grandma,
    cursor_text: cursor,
}

ignored_exceptions = (StaleElementReferenceException)

def run_game():
    ###I got rid of theh errors, but I can't figure out why it isn't buying upgrades.###
    """This function has all the procedural code and the AI for the bot."""
    number_of_seconds = 5
    start_time = time()
    while time() - start_time < number_of_seconds:
        money = int(body.find_element(By.CSS_SELECTOR, "[id='money']").text)
        cookie.click()
    # if money is greater than any of the items in upgrades, then buy the most expensive
    for key, value in upgrades.items():
        if money > int(key):
            try:
                value.click()
            except StaleElementReferenceException:
                WebDriverWait(
                    driver=driver,
                    timeout=10,
                    ignored_exceptions=ignored_exceptions
                ).until(EC.presence_of_element_located((By.ID, "game")))
    run_game()

run_game()
# driver.quit()
