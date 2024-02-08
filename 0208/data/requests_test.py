import requests

resp = requests.get("http://httpbin.org/get")
print(resp.text)


# 파라미터 만들기
param = {"id" : "itstudy", "name":"군계", "age":53}
# 파라미터와 함께 post 요청
resp = requests.post('http://httpbin.org/post', data = param)
print(resp.text)

# 이미지 파일 다운로드
imageurl = "https://img.hankyung.com/photo/202011/AA.24402414.1.jpg"
# 저장할 파일 이름
filename = "test.jpg"

try:
    # 다운로드
    resp = requests.get(imageurl)
    # 파일에 저장
    with open(filename, "wb") as h:
        # 다운로드 받은 내용을 bytes 로 리턴
        img = resp.content
        # 파일에 저장
        h.write(img)
except  Exception as e:
    print(e)
    