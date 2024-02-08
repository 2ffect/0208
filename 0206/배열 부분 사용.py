import numpy as np

ar = np.arange(10)
br = ar.reshape((2, -1))

print(ar) # 1차원 배열
# 출력 : [0 1 2 3 4 5 6 7 8 9]
print(br) # 2차원 배열
# 출력 : [[0 1 2 3 4]
#         [5 6 7 8 9]]

# 1차원 배열에서 요소 접근
print(ar[0])
# 출력 : 0 / 첫번째 데이터
print(ar[-1])
# 출력 : 9 / 마지막 데이터

# 2차원 배열에서 요소 접근
print(br[0,2]) 
# 출력 : 2 / 첫번째 행의 3번째 데이터
print(br[0][2])
# 출력 : 2 / 첫번째 행의 3번째 데이터
