# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choose_FaceLM.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_landmarks_count = QtWidgets.QLabel(self.centralwidget)
        self.label_landmarks_count.setGeometry(QtCore.QRect(50, 570, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_landmarks_count.setFont(font)
        self.label_landmarks_count.setObjectName("label_landmarks_count")
        self.btn_iterator_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iterator_check.setGeometry(QtCore.QRect(380, 590, 191, 51))
        self.btn_iterator_check.setObjectName("btn_iterator_check")
        self.pic_view_1 = QtWidgets.QLabel(self.centralwidget)
        self.pic_view_1.setGeometry(QtCore.QRect(80, 120, 58, 15))
        self.pic_view_1.setObjectName("pic_view_1")
        self.pic_view_2 = QtWidgets.QLabel(self.centralwidget)
        self.pic_view_2.setGeometry(QtCore.QRect(480, 90, 411, 351))
        self.pic_view_2.setText("")
        self.pic_view_2.setPixmap(QtGui.QPixmap("images/DLIB_landmarks_small.jpg"))
        self.pic_view_2.setObjectName("pic_view_2")
        self.btn_load_pic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_pic.setGeometry(QtCore.QRect(60, 20, 131, 51))
        self.btn_load_pic.setObjectName("btn_load_pic")
        self.btn_load_landmarks = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_landmarks.setGeometry(QtCore.QRect(220, 20, 131, 51))
        self.btn_load_landmarks.setObjectName("btn_load_landmarks")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.load_image = QtWidgets.QAction(MainWindow)
        self.load_image.setObjectName("load_image")
        self.load_landmarks = QtWidgets.QAction(MainWindow)
        self.load_landmarks.setObjectName("load_landmarks")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_landmarks_count.setText(_translate("MainWindow", "目前已選取特徵點總數 : "))
        self.btn_iterator_check.setText(_translate("MainWindow", "檢測人臉特徵點"))
        self.pic_view_1.setText(_translate("MainWindow", "TextLabel"))
        self.btn_load_pic.setText(_translate("MainWindow", "讀取圖片"))
        self.btn_load_landmarks.setText(_translate("MainWindow", "讀取人臉特徵點(*.txt)"))
        self.menu.setTitle(_translate("MainWindow", "檔案"))
        self.load_image.setText(_translate("MainWindow", "讀取圖片"))
        self.load_landmarks.setText(_translate("MainWindow", "讀取Landmarks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

