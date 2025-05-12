from urllib.request import urlopen

result = urlopen("https://papago.naver.com/")
print(result.read(1000).decode("utf-8"))