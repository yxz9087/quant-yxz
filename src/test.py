import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt


file="E:\data\stock\meta\stock_list.csv"
pro = ts.pro_api()
# data=pro.query('stock_basic', exchange='', list_status='L')
# data.to_csv(file,encoding='utf_8_sig')
data=pd.read_csv(file)
data1=data.query('name=="江西铜业"')
ts_code = data1['ts_code'].tolist()[0]
df = pro.daily(ts_code=ts_code, start_date='20180701', end_date='20190626').to_csv(file,encoding='utf_8_sig')
df.plot("trade_date","close")
plt.show()


