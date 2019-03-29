from PyQt5.QtCore import QThread, pyqtSignal
from subprocess import Popen
import setting
import glob
import os
import setting
import re

class transformMediaThread(QThread):

    transform_finish_trigger = pyqtSignal()
    transform_progress = pyqtSignal(float)

    def __init__(self, transformMode):
        QThread.__init__(self)
        self.transformMode = transformMode

    def __del__(self):
        self.wait()

    def run(self):

        print('transforming...')

        # 轉檔為0則輸出mp3
        # 轉檔為1則輸出mp4
        if self.transformMode == 0:
            transformAudio()
        if self.transformMode == 1:
            mergeVideoAudio()

        print('transform finished')

        setting.isNeedTransform = False

        self.transform_finish_trigger.emit()

def mergeVideoAudio():
    ffmpeg = '.\\ffmpeg\\bin\\ffmpeg'
    file_path = '.\\temp\\'
    output_path = '.\\output\\'
    audio = str([os.path.basename(x) for x in glob.glob(".\\temp\\Audio.*")][0])
    video = str([os.path.basename(x) for x in glob.glob(".\\temp\\Video.*")][0])
    filetered_file_name = setting.fileName
    filetered_file_name = re.sub(r'[\/:*?"<>|]', ' ', filetered_file_name)

    cmd = '{ffmpeg} -y -i \"{file_path}{audio_fileName}\" -i \"{file_path}{video_fileName}\" \
           -map 0:a  -map 1:v -c:v copy -c:a ac3 -b:a 320K {output_path}\\\"{output_fileName}.mp4\"' \
           .format(ffmpeg=ffmpeg, file_path=file_path, audio_fileName=audio, video_fileName=video, output_path=output_path, 
                   output_fileName=filetered_file_name)

    p = Popen(cmd)
    p.wait()
    # thread = pexpect.spawn(cmd)

def transformAudio():
    ffmpeg = '.\\ffmpeg\\bin\\ffmpeg'
    file_path = '.\\temp\\'
    output_path = '.\\output\\'
    audio = str([os.path.basename(x) for x in glob.glob(".\\temp\\Audio.*")][0])
    filetered_file_name = setting.fileName
    filetered_file_name = re.sub(r'[\/:*?"<>|]', ' ', filetered_file_name)

    cmd = '{ffmpeg} -y -i \"{file_path}{audio_fileName}\" \
           -b:a 320K {output_path}\\\"{output_fileName}.mp3\"' \
           .format(ffmpeg=ffmpeg, file_path=file_path, audio_fileName=audio, output_path=output_path, 
                   output_fileName=filetered_file_name)
    print(cmd)
    p = Popen(cmd)
    p.wait()

# ffmpeg -i Audio.mp4 -i Video.mp4 -map 0:a  -map 1:v -c:v copy -c:a ac3 -b:a 320K output.mp4