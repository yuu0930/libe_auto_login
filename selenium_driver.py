from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumDriver:
    def __init__(self, timeout=10): # WebdriverとWebdriverWaitを初期化する
        self.driver = webdriver.chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, timeout)

    def open_page(self, url):
        self.driver.get(url) # 指定したURLを開く
    
    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator)) # 要素が表示されるのを待ってからテキストを入力する
        element.send_keys(text) # 指定したキーを送信する
        
    def click_button(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator)) # 要素がクリック可能になるのを待ってからクリックする
        element.click() # ボタンをクリックする
        
    def quit(self):
        self.driver.quit() # ブラウザを閉じる