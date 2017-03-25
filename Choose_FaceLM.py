#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import cv2
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


        default_img = cv2.imread("elsa_big.jpg")
        self.pic_view_1.resize(default_img.shape[0], default_img.shape[1])
        self.pic_view_1.setPixmap(self.mat2pix(default_img))
        self.reset_image(default_img)

    def mat2pix(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return(QtGui.QPixmap(QtGui.QImage(image, image.shape[0], image.shape[1],
                                  QtGui.QImage.Format_RGB888)))
    def load_image_to_pic_view_1(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath())
        print("filename", fileName)
        if fileName:
            image = cv2.imread(fileName[0])
            if not image is None :
                self.reset_image(image)
                self.pic_view_1.resize(image.shape[0], image.shape[1])
                self.pic_view_1.setPixmap(self.mat2pix(image))
            
    def reset_image(self, image):
        self.img = image
        self.landmarks = []
        print("image postion = %d, %d" % ())
    def draw(self):
        print("x = %d, y = %d" % (self.x, self.y))
        # cv2.circle(img,(447,63), 63, (0,0,255), -1)

    def mousePressEvent(self,event):
        self.x , self.y = event.pos().x() , event.pos().y()
        self.draw()
        self.statusbar.showMessage("%f , %f" % (self.x,self.y))
    def OnAlert(self):
        QMessageBox.about( self, "alert", "About" )
def mainwindow():
    app = QtWidgets.QApplication(sys.argv)
    Ui = MainWindow()
    Ui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    mainwindow()