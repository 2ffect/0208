import numpy as np

# 배열 생성
ar = np.arange(10)
print(ar)
# 출력 : [0 1 2 3 4 5 6 7 8 9]

# 범위를 이용한 배열 생성
br = ar[0:4]
print(br)
# 출력 : [0 1 2 3]

br[0] = 42
print(br)
# 출력 : [42 1 2 3]
print(ar)
# 출력 : [42 1 2 3 4 5 6 7 8 9]

# ar을 직접적으로 수정하지 않았지만 ar의 배열이 수정 됨