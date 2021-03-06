import tushare as ts
import numpy as np
import pandas as pd

#中证新兴    000964
#中证 新能源 000941
#信息产业    h30007
#新材料     h30597
#机器人     h30590

index_cons_dir = '/Users/huyiqing/Desktop/capstone/index_con/'

index_cons_000964 = pd.read_excel(index_cons_dir + '000964cons.xls') # 中证新兴
index_cons_000941 = pd.read_excel(index_cons_dir + '000941cons.xls') # 新能源
index_cons_h30007 = pd.read_excel(index_cons_dir + 'h30007cons.xls') # 信息产业
index_cons_h30597 = pd.read_excel(index_cons_dir + 'h30597cons.xls') # 新材料
index_cons_h30590 = pd.read_excel(index_cons_dir + 'h30590cons.xls') # 机器人

# index_cons_h30590 = index_cons_h30590['成分券代码\nConstituent Code']
# print(index_cons_h30590)


# =================  处理000964中证新兴  ==================     #
index_code_000964 = index_cons_000964['成分券代码\nConstituent Code']
# print(index_cons_000964)

ind_all = ts.get_industry_classified()
ind_all = ind_all.convert_objects(convert_numeric=True)
# ind_all.dtypes
# 全部98只中证新兴成分股信息ind_emerging
ind_emerging = ind_all[ind_all['code'].isin(index_code_000964)]




