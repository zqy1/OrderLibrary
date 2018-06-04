# coding:utf-8
import os
import requests
import json
from bs4 import BeautifulSoup
import datetimeManage


url = 'http://seat.hhit.edu.cn/ClientWeb/xcus/ic2/Default.aspx'
login_url = 'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/login.aspx'


def simulate_login(id=2015122937,pwd=2015122937,init_url=login_url):
    """模拟登录
    输入：学号，密码
    req.text json格式的个人信息 accno id name  phone email score credit msn...
    返回：session会话，为了接下来的选择阅览室座位保持连接
    """
    headers = {
        'Host': 'seat.hhit.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    payload = {
        'id':id,
        'pwd':pwd,
        'act':'login',
    }

    session = requests.Session()
    req = session.post(init_url,data=payload,headers=headers)
    # print(req.text)
    print(req)
    return session

def select_room(ids,pwds,dev_id='100457402', start='2018-05-20 07:00', end='2018-05-20 13:00'):
    """提交预约信息
    """
    payload = {'dev_id': dev_id, 'lab_id': '', 'kind_id':'', 'room_id':'', 'type':'dev',
    'prop':'', 'test_id':'', 'term':'', 'test_name':'', 'start':start,'end':end,
     'start_time':'', 'end_time':'', 'up_file':'', 'memo':'', 'act':'set_resv', '_':'1526737582064'
    }
    url = 'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/reserve.aspx'
    session = simulate_login(id=ids, pwd=pwds)
    req2 = session.get(url, params=payload)
    print(req2)
    print(req2.text)
    session.close()

def get_room_url(url):
    # 获取所有阅览室的url 返回字典或列表
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'lxml')
    item_list = soup.find(id='item_list').find_all(class_='it')
    room_head_url = 'http://seat.hhit.edu.cn/ClientWeb/xcus/'
    readingroom_list = []
    room_url_dict = {}
    for i in item_list:
        room_tail_url = i.attrs['url'].strip('../')
        room_url = room_head_url + room_tail_url
        readingroom_list.append(room_url)
        # print(room_url)
        room_url_dict[i.a.span.text] = room_url
    
    # print(room_url_dict)
    return readingroom_list

# 第一步
def post_url(url):
    req = requests.post(url)
    print(req)

# 第二步 第三步数据包含第二步，可跳过
# 第三步
"""
使用的是ajax技术，直接获取不到，先post后再获取json格式解析
"""
def get_seat_dict():
  
    payload = {'byType': 'devcls', 'classkind': '8', 'display':'fp', 'md':'d', 'room_id':'100455353',
    'purpose':'', 'cld_name':'default', 'date':'2018-05-19', 'fr_start':'19:40', 'fr_end':'20:40',
     'act':'get_rsv_sta', '_':'1526727934674'
    }
    url = 'http://seat.hhit.edu.cn/ClientWeb/pro/ajax/device.aspx'
    req = requests.get(url, params=payload)
    # req.text内容是json格式
    to_json(req, 'seat_all.json')
    read_json('seat_all.json')

    

# def to_json(req, filename):
#     # 传入json格式的请求，文件名
#     if not os.path.exists(filename):
#         req_json = json.loads(req.text)
#         with open(filename, 'w', encoding='utf-8') as f:
#             json.dump(req_json, f)
#     else:
#         print('文件已存在')

def to_json(req, filename):
    # 传入json格式的请求，文件名
    req_json = json.loads(req.text)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(req_json, f)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        req_json = json.load(f)
        info = req_json['data']
        # info_dict = {i['devId']:i['devName'] for i in info}
        for i in info:
            id = i['id']




def main():

    all_day = datetimeManage.all_day()
    for i in all_day:
        select_room('2015122912', '2015122912', start=i[0], end=i[1])

    # select_room('2015122912','2015122912', start='2018-06-05 14:00', end='2018-06-05 18:00')
    # simulate_login('2015122912','2015122912')
    # readingroom_list = get_room_url(url)
    
    # post_url(readingroom_list[0])
    # get_seat_dict()

if __name__ == '__main__':
    main()
