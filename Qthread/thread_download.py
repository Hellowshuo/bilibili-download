from threading import Thread
from PyQt5.QtCore import *
import threading
import os, sys
import urllib.request

class Download_thread(QThread):
    """docstring for Download_thread"""
    download_done = pyqtSignal(bool)
    combine_done = pyqtSignal(bool)
    update = pyqtSignal(dict)

    def __init__(self):
        super(Download_thread, self).__init__()

    def run(self):
        # 利用线程名字来判断是哪个进度
        select_list = []
        t_list = []
        for index,item in enumerate(self.data['data']):
            if item['select']:
                if len(item['video_list']) > 1:
                    select_list.append(item)
                t = Thread(name=str(index),target=self.down_video,args=(item['video_list'],item['title'],item['page']))
                t_list.append(t)
                t.start()

        for t in t_list:
            t.join()

        self.download_done.emit(True)
        if select_list != []:
            self.combine_done.emit(False)
            for item in select_list:
                self.combine_video(item['title'])
            self.combine_done.emit(True)

    def down_video(self,video_list, title, page):
        num = 1
        # print('[正在下载P{}段视频,请稍等...]:'.format(page) + title)
        currentVideoPath = os.path.join(self.data['download_dir'], 'bilibili_video', title)  # 当前目录作为下载目录
        for i in video_list:
            opener = urllib.request.build_opener()
            # 请求头
            opener.addheaders = [
                # ('Host', 'upos-hz-mirrorks3.acgvideo.com'),  #注意修改host,不用也行
                ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
                ('Accept', '*/*'),
                ('Accept-Language', 'en-US,en;q=0.5'),
                ('Accept-Encoding', 'gzip, deflate, br'),
                ('Range', 'bytes=0-'),  # Range 的值要为 bytes=0- 才能下载完整视频
                ('Referer', 'https://www.bilibili.com/video/av67964765?p=3'),  # 注意修改referer,必须要加的!
                ('Origin', 'https://www.bilibili.com'),
                ('Connection', 'keep-alive'),
            ]
            urllib.request.install_opener(opener)
            # 创建文件夹存放下载的视频
            if not os.path.exists(currentVideoPath):
                os.makedirs(currentVideoPath)
            # 开始下载
            if len(video_list) > 1:
                urllib.request.urlretrieve(url=i, filename=os.path.join(currentVideoPath, r'{}-{}.flv'.format(title, num)),reporthook=self.Schedule_cmd)
            else:
                urllib.request.urlretrieve(url=i, filename=os.path.join(currentVideoPath, r'{}.flv'.format(title)),reporthook=self.Schedule_cmd) 
            num += 1

    def Schedule_cmd(self,blocknum, blocksize, totalsize):
        recv_size = blocknum * blocksize
        pervent = round(float(recv_size / totalsize*100))
        data = dict(
            index=int(threading.current_thread().name),
            progress=pervent
            )
        self.update.emit(data)

    def combine_video(self, title):

        currentVideoPath = os.path.join(self.data['download_dir'], 'bilibili_video', title)
        os.chdir(currentVideoPath)
        file_list = os.listdir('.')
        new_file = []
        for file in file_list:
            if file.endswith(".flv"):
                if file+".ts" in file_list:
                    os.remove(file+".ts")
                os.system('''ffmpeg -i "%s" -c copy -bsf:v h264_mp4toannexb -f mpegts "%s.ts"''' % (file,file))
                new_file.append("%s.ts" % file)

        if title + '.mp4' in file_list:
            os.remove(title + '.mp4')

        os.system('''ffmpeg -i "concat:%s" -c copy -bsf:a aac_adtstoasc -movflags +faststart "%s.mp4"''' % ('|'.join(sorted(new_file)), title))
        for file in os.listdir("."):
            if file != title + ".mp4":
                os.remove(file)
        os.chdir(sys.path[0])
