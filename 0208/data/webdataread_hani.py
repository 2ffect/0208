import pandas as pd
import urllib.request
# 한글을 인코딩
from urllib.parse import quote
keyword = quote("사이버가수아담")

# 웹에서 데이터 가져오기
result = urllib.request.urlopen("https://search.hani.co.kr/search?searchword=" + keyword)
print(result.read())

