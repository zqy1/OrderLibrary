# -*- coding:utf-8 -*-
"""时间管理模块"""
from datetime import datetime
from datetime import timedelta


# 全天时间段 获取第二天日期并返回次日全天预定时间段
def all_day():
    # 当前日期时间
    current_datetime = datetime.now()
    # 当前日期
    current_date = datetime.date(current_datetime)
    # 预定日期
    subscribe_date = current_date + timedelta(days=1)
    subscribe_date_str = subscribe_date.strftime('%Y-%m-%d ')
    day_time = [(subscribe_date_str + str(i) + ':00', subscribe_date_str + str(i+4)+':00') for i in range(6,22,4)]
    return day_time

# 本地现在时间
time = datetime.now().strftime('%Y-%m-%d %H:%M')

# 当前日期时间
current_datetime = datetime.now()

# 当前日期
current_date = datetime.date(current_datetime)
# 当前时间
current_time = datetime.time(current_datetime)

end = current_datetime + timedelta(hours=4)

# 当前时间大于23:00时，预约日期开始时间只能是次日6：00-21:00
if current_time.hour > 23:
    subscribe_date = current_date + timedelta(days=1)
    start_subscribe_time = [i for i in range(6, 22)]

else:
    pass
