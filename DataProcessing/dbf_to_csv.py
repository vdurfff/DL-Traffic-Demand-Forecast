# from dbfread import DBF
# import csv
# import os

# 找出文件夹中所有.dbf文件的文件名，保存在数组中
# # 指定文件夹路径
# folder_path = r'E:\2017POI\2017'

# # 存储 dbf 文件名的列表
# dbf_files = []
# i=0
# # dbf_files = ['交通设施服务.dbf']

# # 遍历文件夹中的所有文件
# for file_name in os.listdir(folder_path):
#     # 检查文件是否以 .dbf 结尾
#     if file_name.endswith(".dbf"):
#         # 如果是，将文件名添加到列表中
#         dbf_files.append(file_name)
#         i += 1
# print(i)
# print(dbf_files)


# 将dbf中的数据写入csv,同时进行筛选
# 指定条件
# desired_category = "海口市"

# # 创建 CSV 文件
# csv_file_path = r"E:\2017POI\海口POI.csv"
# with open(csv_file_path, 'a', newline='', encoding='GB18030') as csvfile:
#     writer = csv.writer(csvfile)

    # 遍历所有 dbf 文件
    # for dbf_file in dbf_files:
    #     try:
    #         # 打开 DBF 文件并读取数据
    #         table = DBF(r"E:\2017POI\2017\\" + dbf_file, encoding='utf-8',char_decode_errors='ignore')
    #         # 如果csv文件为空则写入表头
    #         if os.stat(csv_file_path).st_size == 0:
    #             writer.writerow(table.field_names)
    #         # 检查每行数据是否符合条件，并写入 CSV 文件
    #         for record in table:
    #             if record['CITY'] == desired_category:
    #                 writer.writerow(list(record.values()))
    #         print(dbf_file, 'OK')
    #     except:
    #         print(dbf_file, 'ERROR')
# print('dbf文件中有关海口的数据已转成csv')

############### TEST ##################
import csv
from dbfread import DBF
import pandas as pd
import os

# 打开DBF文件并读取数据
dbf_file = r"D:\系统默认\Documents\gradProject\rawData\Export\POI_grid.dbf"
table = DBF(dbf_file,encoding='GB18030')

# 创建CSV文件并写入数据
csv_file = r"D:\系统默认\Documents\gradProject\rawData\Export\POI_grid.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(table.field_names)
    # 写入每行数据
    for record in table:
        writer.writerow(list(record.values()))
print('dbf处理结束')

# Open csv file
# file = r"E:\2017POI\2017\餐饮服务.csv"
df = pd.read_csv(csv_file,encoding='GB18030')
df.info()
# print(df.head())

# # Screen data of '海口市'
# data = df[df["CITY"].str.contains("海口市")]
# # data.info()
# # print(data.head())

# data.to_csv(r'D:\系统默认\Documents\gradProject\rawData\haiKouWeather_clean.csv', index=False)
# print('csv已保存')   
