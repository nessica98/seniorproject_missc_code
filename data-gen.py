import random
import pandas as pd
from datetime import datetime, timedelta

boat_name = ['wooseok','seungwoo','seunghun','minhyun','seongwoo','junho','bomin']
N = 1000
start_time = '2020-04-20 06:00'

str_dt_obj =  datetime.strptime(start_time,"%Y-%m-%d %H:%M")
list_dat = []
for i in range(N):
    a = random.randint(0,len(boat_name))
    check_list = [x for x in range(a)]
    dt_fill_obj = str_dt_obj + timedelta(minutes = i*5)
    for ii in range(a):
        b = random.randint(0,a-1)
        if b in check_list:
            data_res = (boat_name[b],random.random()*random.randint(0,20),random.random()*random.randint(85,120),dt_fill_obj.strftime("%Y-%m-%d %H:%M"))
            check_list.remove(b)
            #print(data_res)
            list_dat.append(data_res)
        else:
            continue

df = pd.DataFrame(list_dat, columns =['NodeName', 'LAT', 'LONG','UpdateDateTime']) 
  
print(df)  

df.to_csv('result1.csv',index=False)