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
        MainWindow.resize(1156, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_landmarks_count = QtWidgets.QLabel(self.centralwidget)
        self.label_landmarks_count.setGeometry(QtCore.QRect(700, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_landmarks_count.setFont(font)
        self.label_landmarks_count.setObjectName("label_landmarks_count")
        self.btn_load_pic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_pic.setGeometry(QtCore.QRect(20, 20, 131, 51))
        self.btn_load_pic.setObjectName("btn_load_pic")
        self.btn_load_landmarks = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_landmarks.setGeometry(QtCore.QRect(170, 20, 211, 51))
        self.btn_load_landmarks.setObjectName("btn_load_landmarks")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 1221, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_pic = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_pic.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout_pic.setContentsMargins(0, 0, 0, 0)
        self.layout_pic.setObjectName("layout_pic")
        self.pic_view_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pic_view_1.setObjectName("pic_view_1")
        self.layout_pic.addWidget(self.pic_view_1)
        self.pic_view_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pic_view_2.setText("")
        self.pic_view_2.setObjectName("pic_view_2")
        self.layout_pic.addWidget(self.pic_view_2)
        self.btn_delete_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_point.setGeometry(QtCore.QRect(530, 20, 131, 51))
        self.btn_delete_point.setObjectName("btn_delete_point")
        self.btn_load_landmarks_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_landmarks_3.setGeometry(QtCore.QRect(390, 20, 131, 51))
        self.btn_load_landmarks_3.setObjectName("btn_load_landmarks_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 25))
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
        self.btn_load_pic.setText(_translate("MainWindow", "讀取圖片"))
        self.btn_load_landmarks.setText(_translate("MainWindow", "讀取人臉特徵點(*.txt)"))
        self.pic_view_1.setText(_translate("MainWindow", "TextLabel"))
        self.btn_delete_point.setText(_translate("MainWindow", "刪除上一個點"))
        self.btn_load_landmarks_3.setText(_translate("MainWindow", "輸出人臉特徵點(*.txt)"))
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

