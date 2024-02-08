# 사용할 URL : https://www.hankyung.com/feed/sports
# 파싱 방법
import xml.etree.ElementTree as et
import urllib.request

# 데이터 읽어오기
url = "https://www.hankyung.com/feed/sports"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
# print(response.read())


# 메모리에 펼치기
tree = et.parse(response)
print(tree)
# 루트 찾기
# xroot = tree.getroot()
# print(xroot)


# # 특정 태그의 데이터 가져오기
# items = xroot.findall('title')

# # 태그가 여러개 나올 수 있으므로 반목문 수행
# for node in items:
#     node.find('title').text # 테그 안의 데이터
