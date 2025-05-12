# # 정삼각형 클래스 만들기
# class ETriangle:
#     def __init__(self, length):
#         self.__length = length
#     def get_length(self):
#         return self.__length
#     def set_length(self, length):
#         if length <= 0:
#             print("길이는 0보다 커야합니다.")
#         else:
#             self.__length = length
#     @property 
#     def length(self):
#         return self.__length
    
#     @length.setter
#     def length(self, length):
#         if length <= 0:
#             raise ValueError("길이는 0보다 커야합니다.")
#         self.__length = length

# # 정삼각형 클래스 사용해보기
# triangle = ETriangle(5)

# #print(triangle.__length)
# triangle.__length = 3
# print(triangle.get_length())
# triangle.set_length(8)
# triangle.set_length(-3)
# print(triangle.get_length())

# print("=====================================")

# triangle.length = 0
# print(triangle.length)
# triangle.length = -3
# print(triangle.length)



class Video:
    def __init__(self, verified, title, length):
        self.__verified = verified
        self.title = title
        self.length = length
    @property
    def verified(self):
        return self.__verified
    @verified.setter
    def verified(self, verified):
        if verified != True:
            raise ValueError("검증되지 않았습니다.")
        self.__verified = True
        print("검증되었습니다.")

video = Video(False, "파이썬", 120)
video.verified = True
print(video.verified)
video.verified = False
print(video.verified)