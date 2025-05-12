class bread:
    def __init__ (self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def buy(self):
        if self.stock <= 0:
            print("재고가 없습니다.")
        else:
            self.stock -= 1
            print("구매가 완료되었습니다.")
            
# 빵 클래스 상속받아 붕어빵 클래스 만들기
class FishShapedBun(bread):
    def __init__(self, name, price, stock, inside):
        super().__init__(name, price, stock)
        self.inside = inside
    
    def buy(self):
        super().buy()
        print(f"맛있는 {self.inside} 붕어빵")

# bread1 = bread("식빵", 3000, 3)
# for i in range(6):
#     bread1.buy()

fishShapedBun = FishShapedBun("붕어빵", 1000, 5, "팥")
for i in range(6):
    fishShapedBun.buy()