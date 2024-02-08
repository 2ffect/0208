import numpy as np

# 데이터 타입확인과 형 변환
ar = np.array([1, "2", 3]) # 숫자와 문자열을 가지고 배열을 생성 > 문자
print(ar.dtype)
# 출력 : <U11

br = np.array([1, 2.3, 3]) # 정수와 실수를 가지고 배열을 생성 > 실수
print(br.dtype)
# 출력 : float64

# ar 배열의 자료형을 정수로 형 변환
cr = ar.astype(np.int32)
print(cr.dtype)
# 출력 : int32
