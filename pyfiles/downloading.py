from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_progress(object):
    def setupUi(self, progress):
        progress.setObjectName("progress")
        progress.resize(816, 616)
        self.centralwidget = QtWidgets.QWidget(progress)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 811, 591))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 50, 521, 321))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Pictures/Fast loading-bro.svg"))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(110, 440, 601, 41))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.progressBar.setStyleSheet("QProgressBar::chunk\n"
"{background-color: rgb(255, 0, 0);\n"
"border-radius:15px;}\n"
"QProgressBar{\n"
"background-color: ;\n"
"    background-color: rgb(198, 198, 198);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border-style: none;\n"
"}\n"
"")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(310, 510, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        progress.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(progress)
        self.statusbar.setObjectName("statusbar")
        progress.setStatusBar(self.statusbar)

        self.retranslateUi(progress)
        QtCore.QMetaObject.connectSlotsByName(progress)

    def retranslateUi(self, progress):
        _translate = QtCore.QCoreApplication.translate
        progress.setWindowTitle(_translate("progress", "MainWindow"))
        self.progressBar.setToolTip(_translate("progress", "Loading"))
        self.progressBar.setFormat(_translate("progress", "%p%"))
        self.label_2.setText(_translate("progress", "Downloading"))
