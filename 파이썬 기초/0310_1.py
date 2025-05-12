#간단한 함수 만들기
def say_hello_5times():
    for i in range(5): #0~4 총 5회
        print("Hello")

#함수에 매개변수 만들기
def say_hello_n_times(n, str):
    for i in range(n):
        print(str)
        
#가변 매개변수 활용하기
def say_strings_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
 
#기본 매개변수 활용하기
def say_strings_d_times(*values, d=3):
    for i in range(d):
        for value in values:
            print(value)
        print()                

def function_ex1(*values, num=0):
    print("num = ", num)
    print("values: ")
    for value in values:
        print(value)
function_ex1("선린", "솦과", num=1)

def function_ex2(num = 0, *values):
    print("num = ", num)
    print("values: ")
    for value in values:
        print(value)
function_ex2("선린", "솦과", 1)

#say_hello_5times()

#say_hello_n_times(10, "안녕하세요")

#say_strings_n_times(4, "선린인터넷고등학교", "소프트웨어과", "석성택")

#say_strings_d_times("안녕하세요", "반갑습니다", d=4)


