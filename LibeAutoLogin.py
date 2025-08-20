from selenium import webdriver
from selenium.webdriver.common.by import By # 要素を指定するためのコード Byをインポートする
from selenium.webdriver.support.ui import WebDriverWait #指定したい要素が表示されるまで待つコード
from selenium.webdriver.support import expected_conditions as EC #指定したい要素が表示されるまで待つコード
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv # .envファイルを読み込む準備
import os

# .envファイル（環境変数）の読み込み
load_dotenv()
login_addles = os.getenv("LOGIN_ADDLES")
login_password = os.getenv("LOGIN_PASSWORD")

# chromeを自動で起動
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #driverはブラウザを扱えるように接続してくれるもの

# 任意のページを開く（リベシティのログイン画面）
driver.get("https://libecity.com/signin") #getメソッド+（）開きたいページのURLを引数に指定する
wait = WebDriverWait(driver, 10) #ページが開くまで10秒待機

# メールアドレスの自動入力
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="メールアドレス"]')))
mail_element = driver.find_element(By.XPATH, '//input[@placeholder="メールアドレス"]')
mail_element.send_keys(login_addles)

# パスワードの自動入力
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="パスワード"]'))) #ある要素が表示されるまで待機
pass_element = driver.find_element(By.XPATH, '//input[@placeholder="パスワード"]') # 要素を指定して変数に代入
pass_element.send_keys(login_password)

# ログインボタンのクリック
login_button = driver.find_element(By.CSS_SELECTOR, "#contents_wrap > main > div.login_tab_box.is_show > section > p.form_data_area.text-center > button")
login_button.click()

# ログイン後の確認のための待機時間
time.sleep(10) #待機時間の設定 ()内の数字で秒数指定

#アプリの終了（直前で設定した待機時間経過後）
driver.quit()



# pythonはシステム(WSL全体)のpythonと仮想環境のpythonの2種類がある
# 仮想環境のpythonはプロジェクト専用に切り分けた環境
# 他のプロジェクトに影響を与えない、プロジェクト毎にライブラリのバージョン変更できるなどのメリットから仮想環境のpythonを選択する方が良い
# 仮想環境のpythonの構築手順
# cd repos/libe_auto_login プロジェクトフォルダに移動
# python3 -m venv venv 仮想環境を作成
# source venv/bin/activate 仮想環境を有効化
# pip install selenium webdriver-manager 必要なライブラリをインストール
# python LibeAutoLogin.py 実行
