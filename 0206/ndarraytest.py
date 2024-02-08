# 날짜 및 시간 관련 패키지
import datetime
li = range(1, 1000000)

# 현재 시간을 저장
start = datetime.datetime.now()
# 모든 요소에 10을 곱하기
for i in li:
    i = i *10
# 현재 시간을 저장
end = datetime.datetime.now()

print(start, end)
# 2024-02-06 12:35:01.494021(시작한 시간) 
# 2024-02-06 12:35:01.539072(끝난 시간)