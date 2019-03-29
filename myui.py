# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setMaximumSize(QtCore.QSize(500, 40))
        self.input.setAutoFillBackground(False)
        self.input.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.input.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.input_btn = QtWidgets.QPushButton(self.centralwidget)
        self.input_btn.setObjectName("input_btn")
        self.horizontalLayout.addWidget(self.input_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.downloadOption = QtWidgets.QTableWidget(self.centralwidget)
        self.downloadOption.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadOption.sizePolicy().hasHeightForWidth())
        self.downloadOption.setSizePolicy(sizePolicy)
        self.downloadOption.setMinimumSize(QtCore.QSize(300, 0))
        self.downloadOption.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.downloadOption.setFont(font)
        self.downloadOption.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.downloadOption.setColumnCount(7)
        self.downloadOption.setObjectName("downloadOption")
        self.downloadOption.setRowCount(0)
        self.downloadOption.horizontalHeader().setDefaultSectionSize(49)
        self.verticalLayout.addWidget(self.downloadOption)
        self.preview = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.preview.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.preview.setAutoFillBackground(False)
        self.preview.setUrl(QtCore.QUrl("about:blank"))
        self.preview.setObjectName("preview")
        self.verticalLayout.addWidget(self.preview)
        self.video_title = QtWidgets.QLabel(self.centralwidget)
        self.video_title.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_title.sizePolicy().hasHeightForWidth())
        self.video_title.setSizePolicy(sizePolicy)
        self.video_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.video_title.setAcceptDrops(False)
        self.video_title.setText("")
        self.video_title.setScaledContents(True)
        self.video_title.setWordWrap(True)
        self.video_title.setObjectName("video_title")
        self.verticalLayout.addWidget(self.video_title)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.mp4_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mp4_btn.sizePolicy().hasHeightForWidth())
        self.mp4_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.mp4_btn.setFont(font)
        self.mp4_btn.setAutoDefault(False)
        self.mp4_btn.setDefault(False)
        self.mp4_btn.setFlat(False)
        self.mp4_btn.setObjectName("mp4_btn")
        self.verticalLayout.addWidget(self.mp4_btn)
        self.mp3_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mp3_btn.sizePolicy().hasHeightForWidth())
        self.mp3_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.mp3_btn.setFont(font)
        self.mp3_btn.setObjectName("mp3_btn")
        self.verticalLayout.addWidget(self.mp3_btn)
        self.info = QtWidgets.QTextBrowser(self.centralwidget)
        self.info.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        self.version_info = QtWidgets.QLabel(self.centralwidget)
        self.version_info.setEnabled(False)
        self.version_info.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_info.setObjectName("version_info")
        self.verticalLayout.addWidget(self.version_info)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.label.setText(_translate("MainWindow", "網址"))
        self.input_btn.setText(_translate("MainWindow", "輸入"))
        self.mp4_btn.setText(_translate("MainWindow", "Download MP4"))
        self.mp3_btn.setText(_translate("MainWindow", "Download MP3"))
        self.version_info.setText(_translate("MainWindow", "version 1.0"))

from PyQt5 import QtWebEngineWidgets
