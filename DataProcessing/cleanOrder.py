import pandas as pd
# import re

file = r'D:\系统默认\Documents\gradProject\rawData\海口网约车订单数据.csv'
df = pd.read_csv(file)

# Data type
df['订单ID'] = df['订单ID'].astype('str')
df['车型'] = df['车型'].astype('str')
df['订单时效'] = df['订单时效'].astype('str')
df['到达时间'] = df['到达时间'].astype('datetime64[ns]')
df['出发时间'] = df['出发时间'].astype('datetime64[ns]')

# Duplicated data -> none
# print(df[df.duplicated(keep=False)])
# df.drop_duplicates(keep='first',inplace=True)
# df.reset_index(drop=True)

# Data mappling -> ok
# print(df['车型'].unique())
# print(df['订单时效'].unique())

# Missing value?
# print(df.isnull().sum())
# print(df[df.isnull().values==True])
# attributes = ['行程距离','出发时间','到达时间','订单费用','行程时间','终点经度','终点纬度','起点经度','起点纬度']
# for attribute in attributes:
#     print(attribute)
#     print(df[df[attribute] == ""])
    # print(df[df[attribute].apply(lambda x: len(re.findall('NA|[*|?|!|#|-]', x)) != 0)])



# print(df.describe)

df.rename(columns={'订单ID':'OrderID',
                   '车型':'VehicleType',
                   '订单时效':'Appointment',
                   '行程距离':'Distance',
                   '到达时间':'ArrivalTime',
                   '出发时间':'DepartureTime',
                   '订单费用':'Cost',
                   '行程时间':'TravelTime',
                   '终点经度':'lon_e',
                   '终点纬度':'lat_e',
                   '起点经度':'lon_s',
                   '起点纬度':'lat_s'},inplace=True)
df.info()
#将转换完的数据保存到新的csv文件 index=False去掉编号
df.to_csv(r'D:\系统默认\Documents\gradProject\rawData\haiKouOrder_clean.csv', index=False)   