from extractor import Extractor
from matcher import Matcher

import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindowUI(object):
    """Class untuk UI"""

    def __init__(self):
        self.extractor = Extractor()

    def setupUi(self, MainWindow):
        # Main
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 660)
        MainWindow.setWindowIcon(QIcon("icon\\itb_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setWindowTitle("Face Recognition App")
        # Background and title
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(-10, -10, 881, 661))
        pixmap = QPixmap(os.getcwd() + "\\img\\background.png")
        pixmap = pixmap.scaled(self.backgroundLabel.width(), self.backgroundLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.backgroundLabel.setPixmap(pixmap)
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(320, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        # Search Group
        self.searchGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.searchGroup.setGeometry(QtCore.QRect(30, 440, 571, 191))
        self.searchGroup.setObjectName("searchGroup")
        self.formLayoutWidget = QtWidgets.QWidget(self.searchGroup)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 531, 115))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.srcFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.srcFormLayout.setContentsMargins(0, 0, 0, 0)
        self.srcFormLayout.setObjectName("srcFormLayout")
        # Search label
        self.imgPathLbl = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgPathLbl.sizePolicy().hasHeightForWidth())
        self.imgPathLbl.setSizePolicy(sizePolicy)
        self.imgPathLbl.setMinimumSize(QtCore.QSize(0, 0))
        self.imgPathLbl.setObjectName("imgPathLbl")
        self.srcFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.imgPathLbl)
        self.topImgLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.topImgLbl.setObjectName("topImgLbl")
        self.srcFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.topImgLbl)
        self.matchAlgLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.matchAlgLbl.setObjectName("matchAlgLbl")
        self.srcFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.matchAlgLbl)
        self.fastAlgLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.fastAlgLbl.setObjectName("fastAlgLbl")
        self.srcFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fastAlgLbl)
        # Search Input
        self.imgPathGrid = QtWidgets.QGridLayout()
        self.imgPathGrid.setObjectName("imgPathGrid")
        self.imgPathBtn = QtWidgets.QToolButton(self.formLayoutWidget)
        self.imgPathBtn.setObjectName("imgPathBtn")
        self.imgPathGrid.addWidget(self.imgPathBtn, 0, 1, 1, 1)
        self.imgPathInp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.imgPathInp.setEnabled(True)
        self.imgPathInp.setObjectName("imgPathInp")
        self.imgPathGrid.addWidget(self.imgPathInp, 0, 0, 1, 1)
        self.srcFormLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.imgPathGrid)
        self.topImgInp = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.topImgInp.setMinimum(1)
        self.topImgInp.setValue(5)
        self.topImgInp.setObjectName("topImgInp")
        self.srcFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.topImgInp)
        self.matchAlgInp = QtWidgets.QComboBox(self.formLayoutWidget)
        self.matchAlgInp.addItems(["Euclidean Distance", "Cosine Similarity"])
        self.matchAlgInp.setObjectName("matchAlgInp")
        self.srcFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.matchAlgInp)
        self.fastAlgInp = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.fastAlgInp.setEnabled(True)
        self.fastAlgInp.setText("")
        self.fastAlgInp.setObjectName("fastAlgInp")
        self.srcFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fastAlgInp)
        self.initBtn = QtWidgets.QPushButton(self.searchGroup)
        self.initBtn.setGeometry(QtCore.QRect(120, 150, 93, 28))
        self.initBtn.setObjectName("initBtn")
        self.searchBtn = QtWidgets.QPushButton(self.searchGroup)
        self.searchBtn.setGeometry(QtCore.QRect(20, 150, 93, 28))
        self.searchBtn.setEnabled(False)
        self.searchBtn.setObjectName("searchBtn")
        # Image In Group
        self.ImInGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.ImInGroup.setGeometry(QtCore.QRect(60, 50, 351, 381))
        self.ImInGroup.setObjectName("ImInGroup")
        self.picInLabel = QtWidgets.QLabel(self.ImInGroup)
        self.picInLabel.setGeometry(QtCore.QRect(10, 30, 331, 341))
        self.picInLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.picInLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picInLabel.setObjectName("picInLabel")
        # Image Out Group
        self.ImOutGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.ImOutGroup.setGeometry(QtCore.QRect(460, 50, 351, 381))
        self.ImOutGroup.setObjectName("ImOutGroup")
        self.picOutLabel = QtWidgets.QLabel(self.ImOutGroup)
        self.picOutLabel.setGeometry(QtCore.QRect(10, 30, 331, 341))
        self.picOutLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.picOutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picOutLabel.setObjectName("picOutLabel")
        # Extract Database Group
        self.extGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.extGroup.setGeometry(QtCore.QRect(620, 500, 191, 91))
        self.extGroup.setObjectName("extGroup")
        self.extBtn = QtWidgets.QPushButton(self.extGroup)
        self.extBtn.setGeometry(QtCore.QRect(30, 50, 131, 28))
        self.extBtn.setObjectName("extBtn")
        self.imgFilterBox = QtWidgets.QCheckBox(self.extGroup)
        self.imgFilterBox.setGeometry(QtCore.QRect(30, 30, 131, 20))
        self.imgFilterBox.setObjectName("imgFilterBox")
        # Image out button
        self.imOutBtnGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.imOutBtnGroup.setGeometry(QtCore.QRect(620, 439, 191, 61))
        self.imOutBtnGroup.setObjectName("imOutBtnGroup")
        self.prevImgBtn = QtWidgets.QPushButton(self.imOutBtnGroup)
        self.prevImgBtn.setEnabled(False)
        self.prevImgBtn.setGeometry(QtCore.QRect(30, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        self.prevImgBtn.setFont(font)
        self.prevImgBtn.setObjectName("prevImgBtn")
        self.nextImgBtn = QtWidgets.QPushButton(self.imOutBtnGroup)
        self.nextImgBtn.setEnabled(False)
        self.nextImgBtn.setGeometry(QtCore.QRect(100, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        self.nextImgBtn.setFont(font)
        self.nextImgBtn.setObjectName("nextImgBtn")
        # About and Exit button
        self.aboutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.aboutBtn.setGeometry(QtCore.QRect(620, 600, 93, 28))
        self.aboutBtn.setObjectName("aboutBtn")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(720, 600, 93, 28))
        self.exitBtn.setObjectName("exitBtn")
        # Status bar
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.showMessage("Ready")
        MainWindow.setStatusBar(self.statusBar)
        # Finishing setup
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Signal and Slot
        # Search
        self.imgPathInp.returnPressed.connect(self.imageInputPathChanged)
        self.imgPathBtn.clicked.connect(self.selectImageInput)
        self.initBtn.clicked.connect(self.initializeMatcher)
        self.searchBtn.clicked.connect(self.searchImage)
        # Image Out
        self.prevImgBtn.clicked.connect(self.prevImage)
        self.nextImgBtn.clicked.connect(self.nextImage)
        # Extract Database
        self.extBtn.clicked.connect(self.extractDatabase)
        # About and Exit
        text = "A project from course Linear Algebra and Geometry IF2123 ITB 2019"
        self.aboutBtn.clicked.connect(lambda: self.dialogWindow("About", "Face Recognition App", subtext=text, type="Information"))
        self.exitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition App IF2123 ITB 2019"))
        self.titleLabel.setText(_translate("MainWindow", "Face Recognition App"))
        self.searchGroup.setTitle(_translate("MainWindow", "Search Settings"))
        self.imgPathLbl.setText(_translate("MainWindow", "Image In Path"))
        self.topImgLbl.setText(_translate("MainWindow", "Top Image Out"))
        self.matchAlgLbl.setText(_translate("MainWindow", "Matching Algorithm"))
        self.fastAlgLbl.setText(_translate("MainWindow", "Fast Algorithm"))
        self.imgPathBtn.setText(_translate("MainWindow", "..."))
        self.initBtn.setText(_translate("MainWindow", "Init Matcher"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.ImInGroup.setTitle(_translate("MainWindow", "Image In"))
        self.ImOutGroup.setTitle(_translate("MainWindow", "Image Out"))
        self.extGroup.setTitle(_translate("MainWindow", "Database"))
        self.imgFilterBox.setText(_translate("MainWindow", "Image Only Filter"))
        self.extBtn.setText(_translate("MainWindow", "Extract"))
        self.imOutBtnGroup.setTitle(_translate("MainWindow", "Image Out Button"))
        self.prevImgBtn.setText(_translate("MainWindow", "<"))
        self.nextImgBtn.setText(_translate("MainWindow", ">"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.aboutBtn.setText(_translate("MainWindow", "About"))

    def selectImageInput(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if fileName:
            self.setImageInput(fileName)

    def imageInputPathChanged(self):
        try:    # test file existence
            if os.path.isfile(self.imgPathInp.text()):  # image test
                img = Image.open(self.imgPathInp.text())
                self.setImageInput(self.imgPathInp.text())
            else:
                self.dialogWindow("Open File", self.imgPathInp.text(), subtext="File not found!", type="Warning")
        except IOError:
            self.dialogWindow("Open File", self.imgPathInp.text(), subtext="File is not an image!", type="Warning")

    def setImageInput(self, fileName):
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(self.picInLabel.width(), self.picInLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.picInLabel.setPixmap(pixmap)
        self.picInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imgPathInp.setText(fileName)

    def setImageOutput(self, fileName):
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(self.picOutLabel.width(), self.picOutLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.picOutLabel.setPixmap(pixmap)
        self.picOutLabel.setAlignment(QtCore.Qt.AlignCenter)

    def initializeMatcher(self):
        self.setStatusText("Precomputing vector norm from package...")
        if self.fastAlgInp.isChecked():
            self.matcher = Matcher(fastAlgorithm=True)
        else:
            self.matcher = Matcher()
        self.searchBtn.setEnabled(True)
        self.setStatusText("Initialization completed")

    def searchImage(self):
        self.setStatusText("Matching image...")
        try:    # test file existence
            if os.path.isfile(self.imgPathInp.text()):  # image test
                img = Image.open(self.imgPathInp.text())
                self.imgVector = self.extractor.extractImage(self.imgPathInp.text())
                # Setup search
                matchAlgorithm = ("euDist") if (self.matchAlgInp.currentIndex() == 0) else ("cosSim")
                self.simImgPath, self.simImgDist = self.matcher.match(self.imgVector,
                                    matchAlgorithm, self.topImgInp.value(), self.fastAlgInp.isChecked())
                # Show Image Out and Create Image Index Property
                self.topImgMax = self.topImgInp.value() - 1
                self.topImgNow = 0
                self.setImageOutput(self.simImgPath[0])
                if self.topImgNow != self.topImgMax:
                    self.nextImgBtn.setEnabled(True)
                self.setStatusText(self.simImgPath[0] + "\tDistance: " + str(self.simImgDist[0]))
            else:
                self.dialogWindow("Open File", self.imgPathInp.text(), subtext="File not found!", type="Warning")
                self.setStatusText("Matching failed")
        except IOError:
            self.dialogWindow("Open File", self.imgPathInp.text(), subtext="File is not an image!", type="Warning")
            self.setStatusText("Matching failed")

    def prevImage(self):
        self.nextImgBtn.setEnabled(True)
        self.topImgNow -= 1
        if self.topImgNow == 0:
            self.prevImgBtn.setEnabled(False)
        self.setImageOutput(self.simImgPath[self.topImgNow])
        self.setStatusText(self.simImgPath[self.topImgNow] + "\tDistance: " + str(self.simImgDist[self.topImgNow]))

    def nextImage(self):
        self.prevImgBtn.setEnabled(True)
        self.topImgNow += 1
        if self.topImgNow == self.topImgMax:
            self.nextImgBtn.setEnabled(False)
        self.setImageOutput(self.simImgPath[self.topImgNow])
        self.setStatusText(self.simImgPath[self.topImgNow] + "\tDistance: " + str(self.simImgDist[self.topImgNow]))

    def extractDatabase(self):
        self.setStatusText("Extracting vector from database...")
        self.extractor.extractBatch("db", checkImg=self.imgFilterBox.isChecked())
        self.setStatusText("Extraction completed")

    def setStatusText(self, text):
        self.statusBar.showMessage(text)

    def dialogWindow(self, title, text, subtext="" , type="Information"):
        message = QMessageBox()
        if type == "Question":
            message.setIcon(QMessageBox.Question)
        elif type == "Warning":
            message.setIcon(QMessageBox.Warning)
        elif type == "Critical":
            message.setIcon(QMessageBox.Critical)
        else:
            message.setIcon(QMessageBox.Information)
        message.setWindowTitle(title)
        message.setWindowIcon(QIcon("icon/qmessage_icon.png"))
        message.setText(text)
        message.setInformativeText(subtext)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
