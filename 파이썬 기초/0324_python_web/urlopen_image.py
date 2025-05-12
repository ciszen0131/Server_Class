from urllib.request import urlopen
from html.parser import HTMLParser

# HTMLParser 오버라이드
class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)
                
# 이미지 파싱 함수 만들기
def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result) #list comprehension => 리스트 표현식
    return dataSet

def main():
    url = "https://www.google.co.kr/"
    
    with urlopen(url) as open:
        charset = open.headers.get_param('charset')
        data = open.read().decode(charset)
        
    dataSet = parse_image(data)
    print('\n'.join(sorted(dataSet)))
    
if __name__ == '__main__':
    main()