# 날짜 및 시간 관련 패키지
import datetime
import numpy as np
ar = np.arange(1, 1000000)
# 현재 시간을 저장
start = datetime.datetime.now()
ar = ar * 10
# 현재 시간을 저장
end = datetime.datetime.now()
print(start, end)
# 2024-02-06 12:39:02.822599 (시작한 시간) 
# 2024-02-06 12:39:02.823783 (끝난 시간)