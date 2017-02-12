import tushare as ts
import numpy as np
import pandas as pd

#中证新兴    000964
#中证 新能源 000941
#信息产业    h30007
#新材料     h30597
#机器人     h30590

index_cons_dir = '/Users/huyiqing/Desktop/capstone/index_con/'

index_cons_000964 = pd.read_excel(index_cons_dir + '000964cons.xls')
index_cons_000941 = pd.read_excel(index_cons_dir + '000941cons.xls')
index_cons_h30007 = pd.read_excel(index_cons_dir + 'h30007cons.xls')
index_cons_h30597 = pd.read_excel(index_cons_dir + 'h30597cons.xls')
index_cons_h30590 = pd.read_excel(index_cons_dir + 'h30590cons.xls')

# print(index_cons_h30590)