#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beadando.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import math as m
from beadando_val import Values
from beadando_calc import Calculate
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def initSubClasses(self):
        self.V = Values()
        self.C = Calculate()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.termek_neve = QtWidgets.QLabel(self.centralwidget)
        self.termek_neve.setGeometry(QtCore.QRect(140, 22, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.termek_neve.setFont(font)
        self.termek_neve.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.termek_neve.setAlignment(QtCore.Qt.AlignCenter)
        self.termek_neve.setObjectName("termek_neve")
        self.alapanyag_1 = QtWidgets.QLabel(self.centralwidget)
        self.alapanyag_1.setGeometry(QtCore.QRect(20, 130, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alapanyag_1.setFont(font)
        self.alapanyag_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alapanyag_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alapanyag_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alapanyag_1.setObjectName("alapanyag_1")
        self.alapanyag_2 = QtWidgets.QLabel(self.centralwidget)
        self.alapanyag_2.setGeometry(QtCore.QRect(20, 180, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alapanyag_2.setFont(font)
        self.alapanyag_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alapanyag_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alapanyag_2.setObjectName("alapanyag_2")
        self.alapanyag_3 = QtWidgets.QLabel(self.centralwidget)
        self.alapanyag_3.setGeometry(QtCore.QRect(20, 230, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alapanyag_3.setFont(font)
        self.alapanyag_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alapanyag_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alapanyag_3.setObjectName("alapanyag_3")
        self.alapanyag_4 = QtWidgets.QLabel(self.centralwidget)
        self.alapanyag_4.setGeometry(QtCore.QRect(20, 280, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alapanyag_4.setFont(font)
        self.alapanyag_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alapanyag_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alapanyag_4.setObjectName("alapanyag_4")
        self.alapanyag_5 = QtWidgets.QLabel(self.centralwidget)
        self.alapanyag_5.setGeometry(QtCore.QRect(20, 330, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alapanyag_5.setFont(font)
        self.alapanyag_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alapanyag_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alapanyag_5.setObjectName("alapanyag_5")
        self.alapanyag_6 = QtWidgets.QLabel(self.centralwidget)
        self.alapanyag_6.setGeometry(QtCore.QRect(20, 380, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alapanyag_6.setFont(font)
        self.alapanyag_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.alapanyag_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alapanyag_6.setObjectName("alapanyag_6")
        self.beszerzesi_ar_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.beszerzesi_ar_1.setGeometry(QtCore.QRect(340, 140, 151, 31))
        self.beszerzesi_ar_1.setObjectName("beszerzesi_ar_1")
        self.beszerzesi_ar_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.beszerzesi_ar_2.setGeometry(QtCore.QRect(340, 190, 151, 31))
        self.beszerzesi_ar_2.setObjectName("beszerzesi_ar_2")
        self.beszerzesi_ar_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.beszerzesi_ar_3.setGeometry(QtCore.QRect(340, 240, 151, 31))
        self.beszerzesi_ar_3.setObjectName("beszerzesi_ar_3")
        self.beszerzesi_ar_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.beszerzesi_ar_4.setGeometry(QtCore.QRect(340, 290, 151, 31))
        self.beszerzesi_ar_4.setObjectName("beszerzesi_ar_4")
        self.beszerzesi_ar_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.beszerzesi_ar_5.setGeometry(QtCore.QRect(340, 340, 151, 31))
        self.beszerzesi_ar_5.setObjectName("beszerzesi_ar_5")
        self.idotartam = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.idotartam.setGeometry(QtCore.QRect(340, 390, 151, 31))
        self.idotartam.setObjectName("idotartam")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 520, 471, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 550, 471, 201))
        self.listWidget.setObjectName("listWidget")
        self.szamolas = QtWidgets.QPushButton(self.centralwidget)
        self.szamolas.setGeometry(QtCore.QRect(340, 480, 151, 31))
        self.szamolas.setObjectName("szamolas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.termek_neve.setText(_translate("MainWindow", "Rozskenyér"))
        self.alapanyag_1.setText(_translate("MainWindow", "Kenyérliszt beszerzési ára (Ft):"))
        self.alapanyag_2.setText(_translate("MainWindow", "Víz beszerzési ára (Ft):"))
        self.alapanyag_3.setText(_translate("MainWindow", "Instant élesztő beszerzési ára (Ft):"))
        self.alapanyag_4.setText(_translate("MainWindow", "Só beszerzési ára (Ft):"))
        self.alapanyag_5.setText(_translate("MainWindow", "Finomliszt beszerzési ára (Ft):"))
        self.alapanyag_6.setText(_translate("MainWindow", "Elkészítési idő (Aé. 14 óra):"))
        self.szamolas.setText(_translate("MainWindow", "Számol!"))
    
    def Configure(self):
        self.szamolas.clicked.connect(self.showValues)
    
    
    def showValues(self):
        self.C.storeValues(self.V,
                           self.beszerzesi_ar_1.toPlainText(),
                           self.beszerzesi_ar_2.toPlainText(),
                           self.beszerzesi_ar_3.toPlainText(),
                           self.beszerzesi_ar_4.toPlainText(),
                           self.beszerzesi_ar_5.toPlainText(),
                           self.idotartam.toPlainText())
        element = self.C.calculateValues(self.V)
        result = QtWidgets.QListWidgetItem(element)
        self.listWidget.addItem(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.initSubClasses()
    ui.setupUi(MainWindow)
    ui.Configure()
    MainWindow.show()
    sys.exit(app.exec_())