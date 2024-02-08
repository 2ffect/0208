import numpy as np

ar = np.arange(10)

br = ar[[1, 3, 5, 7]]
print(br)
# 출력 : [1 3 5 7]
br[0] = 15700
print(br)
# 출력 : [15700 3 5 7]
print(ar)
# 출력 : [0 1 2 3 4 5 6 7 8 9]

# Fancy Indexing은 데이터를 복사하여 사용하기 때문에 원본에 영향이 없다.


matrix = ar.reshape((2, -1))
print(matrix)
# 출력 : [[0 1 2 3 4]
#         [5 6 7 8 9]]

print(matrix[:,0])
# 출력 : [0 5]

# 2 차원 배열에서 list를 이용해 행 번호나 열 번호를 지정하면 2 차원 배열이 생성된다.
print(matrix[:,[0]])
# 출력 : [[0]
#         [5]]

# numpy의 ndarray나 pandas의 DateFrame에서 하나의 열을 선택할 때
# list를 활용하는 경우 구조를 유지하기 위함이다.