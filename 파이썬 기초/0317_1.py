# #상속 사용하기
# #빵 클래스 만들어보기
# class Bread:
#     def __init__ (self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
    
#     def buy(self):
#         if self.stock <= 0:
#             print("재고가 없습니다.")
#         else:
#             self.stock -= 1
#             print("구매가 완료되었습니다.")
#     def bake(self, stock):
#         self.stock += stock
#         print(f'{self.name}을(를) {stock}개 만들었습니다.')
            
# # 빵 클래스 상속받아 붕어빵 클래스 만들기
# class FishShapedBun(Bread):
#     def __init__(self, name, price, stock, inside):
#         super().__init__(name, price, stock)
#         self.inside = inside
    
#     def buy(self):
#         super().buy()
#         print(f"맛있는 {self.inside} 붕어빵")
        
#     def bake(self, stock):
#         return 

# bread = Bread("식빵", 3000, 3)
# bread.bake(5)
# for i in range(10):
#     bread.buy()

# fishShapedBun = FishShapedBun("붕어빵", 1000, 5, "팥")
# fishShapedBun.bake(3)
# for i in range(7):
#     fishShapedBun.buy()
    
# print(isinstance(bread, Bread))
# print(isinstance(bread, FishShapedBun))
# print(isinstance(fishShapedBun, Bread))
# print(isinstance(fishShapedBun, FishShapedBun))

# print("=====================================")

# print(type(bread) == Bread)
# print(type(bread) == FishShapedBun)
# print(type(fishShapedBun) == Bread)
# print(type(fishShapedBun) == FishShapedBun)


class Office:
    def __init__(self, pencil, eraser, ruler):
        self.pencil = pencil
        self.eraser = eraser
        self.ruler = ruler
    
    def have(self, pen=None):
        if pen is not None:
            print(f'연필: {self.pencil}, 지우개: {self.eraser}, 자: {self.ruler}, 펜: {pen}')
        else:
            print(f'연필: {self.pencil}, 지우개: {self.eraser}, 자: {self.ruler}')

class PencilCase(Office):
    def __init__(self, pencil, eraser, ruler, pen):
        super().__init__(pencil, eraser, ruler)
        self.pen = pen
    
    def have(self, include_pen=False):
        if include_pen:
            print(f'연필: {self.pencil}, 지우개: {self.eraser}, 자: {self.ruler}, 펜: {self.pen}')
        else:
            print(f'연필: {self.pencil}, 지우개: {self.eraser}, 자: {self.ruler}')


o = Office(3, 2, 1)
p = PencilCase(5, 6, 0, 4)


o.have()       
o.have(2)   
p.have()          
p.have(True)       

