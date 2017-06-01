# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created: Thu Jun  1 14:57:57 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import sys
import time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

count1 = 0
count2 = 0
count3 = 0
count4 = 0
GPIO.setmode(GPIO.BOARD)

class Ui_Form(QWidget):
   def __init__(self):
        super().__init__();
        self.player = QMediaPlayer(self)
        self.ui = Prog()
        self.ui.start()
        self.ui.valueUp.connect(self.updateCounter)
        self.ui.valueUp2.connect(self.updateCounter2)
        self.ui.valueUp3.connect(self.updateCounter3)
        self.ui.valueUp4.connect(self.updateCounter4)
        self.setupUi(self)
        
   def updateCounter(self, value):
      self.lcdNumber_4.display(str(value))
    
   def updateCounter2(self,value2):
      self.lcdNumber_5.display(str(value2))
    	
   def updateCounter3(self, value3):
      self.lcdNumber.display(str(value3))
    	
   def updateCounter4(self, value4):
      self.lcdNumber_3.display(str(value4))
 
  
   def setupUi(self, Form):
      Form.setObjectName("Form")
      self.window = Form
      Form.resize(1196, 722)
      self.label = QtWidgets.QLabel(Form)
      self.label.setGeometry(QtCore.QRect(103, 170, 101, 21))
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      self.label.setFont(font)
      self.label.setObjectName("label")
      self.label_2 = QtWidgets.QLabel(Form)
      self.label_2.setGeometry(QtCore.QRect(100, 110, 261, 21))
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      self.label_2.setFont(font)
      self.label_2.setObjectName("label_2")
      self.label_3 = QtWidgets.QLabel(Form)
      self.label_3.setGeometry(QtCore.QRect(340, 170, 101, 21))
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      self.label_3.setFont(font)
      self.label_3.setObjectName("label_3")
      self.label_4 = QtWidgets.QLabel(Form)
      self.label_4.setGeometry(QtCore.QRect(220, 530, 101, 21))
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      self.label_4.setFont(font)
      self.label_4.setObjectName("label_4")
      self.label_6 = QtWidgets.QLabel(Form)
      self.label_6.setGeometry(QtCore.QRect(880, 530, 68, 21))
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      self.label_6.setFont(font)
      self.label_6.setObjectName("label_6")
      
      self.pushButton = QtWidgets.QPushButton(Form)
      self.pushButton.setGeometry(QtCore.QRect(720, 400, 101, 41))
      self.pushButton.setObjectName("pushButton")
      self.pushButton_2 = QtWidgets.QPushButton(Form)
      self.pushButton_2.setGeometry(QtCore.QRect(930, 400, 101, 41))
      self.pushButton_2.setObjectName("pushButton_2")
      self.lcdNumber = QtWidgets.QLCDNumber(Form)
      self.lcdNumber.setGeometry(QtCore.QRect(40, 560, 241, 111))
      self.lcdNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
      self.lcdNumber.setObjectName("lcdNumber")
      self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
      self.lcdNumber_3.setGeometry(QtCore.QRect(680, 560, 241, 111))
      self.lcdNumber_3.setLayoutDirection(QtCore.Qt.RightToLeft)
      self.lcdNumber_3.setObjectName("lcdNumber_3")
      self.line = QtWidgets.QFrame(Form)
      self.line.setGeometry(QtCore.QRect(0, 490, 1201, 16))
      self.line.setFrameShape(QtWidgets.QFrame.HLine)
      self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
      self.line.setObjectName("line")
      self.line_2 = QtWidgets.QFrame(Form)
      self.line_2.setGeometry(QtCore.QRect(540, 490, 20, 221))
      self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
      self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
      self.line_2.setObjectName("line_2")
      self.line_3 = QtWidgets.QFrame(Form)
      self.line_3.setGeometry(QtCore.QRect(540, 0, 20, 501))
      self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
      self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
      self.line_3.setObjectName("line_3")
      
      self.videoWidget  = QVideoWidget(Form)
      self.videoWidget.setGeometry(QtCore.QRect(580,30,581,291))
		
      self.player.setVideoOutput(self.videoWidget)     
      

      

     # self.graphicsView = QtWidgets.QGraphicsView(Form)
     # self.graphicsView.setGeometry(QtCore.QRect(580, 30, 581, 291))
     # self.graphicsView.setObjectName("graphicsView")
      self.lcdNumber_4 = QtWidgets.QLCDNumber(Form)
      self.lcdNumber_4.setGeometry(QtCore.QRect(40, 200, 181, 101))
      self.lcdNumber_4.setObjectName("lcdNumber_4")
      self.lcdNumber_5 = QtWidgets.QLCDNumber(Form)
      self.lcdNumber_5.setGeometry(QtCore.QRect(290, 200, 181, 101))
      self.lcdNumber_5.setObjectName("lcdNumber_5")
      
      self.pushButton.clicked.connect(self.pushButtonClick)
      self.pushButton_2.clicked.connect(self.playButtonClick)
      
      self.retranslateUi(Form)
      QtCore.QMetaObject.connectSlotsByName(Form)
	 	
   def pushButtonClick(self):
      import os
      fileName = QFileDialog.getOpenFileName(None,'Open',os.curdir,'MP4 Files (*.mp4)','*.mp4')
      if len(fileName[0])>0:
         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(fileName[0])))
      if self.player.state() == QMediaPlayer.PlayingState:self.player.stop()
     
   def playButtonClick(self):
   	self.player.play()
   	self.setPlayingMode(True)


	 	
   def retranslateUi(self, Form):
       _translate = QtCore.QCoreApplication.translate
       Form.setWindowTitle(_translate("Form", "Teller Bank - Republic of IoT"))
       self.label.setText(_translate("Form", "TELLER :"))
       self.label_2.setText(_translate("Form", "NOMOR ANTRIAN :"))
       self.label_3.setText(_translate("Form", "CS :"))
       self.label_4.setText(_translate("Form", "TELLER :"))
       self.label_6.setText(_translate("Form", "CS :"))
       self.pushButton.setText(_translate("Form", "Open"))
       self.pushButton_2.setText(_translate("Form", "Play"))
	 	 
