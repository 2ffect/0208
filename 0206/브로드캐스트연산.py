import numpy as np

ar = np.arange(10)
br = ar.reshape((2, -1))


print(br)
# 출력 :[[0 1 2 3 4]
#        [5 6 7 8 9]]

# 브로드캐스트 연산
# 차원이 다른 경우 차원을 순회하면서 연산을 수행한다.
print(br + 10)
# 출력 :[[10 11 12 13 14]
#        [15 16 17 18 19]]

# numpy의 ndarray와 논리 연산을 수행하면 bool 배열이 리턴된다.
print(ar == 3)
# 출력 : [False False False  True False False False False False False]

# 인덱스의 bool 배열을 대입하면 True인 데이터만 추출된다.
print(ar[ar % 2 == 1])
# 1 3 5 7 9 값이 True 이므로 False 값인 0 2 4 6 8 을 제외하고 출력
# 출력 : [1 3 5 7]

data = np.array([100, 200, 300, 400, 500])
print(br + data)
# 출력 : [[100 201 302 403 504]
#         [105 206 307 408 509]]

# 이 경우 차원의 열의 개수가 5개 씩으로 동일해 연산이 수행 됐지만
# 열의 개수가 다른경우 연산이 수행되지 않는다.