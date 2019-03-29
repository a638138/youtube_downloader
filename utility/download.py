from PyQt5.QtCore import QThread, pyqtSignal
from pytube import YouTube, Stream
import setting

class Download_thread(QThread):

    download_finish = pyqtSignal()
    show_download_info = pyqtSignal(Stream, int)
    set_value = pyqtSignal(float)

    def __init__(self, stream, dataType):
        QThread.__init__(self)
        self.stream = stream
        self.dataType = dataType
        
    def __del__(self):
        self.wait()

    def run(self):
        outputPath = str()

        while setting.isDownloading:
            continue

        setting.isDownloading = True

        # 設定檔案名稱
        # 0為純影片
        # 1為影片加音樂，之後要取出其音源，作為轉檔時用到的音源
        # 2為使用者從清單中自選
        if self.dataType == 0:
            file_name = 'Video'
            outputPath = '.\\temp'

        elif self.dataType == 1:
            file_name = 'Audio'
            outputPath = '.\\temp'
            setting.isNeedTransform = True

        elif self.dataType == 2:
            file_name = self.stream.default_filename
            outputPath = '.\\output'

        self.show_download_info.emit(self.stream, self.dataType)
        self.stream.download(output_path=outputPath, filename=file_name)
        self.download_finish.emit()
        # print('Download finished')