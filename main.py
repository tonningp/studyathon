#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt,QRectF,QRect,QPoint
import sys, random

class Example(QWidget):
    
    def __init__(self,x=512,y=512,ball_width=50,ball_height=50):
        super().__init__()
        self.x = x
        self.y = y
        self.ball_width = ball_width
        self.ball_height = ball_height
        self.setPoint(x,y)
        self.initUI()
        
        
    def initUI(self):      

        self.setGeometry(0, 0, 1024, 1024)
        self.setWindowTitle('Tracker')
        

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBall(qp)
        qp.end()
        

    def setPoint(self,x,y): 
        self.x = x-self.ball_width/2
        self.y = y-self.ball_height/2
        self.ball = QRect(self.x,self.y,self.ball_width, self.ball_height)
        self.repaint()

    def drawBall(self, qp):
      
        qp.setPen(Qt.blue)
        qp.setBrush(Qt.blue)
        qp.drawEllipse(self.ball)
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.setPoint(ex.width()/2,ex.height()/2)
    ex.show()
    sys.exit(app.exec_())
