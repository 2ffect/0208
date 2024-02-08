import numpy as np

# 1차원 배열 [0,1,2, ... ,19] 생성
ar = np.arange(20)  
print(ar)
# 출력 : [0 1 2 3 4 5 6 7 8 9]

# 같은 요소를 가지고 2x5 배열로 변형
br = ar.reshape((4, 5))
print(br)
# 출력 : [[ 0  1  2  3  4]
#         [ 5  6  7  8  9]
#         [10 11 12 13 14]
#         [15 16 17 18 19]]

cr = br.flatten()
print(cr)