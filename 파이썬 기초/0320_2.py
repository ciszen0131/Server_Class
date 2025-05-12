# 예외 처리
try: 
    num = int(input("정수 입력: "))
    raise IndexError()
except Exception as exception:
    print("입력은 숫자로만 이루어져야 합니다.")
    print(f'{exception}, {type(exception)}')
else:
    print(f'{num}의 제곱: {num ** 2}')
finally:
    print("프로그램 종료")