class Prog(QtCore.QThread):
   valueUp = QtCore.pyqtSignal(int)
   valueUp2 = QtCore.pyqtSignal(int)
   valueUp3 = QtCore.pyqtSignal(int)
   valueUp4 = QtCore.pyqtSignal(int)
	
   def run(self):
      count1 = 0
      count2 = 0
      count3 = 0
      count4 = 0
      switch_pin = 40
      switch_pin2 = 11
      switch_pin3 = 12
      switch_pin4 = 13
      GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(switch_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(switch_pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(switch_pin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      button_state = False
      button2_state = False
      button3_state = False
      button4_state = False
      old_input1_state = True
      old_input2_state = True
      old_input3_state = True
      old_input4_state = True
      while True:
         new_input_state = GPIO.input(switch_pin)
         new_input2_state = GPIO.input(switch_pin2)
         new_input3_state = GPIO.input(switch_pin3)
         new_input4_state = GPIO.input(switch_pin4)
         if new_input_state == False and old_input_state ==True:
            button_state = not button_state
            count1+=1
            self.valueUp.emit(count1)
         elif new_input2_state == False and old_input2_state == True:
            button2_state = not button2_state
            count2+=1
            self.valueUp2.emit(count2)
         elif new_input3_state == False and old_input3_state == True:
            if count1>count3:
               count3+=1
               self.valueUp3.emit(count3)
         elif new_input4_state == False and old_input4_state == True:
            if count2>count4:
               count4+=1
               self.valueUp4.emit(count4)
					
         old_input_state = new_input_state
         old_input2_state = new_input2_state 
         old_input3_state = new_input3_state 
         old_input4_state = new_input4_state
         


if __name__=='__main__':
    Program =  QtWidgets.QApplication(sys.argv)
    MyProg = Ui_Form()
    MyProg.show()
    sys.exit(Program.exec_())