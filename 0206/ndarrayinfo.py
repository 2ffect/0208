# 배열의 생성과 정보 확인
import numpy as np       # numpy 모듈을 np라는 이름으로 가져와 사용
ar = np.array([1, 2, 3]) # list를 이용해 ndarray를 생성

# ndim 차원을 확인
print(ar.ndim) # 출력 : 1 (1차원) 단순한 리스트 이므로
# shape 각 차원의 데이터 개수를 튜플로 리턴
print(ar.shape) # 출력 : (3,) 튜플로 출력되야 하기때문

# 리스트 안에 리스트가 있을경우 2차원
table = np.array([[1, 2, 3], [4, 5, 6]])
print(table.ndim) # 출력 : 2 (2차원)
print(table.shape) # 출력 : (2,3) 2행 3열의 배열

# 데이터 1개의 자료형
print(table.dtype) # 출력 : int32
