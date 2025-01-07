import pandas as pd

file = r"D:\系统默认\Documents\gradProject\rawData\haiKouOrder_clean.csv"
df = pd.read_csv(file, encoding='GB18030')

# df.info()
df['出发时间'] = pd.to_datetime(df['出发时间'])
df['出发日期'] = df['出发时间'].dt.date
print(df.head())

df.to_csv(r'D:\系统默认\Documents\gradProject\rawData\haiKouOrder_date.csv', encoding='GB18030', index=False)   