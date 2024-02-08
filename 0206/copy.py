import numpy as np

ar = np.arange(10)

# 데이터를 복사하여 br에 대입하므로 br을 수정해도 원본에 영향이 없다.
br = ar[0:4].copy()

br[0] = 42
print(br)
# 출력 : [42 1 2 3]
print(ar)
# 출력 : [0 1 2 3 4 5 6 7 8 9]

# 위 처럼 데이터를 가져오는 과정에서 .copy()를 사용하면 원본 데이터에 영향을 주지 않고
# br의 인덱스를 수정할 수 있다.