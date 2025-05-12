#파이썬 자료형 확인하기
# num_i = 45
# num_f = 20.45
# str_n = "석성택"
# list_n = [4, 5, 6, 3, 2]
# dict_n = {'name': '석성택'}

# print(type(num_i))
# print(type(num_f))
# print(type(str_n))
# print(type(list_n))
# print(type(dict_n))

# 클래스 만들어보기
# class Student:
#     count = 0
#     students = []
    
#     @classmethod
#     def print(cls):
#         print(f'이름\t국어\t수학\t영어') 
#         for student in cls.students:
#             print(student.to_string())
    
#     def __init__(self, name, korean, math, english):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
        
#         Student.count += 1
#         Student.students.append(self)
        
        
#     def get_sum(self):
#         return self.korean + self.math + self.english
    
#     def get_average(self):
#         return self.get_sum() / 3    
    
#     def to_string(self):
#         return f'{self.name}\t{self.korean}\t{self.math}\t{self.english}\t{self.get_sum()}\t{self.get_average()}'
    
# student1 = Student('석성택', 100, 100, 100)    
# student2 = Student('이건우', 0, 100, 0)    
# student3 = Student('김도현', 0, 0, 0)

# print(student.get_sum())
# print(student.to_string())

# Student.print()

class Computer:
    users = []
    
    @classmethod
    
    def __init__(self, name, keyboard, mouse, cpu, gpu, monitor, game):
        self.name = name
        self.keyboard = keyboard
        self.mouse = mouse
        self.cpu = cpu
        self.gpu = gpu
        self.monitor = monitor
        self.game = game

    def print(cls):
        print(f'유저명\t키보드\t마우스\tcpu\tgpu\t모니터\t주로 하는 게임')
        for user in cls.users:
            print(user.boast(), end="")
            print(user.playing())

    def playing(self):
        return f'{self.game}'
        
    def boast(self):
        return f'{self.keyboard} {self.mouse} {self.cpu} {self.gpu} {self.monitor}'
    
user1 = Computer('qwer', 'Rainy75', 'Logitech G403 HERO', 'Intel i5-13700k', 'rtx 3080' , 'Dell 27인치 165hz', "valorant")
user2 = Computer('asdf','다얼유 A104 PRO 8K', 'Logitech 지슈라1', 'Intel i7- 8900k', 'rtx 4060 TI' , 'Dell 27인치 165hz', "TFT")
user3 = Computer('zxcv', 'Apex pro TKL GEN', 'Logitech 지슈라2', 'Intel i9-14700k', 'rtx 5080' , 'Dell 27인치 165hz', "OVERWATCH")

# print(setting.boast())
# print(setting.playing()) 