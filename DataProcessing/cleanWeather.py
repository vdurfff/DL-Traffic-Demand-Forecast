import numpy as np
import pandas as pd

# file = r'D:\系统默认\Documents\gradProject\rawData\海口网约车订单数据.csv'
file = r'D:\系统默认\Documents\gradProject\rawData\haiKouWeather.csv'
df = pd.read_csv(file)

# Remove useless column
df.drop(columns='Unnamed: 0',inplace=True)

# Split '风向' to '风向' and '风力'
df[['风向','风力']]=df['风向'].str.split(' ',expand=True)
# df.drop(axis = 1, columns = '风向', inplace = True)

# Remove unit of temporate
df['最高温度'] = df['最高温度'].apply(lambda x:x[:-1])
df['最低温度'] = df['最低温度'].apply(lambda x:x[:-1])
df['风力'] = df['风力'].apply(lambda x:x[:-1])
 
# Consolidate the format of '风力'
# print(df['风力'])
for index, value in df['风力'].items():
    if '~' in value:
        df.loc[index, '风力'] = value[0] + '.5'
    if '微' in value:
        df.loc[index, '风力'] = '0'
# print(df['风力'][179])
# print(type(df['风力'][179]))

# Convert the data type
df['日期'] = df['日期'].astype('datetime64[ns]')
df['最高温度'] = df['最高温度'].astype('float64')
df['最低温度'] = df['最低温度'].astype('float64')
df['风力'] = df['风力'].astype('float64')

# Duplicated -> no
# print(df[df.duplicated(keep=False)])

# Data mapping -> don't need
# print(df['天气'].unique())
# print(df['风向'].unique())

# print(df.shape)
print(type(df['日期']))
# print(df.head())
# print(df.describe)
# df.info()

#将转换完的数据保存到新的csv文件 index=False去掉编号
# df.to_csv(r'D:\系统默认\Documents\gradProject\rawData\haiKouWeather_clean.csv', encoding='GB18030', index=False)   
