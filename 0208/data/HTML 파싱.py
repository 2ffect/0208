# beautifulsoup4 설치하기
# HTML을 XML로 변환해서 파싱한다.
# 모듈을 import 할 때 bs4 를 import 한다.
import bs4, requests

resp = requests.get("https://search.hani.co.kr/search?searchword=%ED%8F%AC%EC%8A%A4%EC%BD%94")
html = resp.text
# print(html)

# html 파싱
bs = bs4.BeautifulSoup(html, 'html.parser')
# print(bs.body.span.get_text()) 데이터 1개만 불러올 수 있어서 잘 안씀
tags = bs.select('article > a > div.article-list-cont > strong')
for tag in tags:
    print(tag.getText())


resp = requests.get("https://weather.go.kr/w/obs=climate/land/")
html = resp.text
# print(html)

# html 파싱
bs = bs4.BeautifulSoup(html, 'html.parser')
# print(bs.body.span.get_text()) 데이터 1개만 불러올 수 있어서 잘 안씀
tags = bs.select('article > a > div.article-list-cont > strong')
for tag in tags:
    print(tag.getText())



# find 함수
# find(태그, attributes, recursive, text, limit, keywords)
# 태그에는 찾고자 하는 태그를 설정
# attributes 에는 태그 중 트정 속성의 값만 가져오고자 할 때 사용
# recursive 는 False이면 최상위 태그에서만 ㅊ자고 True이면 하위로 들어가면서도 찾음
# 일치하는 태그 1개를 찾는다. 여러개를 찾기 위해서는 find_all을 사용

# select 함수
# 선택자를 이용해서 찾아오는 함수.


# bs4.element.Tag
# find와 select의 결과는 Tag클래스의 list, getText()를 호출하면
# 태그가 감싸고 있는 텍스트를 가져올 수 있고 get('속성이름')은 속성의 값을 가져올 수 있다.
# 선택자는 앞에서부터 생략도 가능하다.

#sp_nws_all4 > div.news_wrap.api_ani_send > div > div.news_contents > a.news_tit

