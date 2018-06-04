import requests
import json
from bs4 import BeautifulSoup
import datetime
    #   'http://seat.hhit.edu.cn/ClientWeb/xcus/a/roomdetail.aspx?classKind=8&roomId=100455596&roomName=%e8%a5%bf501'
url = 'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/device.aspx?byType=devcls&classkind=8&display=fp&md=d&room_id=100455588&purpose=&cld_name=default&act=get_dev_coord&_=1526693372830'
url2 = 'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/device.aspx?byType=devcls&classkind=8&display=fp&md=d&room_id=100455588&purpose=&cld_name=default&date=2018-05-19&fr_start=09%3A30&fr_end=10%3A30&act=get_rsv_sta&_=1526693373724'
# req = requests.get(url)
# req2 = requests.get(url2)


# req_json = json.loads(req.text)
# with open('data.json', 'w') as f:
#     json.dump(req_json, f)


# with open('data.json', 'r', encoding='utf-8') as f:
#     req_json = json.load(f)
#     info = req_json['data']['objs']
#     info_dict = {i['id']:i['name'] for i in info}
#     print(info_dict)

#     # 保存为csv文件
#     with open('dict.csv','w',encoding='utf-8') as m:
#         for i in info:
#             m.write(i['id'] + ',' + i['name'] + '\n')


# date = datetime.date.today().isoformat()


time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

current_datetime = datetime.datetime.now()

current_date = datetime.datetime.date(current_datetime)
current_time = datetime.datetime.time(current_datetime)

end = current_datetime+datetime.timedelta(hours=4)

# 当前时间大于23:00时，预约日期开始时间只能是次日6：00-21:00
if current_time.hour > 23:
    subscribe_date = current_date + datetime.timedelta(days=1)
    start_subscribe_time = [i for i in range(6, 22)]

else:
    pass