from extractor import Extractor
from matcher import Matcher

import os
from PIL import Image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindowUI(object):
    """Class untuk UI"""

    def __init__(self):
        # Extractor
        self.extractor = Extractor()
        self.extractor.sgnExtTotalImg.connect(self.extProgBar)
        self.extractor.sgnExtProgress.connect(self.setExtProgBarVal)
        self.extractor.sgnExtException.connect(self.extractDatabaseException)
        self.extractor.sgnExtStatus.connect(self.extractDatabaseStatus)
        self.extractor.sgnExtDone.connect(self.extractDatabaseDone)
        # Matcher
        self.matcher = Matcher()
        self.matcher.sgnSrcTotalImg.connect(self.srcProgBar)
        self.matcher.sgnSrcProgress.connect(self.setSrcProgBarVal)
        self.matcher.sgnSrcException.connect(self.searchImageException)
        self.matcher.sgnSrcResult.connect(self.searchImageResult)
        self.matcher.sgnSrcDone.connect(self.searchImageDone)

    # Setup UI
    def setupUi(self, MainWindow):
        # Main
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(869, 660)
        MainWindow.setWindowIcon(QIcon("icon\\itb_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setWindowTitle("Face Recognition App")
        # Menu bar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 869, 26))
        self.fileMenu = self.menuBar.addMenu("File")
        text = "A project from course Linear Algebra and Geometry IF2123 ITB 2019"
        functor = lambda: self.dialogWindow("About", "Face Recognition App", subtext=text, type="Information")
        self.aboutMenu = self.fileMenu.addAction("About", functor)
        functor = QtCore.QCoreApplication.instance().quit
        self.exitMenu = self.fileMenu.addAction("Exit", functor)
        self.menuBar.setObjectName("menuBar")
        # Background and title
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(-10, -10, 881, 661))
        pixmap = QPixmap(os.getcwd() + "\\img\\background.png")
        pixmap = pixmap.scaled(self.backgroundLabel.width(), self.backgroundLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.backgroundLabel.setPixmap(pixmap)
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(320, 18, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(13)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        # Search Group
        self.searchGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.searchGroup.setGeometry(QtCore.QRect(30, 440, 591, 191))
        self.searchGroup.setObjectName("searchGroup")
        self.formLayoutWidget = QtWidgets.QWidget(self.searchGroup)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 551, 115))
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
        self.ImInGroup.setGeometry(QtCore.QRect(60, 56, 351, 381))
        self.ImInGroup.setObjectName("ImInGroup")
        self.picInLabel = QtWidgets.QLabel(self.ImInGroup)
        self.picInLabel.setGeometry(QtCore.QRect(10, 30, 331, 341))
        self.picInLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.picInLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picInLabel.setObjectName("picInLabel")
        # Image Out Group
        self.ImOutGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.ImOutGroup.setGeometry(QtCore.QRect(460, 56, 351, 381))
        self.ImOutGroup.setObjectName("ImOutGroup")
        self.picOutLabel = QtWidgets.QLabel(self.ImOutGroup)
        self.picOutLabel.setGeometry(QtCore.QRect(10, 30, 331, 341))
        self.picOutLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.picOutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picOutLabel.setObjectName("picOutLabel")
        # Extract Database Group
        self.extGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.extGroup.setGeometry(QtCore.QRect(650, 500, 191, 131))
        self.extGroup.setObjectName("extGroup")
        self.extBtn = QtWidgets.QPushButton(self.extGroup)
        self.extBtn.setGeometry(QtCore.QRect(30, 90, 131, 28))
        self.extBtn.setObjectName("extBtn")
        self.imgFilterBox = QtWidgets.QCheckBox(self.extGroup)
        self.imgFilterBox.setGeometry(QtCore.QRect(20, 30, 131, 20))
        self.imgFilterBox.setObjectName("imgFilterBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.extGroup)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 160, 26))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.threadLbl = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.threadLbl.setObjectName("threadLbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.threadLbl)
        self.threadInp = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.threadInp.setMinimum(1)
        threadPool = QThreadPool()
        self.threadInp.setMaximum(threadPool.maxThreadCount() if (threadPool.maxThreadCount() > 1) else 1)
        self.threadInp.setObjectName("threadInp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.threadInp)
        # Image out button
        self.imOutBtnGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.imOutBtnGroup.setGeometry(QtCore.QRect(650, 439, 191, 61))
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
        # Status bar
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.rightStatus = QLabel("Thread: N/A")
        self.statusBar.addPermanentWidget(self.rightStatus)
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
        self.imgFilterBox.setText(_translate("MainWindow", "Image Only Filter"))
        self.threadLbl.setText(_translate("MainWindow", "Thread"))
        self.imOutBtnGroup.setTitle(_translate("MainWindow", "Image Out Button"))
        self.prevImgBtn.setText(_translate("MainWindow", "<"))
        self.nextImgBtn.setText(_translate("MainWindow", ">"))

    # Slot functions
    # Image Input
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

    # Image Output
    def setImageOutput(self, fileName):
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(self.picOutLabel.width(), self.picOutLabel.height(), QtCore.Qt.KeepAspectRatio)
        self.picOutLabel.setPixmap(pixmap)
        self.picOutLabel.setAlignment(QtCore.Qt.AlignCenter)

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

    # Search Image
    def initializeMatcher(self):
        self.setStatusText("Precomputing vector norm from package...")
        # Create instance
        if self.fastAlgInp.isChecked():
            self.matcher.precalculateVector(fastAlgorithm=True)
        else:
            self.matcher.precalculateVector(fastAlgorithm=False)
        # Activate search button
        self.searchBtn.setEnabled(True)
        self.setStatusText("Initialization completed")

    def searchImage(self):
        self.setStatusText("Matching image...")
        # Deactivate search button
        self.searchBtn.setEnabled(False)
        try:    # test file existence
            if os.path.isfile(self.imgPathInp.text()):  # image test
                img = Image.open(self.imgPathInp.text())
                self.imgVector = self.extractor.extractImage(self.imgPathInp.text())
                # Setup search
                matchAlgorithm = ("euDist") if (self.matchAlgInp.currentIndex() == 0) else ("cosSim")
                self.matcher.matchThreader(self.imgVector, matchAlgorithm, self.topImgInp.value(), self.fastAlgInp.isChecked())
            else:
                self.dialogWindow("Open File", self.imgPathInp.text(), subtext="File not found!", type="Warning")
                self.setStatusText("Matching failed")
        except IOError:
            self.dialogWindow("Open File", self.imgPathInp.text(), subtext="File is not an image!", type="Warning")
            self.setStatusText("Matching failed")

    def srcProgBar(self, totalImage):
        self.pbSrc = QProgressDialog("Matching image...", "", 0, totalImage, self.centralwidget)
        self.pbSrc.setWindowTitle("Progress..")
        self.pbSrc.setCancelButton(None)
        self.pbSrc.setAttribute(Qt.WA_DeleteOnClose, True)
        self.pbSrc.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.pbSrc.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.pbSrc.setWindowFlag(Qt.WindowMinimizeButtonHint, True)

    def setSrcProgBarVal(self, progress):
        self.pbSrc.setValue(progress)

    def searchImageException(self, exception):
        print("Error: " + str(exception))

    def searchImageResult(self, res):
        self.simImgPath, self.simImgDist = res

    def searchImageDone(self):
        self.setStatusText("Matching completed")
        # Show Image Out and Create Image Index Property
        self.topImgMax = self.topImgInp.value() - 1
        self.topImgNow = 0
        self.setImageOutput(self.simImgPath[0])
        self.setStatusText(self.simImgPath[0] + "\tDistance: " + str(self.simImgDist[0]))
        # Redefine next and previous image button
        self.prevImgBtn.setEnabled(False)
        if self.topImgNow != self.topImgMax:
            self.nextImgBtn.setEnabled(True)
        else:
            self.nextImgBtn.setEnabled(False)
        # Activate search button
        self.searchBtn.setEnabled(True)
        # Close QProgressDialog if not closed
        self.pbSrc.close()

    # Extract Database
    def extractDatabase(self):
        self.setStatusText("Extracting vector from database...")
        try:
            self.extractor.extractBatchThreader("db", thread=self.threadInp.value(), checkImg=self.imgFilterBox.isChecked())
            self.setThreadStatusText(self.extractor.threadPool.activeThreadCount(),
                                        self.extractor.threadPool.maxThreadCount())
            self.extBtn.setEnabled(False)
        except Exception as e:
            self.setStatusText(str(e))
            self.dialogWindow("Extract Database", str(e), type="Warning")

    def extProgBar(self, totalImage):
        self.pbExt = QProgressDialog("Extracting images...", "Cancel", 0, totalImage, self.centralwidget)
        self.pbExt.setWindowTitle("Progress..")
        self.pbExt.setCancelButton(None)
        self.pbExt.setAttribute(Qt.WA_DeleteOnClose, True)
        self.pbExt.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.pbExt.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.pbExt.setWindowFlag(Qt.WindowMinimizeButtonHint, True)

    def setExtProgBarVal(self):
        print(self.pbExt.value() + 1)
        self.pbExt.setValue(self.pbExt.value() + 1)

    def extractDatabaseException(self, exception):
        print("Error: " + str(exception))

    def extractDatabaseStatus(self, activeThread, maxThread):
        self.setThreadStatusText(activeThread, maxThread)

    def extractDatabaseDone(self):
        self.setStatusText("Extraction finished")
        self.pbExt.close()
        self.extBtn.setEnabled(True)
        self.setThreadStatusText('N', 'A')

    # Misc
    def setStatusText(self, text):
        self.statusBar.showMessage(text)

    def setThreadStatusText(self, active, max):
        self.rightStatus.setText("Thread: {0}/{1}".format(active, max))

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
