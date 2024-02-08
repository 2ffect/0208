import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel('C:/DX_DATA/dx2_code/django/0208/data/data/excel.xlsx')
print(df)

# 엑셀 파일로 저장
writer = pd.ExcelWriter("sample.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name="excel")
writer.close()

# read_html은 list를 리턴 하므로 인덱스를 이용해 원하는 테이블을 선택해야 한다.
li = pd.read_html('https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B5%AC%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D')
print(li[1])
