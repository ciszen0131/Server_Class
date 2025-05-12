import random

#함수 결과 반환
def compare_num(n):
    if n>0:
        return "Positive"
    elif n == 0:
        return "Zero"
    return "Negative"
    
# print(compare_num(0))

def if_same(a, n):
    if n > a:
        print("Down")
    elif n < a:
        print("Up")
    else:
        return False
    return True
    

# a = random.randrange(1, 100)
# while True:
#     print("==========")
#     n = int(input("숫자 입력:"))
#     b = if_same(a, n)
#     if not b:
#         break
# print("정답입니다!")

#매개변수를 함수로 받아 실행
def call_10_times(func):
    for i in range(10):
        func()
        
def say_love():
    print("I love python")
    
# call_10_times(say_love)

#map(), filter() 함수 활용
def super(num):
    return num ** 2

def is_big_10(num):
    return num>10


# output_map = map(super, num_list)
# print("map:", list(output_map))

# output_filter = filter(is_big_10, num_list)
# print("filter: ", list(output_filter))

print("map: ", list(map(lambda n: n ** 2, [1, 3, 9, 27, 81])), "\nfilter: ", list(filter(lambda n: n>10, [1, 3, 9, 27, 81])))