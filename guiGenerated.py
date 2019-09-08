# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataAnalysisGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MPLWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 856)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = MPLWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 100, 641, 261))
        self.widget.setObjectName("widget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 20, 131, 541))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 30, 80, 511))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.acelX = QtWidgets.QCheckBox(self.splitter)
        self.acelX.setObjectName("acelX")
        self.acelY = QtWidgets.QCheckBox(self.splitter)
        self.acelY.setObjectName("acelY")
        self.acelZ = QtWidgets.QCheckBox(self.splitter)
        self.acelZ.setObjectName("acelZ")
        self.velDD = QtWidgets.QCheckBox(self.splitter)
        self.velDD.setObjectName("velDD")
        self.velT = QtWidgets.QCheckBox(self.splitter)
        self.velT.setObjectName("velT")
        self.sparkCut = QtWidgets.QCheckBox(self.splitter)
        self.sparkCut.setObjectName("sparkCut")
        self.suspPos = QtWidgets.QCheckBox(self.splitter)
        self.suspPos.setObjectName("suspPos")
        self.oleoP = QtWidgets.QCheckBox(self.splitter)
        self.oleoP.setObjectName("oleoP")
        self.fuelP = QtWidgets.QCheckBox(self.splitter)
        self.fuelP.setObjectName("fuelP")
        self.tps = QtWidgets.QCheckBox(self.splitter)
        self.tps.setObjectName("tps")
        self.rearBrakeP = QtWidgets.QCheckBox(self.splitter)
        self.rearBrakeP.setObjectName("rearBrakeP")
        self.frontBrakeP = QtWidgets.QCheckBox(self.splitter)
        self.frontBrakeP.setObjectName("frontBrakeP")
        self.volPos = QtWidgets.QCheckBox(self.splitter)
        self.volPos.setObjectName("volPos")
        self.beacon = QtWidgets.QCheckBox(self.splitter)
        self.beacon.setObjectName("beacon")
        self.correnteBat = QtWidgets.QCheckBox(self.splitter)
        self.correnteBat.setObjectName("correnteBat")
        self.ect = QtWidgets.QCheckBox(self.splitter)
        self.ect.setObjectName("ect")
        self.batVoltage = QtWidgets.QCheckBox(self.splitter)
        self.batVoltage.setObjectName("batVoltage")
        self.releBomba = QtWidgets.QCheckBox(self.splitter)
        self.releBomba.setObjectName("releBomba")
        self.releVent = QtWidgets.QCheckBox(self.splitter)
        self.releVent.setObjectName("releVent")
        self.pduTemp = QtWidgets.QCheckBox(self.splitter)
        self.pduTemp.setObjectName("pduTemp")
        self.tempDiscoD = QtWidgets.QCheckBox(self.splitter)
        self.tempDiscoD.setObjectName("tempDiscoD")
        self.tempDiscoE = QtWidgets.QCheckBox(self.splitter)
        self.tempDiscoE.setObjectName("tempDiscoE")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 907, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QtWidgets.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.menuFile.addAction(self.actionOpenFile)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.acelX.setText(_translate("MainWindow", "acelX"))
        self.acelY.setText(_translate("MainWindow", "acelY"))
        self.acelZ.setText(_translate("MainWindow", "acelZ"))
        self.velDD.setText(_translate("MainWindow", "velDD"))
        self.velT.setText(_translate("MainWindow", "velT"))
        self.sparkCut.setText(_translate("MainWindow", "sparkCut"))
        self.suspPos.setText(_translate("MainWindow", "suspPos"))
        self.oleoP.setText(_translate("MainWindow", "oleoP"))
        self.fuelP.setText(_translate("MainWindow", "fuelP"))
        self.tps.setText(_translate("MainWindow", "tps"))
        self.rearBrakeP.setText(_translate("MainWindow", "rearBrakeP"))
        self.frontBrakeP.setText(_translate("MainWindow", "frontBrakeP"))
        self.volPos.setText(_translate("MainWindow", "volPos"))
        self.beacon.setText(_translate("MainWindow", "beacon"))
        self.correnteBat.setText(_translate("MainWindow", "correnteBat"))
        self.ect.setText(_translate("MainWindow", "ect"))
        self.batVoltage.setText(_translate("MainWindow", "batVoltage"))
        self.releBomba.setText(_translate("MainWindow", "releBomba"))
        self.releVent.setText(_translate("MainWindow", "releVent"))
        self.pduTemp.setText(_translate("MainWindow", "pduTemp"))
        self.tempDiscoD.setText(_translate("MainWindow", "tempDiscoD"))
        self.tempDiscoE.setText(_translate("MainWindow", "tempDiscoE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpenFile.setText(_translate("MainWindow", "Open"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())