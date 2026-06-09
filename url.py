from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

url = input("Enter URL: ")

driver.get(url)
time.sleep(3)

driver.save_screenshot("screenshot.png")
print("Screenshot saved!")

driver.quit()