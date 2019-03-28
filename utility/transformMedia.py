from PyQt5.QtCore import QThread, pyqtSignal
import setting

class transformMediaThread(QThread):

    transform_finish_trigger = pyqtSignal()
    transform_progress = pyqtSignal(float)

    def __init__(self):
        QThread.__init__(self)
        
    def __del__(self):
        self.wait()

    def run(self):

        print('transforming...')
        print('transform finished')

        setting.isNeedTransform = False
        for i in range(1, 100):
            self.transform_progress.emit(i)

        self.transform_finish_trigger.emit()
