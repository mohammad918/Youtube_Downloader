from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(1125, 882)
        welcome.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1121, 851))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:rgb(255, 0, 0);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, 50, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(620, 690, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.pushButton.setObjectName("pushButton")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(1080, 10, 31, 28))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("background-color: rgb(193, 0, 0);\n"
"border-radius:8px;\n"
"")
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../YOUTUBE_DOWNLOADER/Pictures/icons8-close-480.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setObjectName("close")
        self.min = QtWidgets.QPushButton(self.frame)
        self.min.setGeometry(QtCore.QRect(1000, 10, 31, 28))
        self.min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min.setStyleSheet("background-color: rgb(0, 229, 0);\n"
"border-radius:8px;")
        self.min.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../YOUTUBE_DOWNLOADER/Pictures/icons8-subtract-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min.setIcon(icon1)
        self.min.setObjectName("min")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 521, 451))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Pictures/Hello-rafiki (2).svg"))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 690, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.max = QtWidgets.QPushButton(self.frame)
        self.max.setGeometry(QtCore.QRect(1040, 10, 31, 28))
        self.max.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius:8px;")
        self.max.setText("")
        self.max.setIcon(icon1)
        self.max.setObjectName("max")
        welcome.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(welcome)
        self.statusbar.setObjectName("statusbar")
        welcome.setStatusBar(self.statusbar)

        self.retranslateUi(welcome)
        self.close.clicked.connect(welcome.close)
        self.min.clicked.connect(welcome.showMinimized)
        self.max.clicked.connect(welcome.showNormal)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "MainWindow"))
        self.label.setText(_translate("welcome", "welcome to savify"))
        self.pushButton.setText(_translate("welcome", "SIGN UP"))
        self.close.setToolTip(_translate("welcome", "close"))
        self.min.setToolTip(_translate("welcome", "minimize"))
        self.pushButton_2.setText(_translate("welcome", "SIGN IN"))
        self.max.setToolTip(_translate("welcome", "normal"))


