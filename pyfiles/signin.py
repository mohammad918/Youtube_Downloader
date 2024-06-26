from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_signin(object):
    def setupUi(self, signin):
        signin.setObjectName("signin")
        signin.resize(845, 842)
        self.centralwidget = QtWidgets.QWidget(signin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 841, 811))
        self.frame.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(110, 90, 621, 641))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 180, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #d8d8d8;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 260, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: #d8d8d8;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(360, 560, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 560, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        font.setUnderline(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(260, 20, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 390, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(800, 10, 31, 28))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("background-color: rgb(193, 0, 0);\n"
"border-radius:8px;\n"
"")
        self.close.setText("")
        self.close.setObjectName("close")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("background-color:rgb(170, 85, 0);")
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/icons8-return-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QtCore.QSize(27, 50))
        self.back.setObjectName("back")
        self.max = QtWidgets.QPushButton(self.frame)
        self.max.setGeometry(QtCore.QRect(760, 10, 31, 28))
        self.max.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius:8px;")
        self.max.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../YOUTUBE_DOWNLOADER/Pictures/icons8-subtract-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max.setIcon(icon1)
        self.max.setObjectName("max")
        self.min = QtWidgets.QPushButton(self.frame)
        self.min.setGeometry(QtCore.QRect(720, 10, 31, 28))
        self.min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min.setStyleSheet("background-color: rgb(0, 229, 0);\n"
"border-radius:8px;")
        self.min.setText("")
        self.min.setIcon(icon1)
        self.min.setObjectName("min")
        signin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(signin)
        self.statusbar.setObjectName("statusbar")
        signin.setStatusBar(self.statusbar)

        self.retranslateUi(signin)
        self.min.clicked.connect(signin.showMinimized)
        self.max.clicked.connect(signin.showNormal)
        self.close.clicked.connect(signin.close)
        QtCore.QMetaObject.connectSlotsByName(signin)

    def retranslateUi(self, signin):
        _translate = QtCore.QCoreApplication.translate
        signin.setWindowTitle(_translate("signin", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("signin", "type your Username or E-mail"))
        self.lineEdit_2.setPlaceholderText(_translate("signin", "type your Password"))
        self.pushButton.setText(_translate("signin", "create new account"))
        self.pushButton_2.setText(_translate("signin", "forgot Password"))
        self.label.setText(_translate("signin", "sign in"))
        self.pushButton_3.setText(_translate("signin", "sign in"))
        self.pushButton_3.setShortcut(_translate("signin", "Return"))
        self.close.setToolTip(_translate("signin", "close"))
        self.back.setToolTip(_translate("signin", "Click to go back"))
        self.max.setToolTip(_translate("signin", "normal"))
        self.min.setToolTip(_translate("signin", "minimize"))

