# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\KULIAH\SEMESTER 3\Algeo\Tubes 2\AlgeoTubes2\main_front.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
<<<<<<< HEAD
        MainWindow.setObjectName("FaceRecognition")
        MainWindow.resize(869, 638)
=======
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 641)
>>>>>>> 3defaa92ca504727a717c5fad66875ccd3e40569
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(-10, -10, 881, 661))
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
        self.searchGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.searchGroup.setGeometry(QtCore.QRect(30, 440, 591, 191))
        self.searchGroup.setObjectName("searchGroup")
        self.formLayoutWidget = QtWidgets.QWidget(self.searchGroup)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 551, 115))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.srcFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.srcFormLayout.setContentsMargins(0, 0, 0, 0)
        self.srcFormLayout.setObjectName("srcFormLayout")
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
        self.topImgInp = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.topImgInp.setObjectName("topImgInp")
        self.srcFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.topImgInp)
        self.matchAlgInp = QtWidgets.QComboBox(self.formLayoutWidget)
        self.matchAlgInp.setObjectName("matchAlgInp")
        self.srcFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.matchAlgInp)
        self.fastAlgLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.fastAlgLbl.setObjectName("fastAlgLbl")
        self.srcFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.fastAlgLbl)
        self.fastAlgInp = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.fastAlgInp.setEnabled(True)
        self.fastAlgInp.setText("")
        self.fastAlgInp.setObjectName("fastAlgInp")
        self.srcFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fastAlgInp)
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
        self.initBtn = QtWidgets.QPushButton(self.searchGroup)
        self.initBtn.setGeometry(QtCore.QRect(120, 150, 93, 28))
        self.initBtn.setObjectName("initBtn")
        self.searchBtn = QtWidgets.QPushButton(self.searchGroup)
        self.searchBtn.setGeometry(QtCore.QRect(20, 150, 93, 28))
        self.searchBtn.setObjectName("searchBtn")
        self.ImInGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.ImInGroup.setGeometry(QtCore.QRect(60, 50, 351, 381))
        self.ImInGroup.setObjectName("ImInGroup")
        self.picInLabel = QtWidgets.QLabel(self.ImInGroup)
        self.picInLabel.setGeometry(QtCore.QRect(10, 30, 331, 341))
        self.picInLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.picInLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picInLabel.setObjectName("picInLabel")
        self.ImOutGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.ImOutGroup.setGeometry(QtCore.QRect(460, 50, 351, 381))
        self.ImOutGroup.setObjectName("ImOutGroup")
        self.picOutLabel = QtWidgets.QLabel(self.ImOutGroup)
        self.picOutLabel.setGeometry(QtCore.QRect(10, 30, 331, 341))
        self.picOutLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.picOutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.picOutLabel.setObjectName("picOutLabel")
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
        self.threadInp.setObjectName("threadInp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.threadInp)
        self.imOutBtnGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.imOutBtnGroup.setGeometry(QtCore.QRect(650, 439, 191, 61))
        self.imOutBtnGroup.setObjectName("imOutBtnGroup")
        self.prevImgBtn = QtWidgets.QPushButton(self.imOutBtnGroup)
        self.prevImgBtn.setGeometry(QtCore.QRect(30, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        self.prevImgBtn.setFont(font)
        self.prevImgBtn.setObjectName("prevImgBtn")
        self.nextImgBtn = QtWidgets.QPushButton(self.imOutBtnGroup)
        self.nextImgBtn.setGeometry(QtCore.QRect(100, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(14)
        self.nextImgBtn.setFont(font)
        self.nextImgBtn.setObjectName("nextImgBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backgroundLabel.setText(_translate("MainWindow", "TextLabel"))
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
        self.picInLabel.setText(_translate("MainWindow", "TextLabel"))
        self.ImOutGroup.setTitle(_translate("MainWindow", "Image Out"))
        self.picOutLabel.setText(_translate("MainWindow", "TextLabel"))
        self.extGroup.setTitle(_translate("MainWindow", "Database"))
        self.extBtn.setText(_translate("MainWindow", "Extract"))
        self.imgFilterBox.setText(_translate("MainWindow", "Image Only Filter"))
        self.threadLbl.setText(_translate("MainWindow", "Thread"))
        self.imOutBtnGroup.setTitle(_translate("MainWindow", "Image Out Button"))
        self.prevImgBtn.setText(_translate("MainWindow", "<"))
        self.nextImgBtn.setText(_translate("MainWindow", ">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
