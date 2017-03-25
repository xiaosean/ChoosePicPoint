#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI import Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    ''' 
    ui and code
    I can not handle menu bar
    
    '''
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("人臉特徵點小工具")
        self.btn_load_pic.clicked.connect(self.load_image_to_pic_view_1)
        # self.pic_view_2-.setPixmap(QtGui.QPixmap("./images/DLIB_landmarks_small.jpg"))
        # self.IP_line.setText(getIP().get_NTUST_IP())
        # self.auto_search.clicked.connect(self.OnAlert)
        # self.query_Button.clicked.connect(self.search_code)
        # self.favor_Button.clicked.connect(self.Add_favor)
    # def combo_value(self):clicked
    #     print(self.query_comboBox.currentText())
    #     print(self.query_comboBox.currentIndex())
    def load_image2(self):
        print("123")
    def load_image_to_pic_view_1(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath())
        print("filename", fileName)
        if fileName:
            image = QtGui.QImage(fileName[0])
            if image.isNull():
                QtGui.QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
            else:
                self.pic_view_1.setPixmap(QtGui.QPixmap(image))
    def OnAlert(self):
        QMessageBox.about( self, "alert", "About" )
def mainwindow():
    app = QtWidgets.QApplication(sys.argv)
    Ui = MainWindow()
    Ui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    mainwindow()