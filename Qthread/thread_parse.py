import requests, hashlib, re, json
import operator
from threading import Thread
from PyQt5.QtCore import *
import threading
import time
import re




#PyQt5多线程
class ParseThread(QThread):
    """docstring for ParseThread"""
    parse_done = pyqtSignal(dict)
    def __init__(self):
        super(ParseThread, self).__init__()

    def run(self):
        if 'ep' in self.url:
            self.parse_bangumi()
        else:
            self.parse_video()

    # 解析番剧
    def parse_bangumi(self):
        ep_url = self.url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        html = requests.get(ep_url,headers=headers).text
        ep_info = re.search(r'INITIAL_STATE__=(.*?"]});', html).group(1)

        ep_info = json.loads(ep_info)
        id_list = []

        for index,i in enumerate(ep_info['epList']):
            try:
                data = dict(
                    aid =str(i['aid']),
                    cid=str(i['cid']),
                    title = i['titleFormat'] + ' ' + i['longTitle'],
                    vip=i['badge'],
                    page=index,
                    )
                id_list.append(data)
            except:
                data = dict(
                    aid =i['aid'],
                    cid=i['cid'],
                    title= '第' + str(i['index']) + '话 ' + i['index_title'],
                    vip=i['badge'],
                    page=index,
                    )
                id_list.append(data)

        t_list = []
        return_data = [] 

        for item in id_list:
            t = threading.Thread(target=bangumi_thread,args=(item,self.config_data['cookie']))
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()
        return_data = dict(
            data = id_list,
            type = "bangumi",
            )
        self.parse_done.emit(return_data)

    def parse_video(self):
        start = self.url
        if start.isdigit() == True:  # 如果输入的是av号
            # 获取cid的api, 传入aid即可
            start_url = 'https://api.bilibili.com/x/web-interface/view?aid=' + start
        else:
            start_url = 'https://api.bilibili.com/x/web-interface/view?aid=' + re.search(r'/av(\d+)/*', start).group(1)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        html = requests.get(start_url, headers=headers).json()
        data = html['data']
        video_title=data["title"].replace(" ","_")
        cid_list = []
        if '?p=' in start:
            # 单独下载分P视频中的一集
            p = re.search(r'\?p=(\d+)',start).group(1)
            cid_list.append(data['pages'][int(p) - 1])
        else:
            # 如果p不存在就是全集下载
            cid_list = data['pages']
        
        self.video_data = []
        self.quality = '80'
        self.start_url = start_url
        t_list = []
        for item in cid_list:
            t = Thread(target=self.parse_data,args=(item,))
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()

        self.video_data.sort(key=operator.itemgetter('page'))
        return_data = dict(
            data = self.video_data,
            type = "video",
            )
        self.parse_done.emit(return_data)

    def parse_data(self,item):
        cid = str(item['cid'])
        title = item['part']
        if not title:
            title = video_title
        title = re.sub(r'[\/\\:*?"<>|]', '', title)  # 替换为空的

        page = int(item['page'])
        start_url = self.start_url + "/?p=" + str(page)
        video_list = get_play_list_video(start_url, cid, self.quality)

        p_data = dict(
        page = page,
        title = title,
        cid = cid,
        video_list = video_list,
        select=False,
            )
        self.video_data.append(p_data)

def bangumi_thread(item,cookie):
    aid = item['aid']
    cid = item['cid']
    title = re.sub(r'[\/\\:*?"<>|]', '', item['title'])  # 替换为空的
    video_list = get_play_list_bangumi(aid, cid, '116',cookie)
    item['video_list'] = video_list
    

def get_play_list_bangumi(aid, cid, quality,cookie):
    url_api = 'https://api.bilibili.com/x/player/playurl?cid={}&avid={}&qn={}'.format(cid, aid, quality)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Cookie': cookie, # 
        'Host': 'api.bilibili.com'
    }
    html = requests.get(url_api, headers=headers).json()
    # print(html)
    # 当下载会员视频时,如果cookie中传入的不是大会员的SESSDATA时就会返回: {'code': -404, 'message': '啥都木有', 'ttl': 1, 'data': None}
    if html['code'] != 0:
        return []
    video_list = []
    for i in html['data']['durl']:
        video_list.append(i['url'])
    # print(video_list)
    return video_list


def get_play_list_video(start_url, cid, quality):
    entropy = 'rbMCKn@KuamXWlPMoJGsKcbiJKUfkPF_8dABscJntvqhRSETg'
    appkey, sec = ''.join([chr(ord(i) + 2) for i in entropy[::-1]]).split(':')
    params = 'appkey=%s&cid=%s&otype=json&qn=%s&quality=%s&type=' % (appkey, cid, quality, quality)
    chksum = hashlib.md5(bytes(params + sec, 'utf8')).hexdigest()
    url_api = 'https://interface.bilibili.com/v2/playurl?%s&sign=%s' % (params, chksum)
    headers = {
        'Referer': start_url,  # 注意加上referer
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    html = requests.get(url_api, headers=headers).json()
    video_list = []
    for i in html['durl']:
        video_list.append(i['url'])
    # print(video_list)
    return video_list

if __name__ == "__main__":
    a = ParseThread()
    a.run()
