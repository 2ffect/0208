import numpy as np

ar = np.arange(10)

# 홀수이거나 4의 배수인 데이터만 출출
print(ar[(ar % 2 == 1) | (ar % 4 == 0)])
# 홀수인 1 3 5 7 9 와 4의 배수인 4 8 이 True 이므로
# 출력 : [0 1 3 4 5 7 8 9]