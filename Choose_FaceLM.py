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
    __img1_location = (0, 115)
    __cur_landmarks_count = 0
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("人臉特徵點小工具")
        self.btn_load_pic.clicked.connect(self.load_image_to_pic_view_1)
        # set default image
        default_img = cv2.imread("elsa_big.jpg")
        self.pic_view_1.resize(default_img.shape[0], default_img.shape[1])
        self.pic_view_1.setPixmap(self.mat2pix(default_img))
        self.dlib_img = cv2.imread("DLIB_landmarks_small.jpg")
        self.pic_view_2.resize(self.dlib_img.shape[0], self.dlib_img.shape[1])
        self.pic_view_2.setPixmap(self.mat2pix(self.dlib_img))
        self.reset_image(default_img)
        self.dlib_pic_ex_landmarks()
        # show next point tip
        image = self.dlib_img.copy()
        self.draw_circles(image, self.dlib_landmarks[:self.__cur_landmarks_count + 1])
        self.pic_view_2.setPixmap(self.mat2pix(image))

    def dlib_pic_ex_landmarks(self):
        self.dlib_landmarks = []
        landmarks_file = open("DLIB_landmarks_small_pos.txt", "r")
        lines = landmarks_file.read().split("\n")
        for line in lines:
            x, y = line.split(" ")
            self.dlib_landmarks.append((x, y))
        landmarks_file.close()

    def is_cursor_in_img1(self):
        if(self.x >= self.__img1_location[0] and self.x <= self.__img1_location[0] + self.pic_view_1.width()) and (self.y >= self.__img1_location[1] and self.y <= self.__img1_location[1] + self.pic_view_1.height()):
            print("in img 1 ")
            return True
        return False

    def mat2pix(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return(QtGui.QPixmap(QtGui.QImage(image, image.shape[1], image.shape[0],
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

    def draw_circles(self, image, landmarks):
        for landmark in landmarks:
            x, y = int(landmark[0]) , int(landmark[1])
            cv2.circle(image, (x, y), 5, (9,90, 255), -1)

    def draw(self):
        if(self.is_cursor_in_img1()):
            print("success")
            # offset margin
            x = self.x - self.__img1_location[0]
            y = self.y - self.__img1_location[1]
            # img1
            image = self.img.copy()
            self.landmarks.append((x, y))
            self.draw_circles(image, self.landmarks)
            self.pic_view_1.setPixmap(self.mat2pix(image))
            self.__cur_landmarks_count += 1
            self.label_landmarks_count.setText("目前已選取特徵點總數 : %d" % self.__cur_landmarks_count)
            # img2
            image = self.dlib_img.copy()
            self.draw_circles(image, self.dlib_landmarks[self.__cur_landmarks_count :self.__cur_landmarks_count + 1])
            self.pic_view_2.setPixmap(self.mat2pix(image))
            print("x = %d, y = %d" % (x, y))

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