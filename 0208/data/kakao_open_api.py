# kakao open api 가져오기
import requests, json

# url 만들기
url = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=PM9&rect=126.95,37.55, 127.0, 37.60'
# 헤더 설정
headers = {'Authorization': 'KakaoAK {}'.format('8ceedf773a5cef215e57d827a5a77ec9')}

# 데이터 다운로드
data = requests.post(url, headers=headers)
# 다운로드 받은 문자열 확인
# print(data.text)

# JSON 문자열을 python의 자료구조로 변경
result = json.loads(data.text)
# print(result)

# documents 키의 데이터 가져오기
documents = result['documents']
for doc in documents:
    print(doc['place_name'], doc['address_name'])

# 데이터베이스에 저장 (MySQL 연동)
import pymysql

con = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'dxjh',
    password = 'yjkk~1606',
    db = 'mango',
    charset = 'utf8'
)

print(con)

cursor = con.cursor()

# 테이블 생성구문 
# cursor.execute("create table phamacy(placename varchar(30), addressname varchar(200))")

#파싱한 데이터 순회
for doc in documents:
    cursor.execute("insert into phamacy(placename, addressname) values(%s, %s)", (doc["place_name"], doc["address_name"]))
# commit
con.commit()

# SELECT의 경우 execute 다음 커서를 이용해 fetch_one 이나 fetachall()을 호출해 튜플을 가져와 읽는다.
