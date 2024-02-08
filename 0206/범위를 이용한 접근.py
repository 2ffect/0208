import numpy as np

ar = np.arange(10)
br = ar.reshape((2, -1))

# print(ar[1:4])
# # 출력 : [1 2 3]
# print(ar[5:])
# # 출력 : [5 6 7 8 9]
# print(ar[:4])
# # 출력 : [0 1 2 3]
# print(ar[:])
# # 출력 : [0 1 2 3 4 5 6 7 8 9]

# 2 차원 배열에서의 접근
print(br)
print(br[1][1:3])
# 출력 : [6 7]
print(br[1]) 
# 출력 : [5 6 7 8 9] / 1 행 전체
print(br[:,1])
# 출력 : [1 6]       / 1 열 전체