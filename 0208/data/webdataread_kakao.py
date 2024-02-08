import pandas as pd
import urllib.request

# 웹에서 데이터 가져오기
result = urllib.request.urlopen("https://www.kakao.com")
print(result.read())




# # 웹에서 데이터 가져오기
# result = urllib.request.urlopen("https://search.hani.co.kr/search?searchword=사이버가수아담")
# print(result.read())

