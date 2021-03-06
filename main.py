# 可以用pyinstaller -F -w main.py 輸出exe

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QTextBrowser
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, QStringListModel, QThread, pyqtSignal
from myui import Ui_MainWindow
from pytube import YouTube, Stream
from utility.download import Download_thread
from utility.transformMedia import transformMediaThread
import globalVariable
import threading
import urllib
import glob
import sys, os
import winsound

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        globalVariable.init()
        super(MyWindow, self).__init__(parent)
        self.yt = None
        self.twoPart = False
        self.setupUi(self)
        self.open_all_GUI()
        ####
        # 使介面簡單點
        self.downloadOption.setVisible(False)
        ####
        self.isDownloadMp3 = False
        self.isDownloadMp4 = False
        self.mp4_btn.setEnabled(False)
        self.mp3_btn.setEnabled(False)
        self.mp4_btn.clicked.connect(self.download_mp4)
        self.mp3_btn.clicked.connect(self.download_mp3)
        self.input_btn.clicked.connect(self.inputClick)
        self.downloadOption.itemDoubleClicked.connect(self.tb_double_clicked)
        self.downloadOption.setHorizontalHeaderLabels(['itag', 'mime_type', 'res', 'fps', 'vcodec', 'acodec', 'abr'])
        self.downloadOption.setEditTriggers(QTableWidget.NoEditTriggers)

    def inputClick(self):
        # Reset table
        while(self.downloadOption.rowCount() > 0):
            self.downloadOption.removeRow(0)
        link = self.input.toPlainText()
        try:
            self.yt = YouTube(link, on_progress_callback=self.progress_check)
            self.close_all_GUI()
            self.start_parse_link(link, self.yt)
            self.open_all_GUI()
        except:
            self.info.setText('請檢查網路連線並確認Youtube網址輸入正確')
            print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
            # return

    def tb_double_clicked(self, mi):
        self.close_all_GUI()
        download_tag = self.downloadOption.item(mi.row(), 0).text()
        # print(download_tag)
        stream = self.yt.streams.get_by_itag(download_tag)
        
        # 建立thread
        self.my_thread = Download_thread(stream, 2)
        self.my_thread.download_finish.connect(self.download_done)
        self.my_thread.set_value.connect(self.set_progress)
        self.my_thread.show_download_info.connect(self.show_download_info)
        # stream.download()
        self.my_thread.start()

    def progress_check(self, stream = None, chunk = None, bytes_remaining = None):
        # Gets the percentage of the file that has been downloaded.
        # print(stream, file_size)
        file_size = stream.filesize
        percent = (100*(file_size-bytes_remaining))/file_size
        now_thread = QThread.currentThread()
        now_thread.set_value.emit(percent)
        # print(percent)
        # self.progressBar.setValue(percent)

    def download_mp4(self):

        # 清除上次的暫存檔
        lastFile = [os.path.basename(x) for x in glob.glob(".\\temp\\*")]
        for name in lastFile:
            os.remove('.\\temp\\{file_name}'.format(file_name=name))

        self.isDownloadMp4 = True
        self.close_all_GUI()
        # sldownloadOption
        bestVideo = self.get_best_video(quality=1080)
        audioStream = self.yt.streams.first()
        videoStream = self.yt.streams.get_by_itag(bestVideo)
        # print(audioStream, videoStream)
        self.twoPart = True

        # 下載影片
        self.video_thread = Download_thread(videoStream, 0)
        self.video_thread.download_finish.connect(self.download_done)
        self.video_thread.set_value.connect(self.set_progress)
        self.video_thread.show_download_info.connect(self.show_download_info)
        # stream.download()
        self.video_thread.start()

        # # 下載音樂
        # 2019/03/28 速度太慢, 改從first的影片中抽取出audio
        # 2019/07/29 音質為主
        audioStream = self.yt.streams.filter(only_audio=True).order_by('abr').last()
        self.audio_thread = Download_thread(audioStream, 1)
        self.audio_thread.download_finish.connect(self.download_done)
        self.audio_thread.set_value.connect(self.set_progress)
        self.audio_thread.show_download_info.connect(self.show_download_info)
        # stream.download()
        self.audio_thread.start()
        
        # # self.my_thread.wait()
        # # 下載first的影片，並從中copy其音源
        # self.audio_thread = Download_thread(audioStream, 1)
        # self.audio_thread.download_finish.connect(self.download_done)
        # self.audio_thread.set_value.connect(self.set_progress)
        # self.audio_thread.show_download_info.connect(self.show_download_info)
        # # stream.download()
        # self.audio_thread.start()


    def download_mp3(self):
        # 清除上次的暫存檔
        lastFile = [os.path.basename(x) for x in glob.glob(".\\temp\\*")]
        for name in lastFile:
            os.remove('.\\temp\\{file_name}'.format(file_name=name))
        self.close_all_GUI()
        self.twoPart = True
        self.isDownloadMp3 = True
        # 下載first的影片，並從中copy其音源
        # audioStream = self.yt.streams.first()
        # self.audio_thread = Download_thread(audioStream, 1)
        # self.audio_thread.download_finish.connect(self.download_done)
        # self.audio_thread.set_value.connect(self.set_progress)
        # self.audio_thread.show_download_info.connect(self.show_download_info)

        audioStream = self.yt.streams.filter(only_audio=True).order_by('abr').last()
        self.audio_thread = Download_thread(audioStream, 1)
        self.audio_thread.download_finish.connect(self.download_done)
        self.audio_thread.set_value.connect(self.set_progress)
        self.audio_thread.show_download_info.connect(self.show_download_info)

        # stream.download()
        self.audio_thread.start()

    def set_progress(self, data):
        self.progressBar.setValue(data)

    def download_done(self):

        globalVariable.isDownloading = False
        # 如果為使用者從表單下載則開啟gui後Return
        if not self.twoPart:
            self.open_all_GUI()
            return

        if globalVariable.isNeedTransform == True:
            self.close_all_GUI()
            # 轉檔為0則輸出mp3
            # 轉檔為1則輸出mp4
            if self.isDownloadMp3 == True:
                transformMode = 0
            elif self.isDownloadMp4 == True:
                transformMode = 1
            self.transform_thread = transformMediaThread(transformMode)
            self.transform_thread.transform_finish_trigger.connect(self.transform_finish)
            self.transform_thread.transform_progress.connect(self.set_progress)
            self.transform_thread.start()
            self.info.append('正在轉檔...')

    def transform_finish(self):
        self.isDownloadMp3 = False
        self.isDownloadMp4 = False
        globalVariable.isNeedTransform = False
        # 提示已經轉檔完成
        winsound.MessageBeep()
        self.info.append('完成轉檔')
        self.info.append('輸出檔案位於output資料夾中')
        self.twoPart = False
        self.open_all_GUI()
        
        
    def show_download_info(self, stream, data_type):
        file_size = stream.filesize
        data_name = str()
        # 0為純影片
        # 1為影片加音樂，之後要取出其音源
        # 2為使用者從清單中自選
        if data_type == 0:
            data_name = 'MP4_Video'
        elif data_type == 1:
            data_name = 'MP4_Audio'
        else:
            data_name = stream.default_filename
        self.info.append('正在下載{}，檔案大小:{:.2f}MB'.format(data_name, file_size/(1024*1024)))

    def start_parse_link(self, link, yt):
        video_id = get_video_id(link)
        self.preview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.preview.page().fullScreenRequested.connect(lambda request: request.accept())
        baseUrl = "local"
        self.preview.setUrl(QUrl("https://www.youtube.com/embed/{}".format(video_id)))
        title = yt.title
        media_length = yt.length
        globalVariable.fileName = title
        globalVariable.media_length = float(media_length)
        self.video_title.setText(title)
        # print(video_id)

        slm=QStringListModel()
        allmetaData = list()
        allstream = yt.streams.all()
        for stream in allstream:
            allmetaData.append(extract_tag(stream))
        
        for index, data in zip(range(len(allmetaData)), allmetaData):
            self.downloadOption.insertRow(index)
            for x, _data in zip(range(len(data.keys())), data.values()):
                if str(_data) == 'None':
                    _data = 'x'
                item = QTableWidgetItem(str(_data))
                self.downloadOption.setItem(index, x, item)

    def close_all_GUI(self):
        self.downloadOption.setEnabled(False)
        self.mp4_btn.setEnabled(False)
        self.mp3_btn.setEnabled(False)
        self.input_btn.setEnabled(False)

    def open_all_GUI(self):
        self.downloadOption.setEnabled(True)
        self.mp4_btn.setEnabled(True)
        self.mp3_btn.setEnabled(True)
        self.input_btn.setEnabled(True)

    def get_best_video(self, quality=1080):
        bestQ = -1
        bestQindex = -1        

        for index in range(self.downloadOption.rowCount()):
            tempMimeType = self.downloadOption.item(index, 1).text()
            tempRes = self.downloadOption.item(index, 2).text()
            tempFps = self.downloadOption.item(index, 3).text()

            if tempFps == 'x' or tempRes == 'x' or tempMimeType != 'video/mp4':
                continue

            tempRes = tempRes.replace('p', '')
            if int(tempRes) > quality:
                continue

            tempBestQ = int(tempRes)+int(tempFps)
            if bestQ < tempBestQ:
                bestQindex = index
                bestQ = tempBestQ
        return self.downloadOption.item(bestQindex, 0).text()

def get_video_id(link):
    counter = 0
    for i in link[link.find('v=')+2:]:
        if i != '&':
            counter += 1
        else:
            break
    return link[link.find('v=')+2:link.find('v=')+2+counter]

def extract_tag(stream):
    # itag mime_type res fps vcodec acodec
    temp = stream
    data = {'itag':None, 'mime_type':None, 'res':None, 'fps':None,\
        'vcodec':None, 'acodec':None, 'abr':None}
    data['itag'] = temp.itag
    data['mime_type'] = temp.mime_type
    if temp.includes_video_track:
        data['res'] = temp.resolution
        data['fps'] = temp.fps
        if not temp.is_adaptive:
            data['vcodec'] = temp.video_codec
            data['acodec'] = temp.audio_codec
        else:
            data['vcodec'] = temp.video_codec
    else:
        data['abr'] = temp.abr
        data['acodec'] = temp.audio_codec

    return data

if __name__ == '__main__':
    os.system('mkdir output')
    os.system('mkdir temp')
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
    