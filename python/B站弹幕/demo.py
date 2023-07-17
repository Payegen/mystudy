# @ Time    : 2019/3/5 14:24
# @ Author  : JuRan

import requests
import time
import random

def barrage_get(room_id):
    url = 'https://api.live.bilibili.com/ajax/msg'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    data = {}
    data['roomid'] = room_id
    data['csrf_token'] = 'dbf003b22095e9398177b5201502b0d0'
    data['csrf'] = 'dbf003b22095e9398177b5201502b0d0'

    data = requests.post(url,data=data,headers=header).json()
    # print(MNIST_data['MNIST_data']['admin'])
    # print(MNIST_data['MNIST_data']['room'])
    barrage_data = []
    for item in data['MNIST_data']['room']:
        # print(item['text'])
        barrage_data.append(item['text'])

    # return barrage_data[random.randint(4,6)]
    return barrage_data

# barrage_get(4634937)


def barrage_send(room_id):
    url = 'https://api.live.bilibili.com/msg/send'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer':'https://live.bilibili.com/4634937?spm_id_from=333.334.b_62696c695f6c697665.11',
        'Cookie': 'buvid3=F183DFD1-333D-41C7-96B6-2584309ADB8E11392infoc; LIVE_BUVID=AUTO2915466777024730; sid=62caghbu; UM_distinctid=1681d30bbba3bf-018f7acb91cacf-b781636-1fa400-1681d30bbbbdfa; stardustvideo=1; CURRENT_FNVAL=16; rpdid=oloolmpmoidospxxmmlxw; fts=1547821462; finger=17c9e5f5; DedeUserID=238650100; DedeUserID__ckMd5=91f6ed8e78cd0180; SESSDATA=dd6ca718%2C1555314087%2C9d7af731; bili_jct=8e6a9dd51c95cf313fde9a2d23b92c52; im_seqno_238650100=26; im_local_unread_238650100=0; bp_t_offset_238650100=239986086553953492; _dfcaptcha=c6ad93e2d652dcc3f0e3db5f67fedb42; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1554787065; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1554787339'
    }
    # cookie = {'Cookie':'buvid3=F183DFD1-333D-41C7-96B6-2584309ADB8E11392infoc; LIVE_BUVID=AUTO2915466777024730; sid=62caghbu; UM_distinctid=1681d30bbba3bf-018f7acb91cacf-b781636-1fa400-1681d30bbbbdfa; stardustvideo=1; CURRENT_FNVAL=16; rpdid=oloolmpmoidospxxmmlxw; fts=1547821462; DedeUserID=238650100; DedeUserID__ckMd5=91f6ed8e78cd0180; SESSDATA=e90262e6%2C1552542584%2C31357f21; bili_jct=dbf003b22095e9398177b5201502b0d0; finger=17c9e5f5; im_seqno_238650100=21; im_local_unread_238650100=0; bp_t_offset_238650100=226003210638021809; _dfcaptcha=6c67c85012f7b3d271a29f37acc98b3c; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1551768880,1551769039,1551770514,1551772846; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1551772846'}
    data = {}

    data['roomid'] = room_id
    data['color'] = 16777215
    data['fontsize'] = 25
    data['mode'] = 1
    data['rnd'] = 1554787338
    data['bubble'] = 0
    data['csrf_token'] = '8e6a9dd51c95cf313fde9a2d23b92c52'
    data['csrf'] = '8e6a9dd51c95cf313fde9a2d23b92c52'

    for i in range(10):
        data['msg'] = barrage_get(room_id)[i]
        print(data['msg'])
    # cookies=cookie
        result = requests.post(url, data=data,headers=header)
        time.sleep(0.5)
        print(result)


barrage_send(52507)