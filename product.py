# クラス定義
class Product:
    # __init__で商品名と在庫数のインスタンス変数を作成
    def __init__(self, name, stock):
        self.name = name # "りんご"を受け取ってインスタンス変数に代入
        self.stock = stock # 5を受け取ってインスタンス変数に代入
    
    # 在庫をamount分増やす
    def add_stock(self, amount):
        self.stock += amount # +=はself.stock = self.stock(5) + amount(5)と同義
    
    def show_stock(self):
        print(f"{self.name}の在庫は{self.stock}です") # self.stockにはクラス内の関数を反映した数字＝10が代入されている
      

apple = Product("りんご", 5) # __init__にりんごと5を渡してインスタンスを作成
apple.add_stock(5) # __init__で作成したインスタンスに5をプラスする
apple.show_stock()
