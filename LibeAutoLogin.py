from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# chromeを自動で起動
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 任意のページを開く
driver.get("https://google.com")
time.sleep(10)