import pandas as pd

# 从ArcGIS导出的数据中保留部分列
csv_file = r"D:\系统默认\Documents\gradProject\rawData\Export\POI_grid.csv"
df = pd.read_csv(csv_file,encoding="GB18030")
df.rename(columns={'FID_haiKou':'FID_POI','FID_grid_b':'FID_grid'},inplace=True)
csv_save = r"D:\系统默认\Documents\gradProject\rawData\POI_grid_s1.csv"
df.to_csv(csv_save,columns=['FID_POI','BASETYPE','FID_grid'],index=False,encoding='GB18030')