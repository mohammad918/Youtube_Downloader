from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_finish(object):
    def setupUi(self, finish):
        finish.setObjectName("finish")
        finish.resize(823, 627)
        self.centralwidget = QtWidgets.QWidget(finish)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 821, 601))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, -10, 481, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Pictures/Done-bro.svg"))
        self.label.setObjectName("label")
        self.Exit = QtWidgets.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(690, 530, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.Exit.setFont(font)
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.Exit.setObjectName("Exit")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(20, 530, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.back.setObjectName("back")
        finish.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(finish)
        self.statusbar.setObjectName("statusbar")
        finish.setStatusBar(self.statusbar)

        self.retranslateUi(finish)
        self.Exit.clicked.connect(finish.close)
        QtCore.QMetaObject.connectSlotsByName(finish)

    def retranslateUi(self, finish):
        _translate = QtCore.QCoreApplication.translate
        finish.setWindowTitle(_translate("finish", "MainWindow"))
        self.Exit.setToolTip(_translate("finish", "exit"))
        self.Exit.setText(_translate("finish", "finish"))
        self.back.setToolTip(_translate("finish", "back home"))
        self.back.setText(_translate("finish", "home"))

