import tushare as ts
import numpy as np
import pandas as pd


# 节能环保
#   节能环保 节能
# 新兴信息产业
#   国产软件 互联金融 云计算 物联网
# 生物产业:
#   生物疫苗 超级细菌 基因概念 基因芯片 基因测序
# 新能源:
#   新能源 智能电网 氢燃料 生物质能 核能核电 生物燃料 绿色照明
# 新能源汽车
#   汽车电子 特斯拉 智能交通
# 高端装备制造业
#   智能穿戴 机器人概念 3D打印 智能机器
# 新材料:
#   石墨烯 超导概念 多晶硅

# df = ts.get_concept_classified()
# df.to_csv("/Users/huyiqing/Desktop/capstone/concept.csv")

df_concept_all = pd.read_csv("/Users/huyiqing/Desktop/capstone/concept.csv")
# print(df_concept_all)
df_new_energy = df_concept_all.copy()
df_new_energy = df_new_energy[df_new_energy['c_name'].isin(['新能源', '智能电网', '氢燃料', '生物质能', '核能核电', '生物燃料', '绿色照明'])]
# print(df_new_energy)
print(df_new_energy.groupby('code').count())
