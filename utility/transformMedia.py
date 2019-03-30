from PyQt5.QtCore import QThread, pyqtSignal
from subprocess import Popen, PIPE
from pexpect import popen_spawn, EOF
import globalVariable
import glob
import os
import re

class transformMediaThread(QThread):

    transform_finish_trigger = pyqtSignal()
    transform_progress = pyqtSignal(int)

    def __init__(self, transformMode):
        QThread.__init__(self)
        self.transformMode = transformMode

    def __del__(self):
        self.wait()

    def run(self):

        print('transforming...')

        # 轉檔為0則輸出mp3
        # 轉檔為1則輸出mp4
        try:    
            if self.transformMode == 0:
                self.transformAudio() 
            if self.transformMode == 1:
                self.mergeVideoAudio()
        except:
            # 考慮做例外處理
            globalVariable.transform_status = -1

        print('transform finished')

        globalVariable.isNeedTransform = False
        # 確保秒數沒有剛好整除的情況，進度條沒跑完
        self.transform_progress.emit(100)
        self.transform_finish_trigger.emit()

    def mergeVideoAudio(self):
        ffmpeg = '.\\ffmpeg\\bin\\ffmpeg'
        file_path = '.\\temp\\'
        output_path = '.\\output\\'
        audio = str([os.path.basename(x) for x in glob.glob(".\\temp\\Audio.*")][0])
        video = str([os.path.basename(x) for x in glob.glob(".\\temp\\Video.*")][0])
        filetered_file_name = globalVariable.fileName
        filetered_file_name = re.sub(r'[\/:*?"<>|]', ' ', filetered_file_name)

        cmd = '{ffmpeg} -y -i \"{file_path}{audio_fileName}\" -i \"{file_path}{video_fileName}\" \
            -map 0:a  -map 1:v -c:v copy -c:a ac3 -b:a 320K {output_path}\\\"{output_fileName}.mp4\"' \
            .format(ffmpeg=ffmpeg, file_path=file_path, audio_fileName=audio, video_fileName=video, output_path=output_path, 
                    output_fileName=filetered_file_name)

        self.displayAndStartProgress(cmd)
    # thread = pexpect.spawn(cmd)

    def transformAudio(self):
        ffmpeg = '.\\ffmpeg\\bin\\ffmpeg'
        file_path = '.\\temp\\'
        output_path = '.\\output\\'
        audio = str([os.path.basename(x) for x in glob.glob(".\\temp\\Audio.*")][0])
        filetered_file_name = globalVariable.fileName
        filetered_file_name = re.sub(r'[\/:*?"<>|]', ' ', filetered_file_name)
        
        # ffmpeg 轉檔指令
        cmd = '{ffmpeg} -y -i \"{file_path}{audio_fileName}\" \
            -b:a 320K {output_path}\\\"{output_fileName}.mp3\"' \
            .format(ffmpeg=ffmpeg, file_path=file_path, audio_fileName=audio, output_path=output_path, 
                    output_fileName=filetered_file_name)
        
        self.displayAndStartProgress(cmd)

    def displayAndStartProgress(self, cmd):
        thread = popen_spawn.PopenSpawn(cmd)

        # 比對ffmpeg output的資料
        # 參考自:https://stackoverflow.com/questions/7632589/getting-realtime-output-from-ffmpeg-to-be-used-in-progress-bar-pyqt4-stdout
        cpl = thread.compile_pattern_list([
            EOF,
            "time= *\d+:\d+:\d+"
        ])

        while True:
            i = thread.expect_list(cpl, timeout=None)
            if i == 0: # EOF
                print("the sub process exited")
                break
            elif i == 1:
                time_number = thread.match.group(0)
                time_number = time_number[5:].decode('utf-8')
                current_second = float(time_number[:2])*60*60 + float(time_number[3:5])*60 + float(time_number[6:])

                percent = current_second / globalVariable.media_length * 100
                # print(current_second, globalVariable.media_length)
                self.transform_progress.emit(percent)
