from selenium.webdriver.common.by import By # 要素を指定するためのByを使えるようにする
import time                                 # 時間を扱うためのライブラリ（機能が詰まった道具箱）を使えるようにする
from dotenv import load_dotenv              # .envファイルを読み込む準備
import os                                   # OS(オペレーティングシステム(Windouws))の機能と対話するためのライブラリを使えるようにする
from selenium_driver import SeleniumDriver  # 作成したselenium_driver.pyをインポートする

# .envファイル（環境変数）の読み込み
load_dotenv()                               # os.getenv=指定された名前の環境変数の値を取得する

# os.getenvで指定した名前の環境変数の値を取得
LOGIN_ADDLES = os.getenv("LOGIN_ADDLES")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

# 定数定義(プログラム中に変更しない値)
BASE_URL = "https://libecity.com/signin"                                  # この部分はプログラムの実行中に値が変わることが意図されていないもの
MAIL_INPUT_LOCATOR = (By.XPATH, '//input[@placeholder="メールアドレス"]')  # pythonでは「定数」として扱われる
PASS_INPUT_LOCATOR = (By.XPATH, '//input[@placeholder="パスワード"]')      # pythonの定数は全て大文字のスネークケースで命名する
LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#contents_wrap > main > div.login_tab_box.is_show > section > p.form_data_area.text-center > button")
HOME_BUTTON_LOCATOR = (By.XPATH, '//*[@id="tool_bar"]/div[1]/ul/li[1]/a') # 大文字で書くことで可読性を向上させ、定数と示すことで意図しない変更を防ぐ

# メインの処理
def main():
    """ 指定したURLに自動でログインし、10秒後にブラウザを閉じるメイン処理"""
    # SeleniumDriverクラスのインスタンスを作成
    # これにより、__init__メソッドが呼び出され、chromeブラウザが起動
    # browserはインスタンス変数、この変数をtry以下のコードの中で使用
    browser = SeleniumDriver(timeout=10)  
                                    
    # try...except...finally構文
    # try=実行
    try:
        # 1. ページを開く
        browser.open_page(BASE_URL)

        # 2. メールアドレスとパスワードの入力
        browser.input_text(MAIL_INPUT_LOCATOR, LOGIN_ADDLES)
        browser.input_text(PASS_INPUT_LOCATOR, LOGIN_PASSWORD)
        
        # 3. ログインボタンをクリック
        browser.click_element(LOGIN_BUTTON_LOCATOR)
        
        # 4. ログイン後のページ表示まで待機,ログインが成功する場合、ホームボタンがブラウザに表示される
        browser.wait_for_element_visibility(HOME_BUTTON_LOCATOR)
        
        # 5. ログイン後のブラウザを目視で確認するための待機時間
        time.sleep(10)
        
    except Exception as e:
        # tryブロック内でエラーが発生した場合、実行されるブロック
        print(f"エラーが発生しました: {e}")
    finally:         
        # try実行の成否に関わらず実行されるブロック
        # ブラウザを閉じる
        browser.quit()

# このスクリプトが直接実行された場合にmain()関数を呼び出す
# ターミナルで python LibeAutoLogin.pyとコマンド入力して実行＝直接実行
# 直接実行することで__name__ = "__main__"となる
# if __name__ = "__main__"が「真」となり、main()が実行される
# これにより、他のファイルからモジュールとしてインポートされた場合はmain()は自動実行されない
if __name__ == "__main__": 
    main()




# pythonはシステム(WSL全体)のpythonと仮想環境のpythonの2種類がある
# 仮想環境のpythonはプロジェクト専用に切り分けた環境
# 他のプロジェクトに影響を与えない、プロジェクト毎にライブラリのバージョン変更できるなどのメリットから仮想環境のpythonを選択する方が良い
# 仮想環境のpythonの構築手順
# cd repos/libe_auto_login プロジェクトフォルダに移動
# python3 -m venv venv 仮想環境を作成
# source venv/bin/activate 仮想環境を有効化
# pip install selenium webdriver-manager 必要なライブラリをインストール
# python LibeAutoLogin.py 実行
