# %%

import numpy as np
import pandas as pd
from sklearn import datasets
import os

# %%
# 클립보드의 내용을 읽어오기
pd.read_clipboard()

# %%
# 자주 사용하는 데이터 셋
# => scikit-learn에서 제공하는 데이터 셋

iris = datasets.load_iris()
print(type(iris))
print("----------------------------------------------------------")
print(dir(iris))
print("----------------------------------------------------------")
print(iris.keys())
print("----------------------------------------------------------")
print(type(iris.data))

# %% [markdown]
# fwf 파일 읽기

# %%
df = pd.read_fwf("C:/DX_DATA/dx2_code/django/0208/data/data/data_fwf.txt",
                 widths = (10,2,5),
                 names = ('날짜','이름','가격'),
                 encoding = 'utf-8')


print(df)

# %% [markdown]
# CSV 파일 읽기

# %%
# item.csv 파일 읽기
item = pd.read_csv("C:/DX_DATA/dx2_code/django/0208/data/data/item.csv",
                   header = None, names = ['제품이름','수량','가격'])
print(item)
print(item.info())


# %% [markdown]
# 큰 파일을 읽을 때의 코드

# %%
i = 0

while True:
    try:
        parser = pd.read_csv("C:/DX_DATA/dx2_code/django/0208/data/data/item.csv",
                             header = None, nrows =2 , skiprows = i*2,names = ['제품이름','수량','가격'])
        
        if len(parser) == 0:
            break
        
        print(parser)
        
        print('---------------------------------------------------')
        i = i + 1
        
        
        
    except:
        break

# %%
parser = pd.read_csv("C:/DX_DATA/dx2_code/django/0208/data/data/item.csv", header = None,
                     chunksize = 2)

for piece in parser:
    print(piece)

# %% [markdown]
# 구분자 바꾸기 설정

# %%
gapminder = pd.read_csv('C:/DX_DATA/dx2_code/django/0208/data/data/gapminder.tsv',
                        sep = '\t')

gapminder

# %%
import csv

lines = list(csv.reader(open('C:/DX_DATA/dx2_code/django/0208/data/data/fruit.csv'),
                             delimiter='|'))

df = pd.DataFrame(lines, columns = ['name','count','price'])
print(df)

# %%
i = 0 
while True:
    try:
        good = pd.read_csv('C:/DX_DATA/dx2_code/django/0208/data/data/good.csv')

# %% [markdown]
# 한국어 encoding 하는 코드

X

