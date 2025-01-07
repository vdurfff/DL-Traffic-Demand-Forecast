# import numpy as np
import pandas as pd

file = r'D:\系统默认\Documents\gradProject\rawData\海口POI.csv'
df = pd.read_csv(file, encoding ='GB18030')

df['CODE'] = df['CODE'].astype('str')

# Deal with duplicated data -> 2
# print(df[df.duplicated(keep=False)])
df.drop_duplicates(keep='first',inplace=True)
df.reset_index(drop=True)

# # 数据映射 -> don't need
# print(df['PROVINCE'].unique())
# print(df['COUNTY'].unique())
# print(df['CITY'].unique())
# print(df['BASETYPE'].unique())
# print(df['SUBTYPE'].unique())
# print(df['CATEGORY'].unique())

df.info()

#将转换完的数据保存到新的csv文件 index=False去掉编号
df.to_csv(r'D:\系统默认\Documents\gradProject\rawData\haiKouPOI_clean.csv', encoding ='GB18030', index=False)   
