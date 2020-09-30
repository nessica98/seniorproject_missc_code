from datetime import datetime, timedelta


date_time = '2020-09-20 00:30'

dt_obj = datetime.strptime(date_time,"%Y-%m-%d %H:%M")
future_date_after_one_year = dt_obj + timedelta(minutes = 5)

print(dt_obj)
print(future_date_after_one_year)