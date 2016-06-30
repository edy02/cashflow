# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(836, 656)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tblVypis = QtGui.QTableWidget(self.centralwidget)
        self.tblVypis.setGeometry(QtCore.QRect(260, 0, 571, 211))
        self.tblVypis.setLineWidth(1)
        self.tblVypis.setObjectName(_fromUtf8("tblVypis"))
        self.tblVypis.setColumnCount(5)
        self.tblVypis.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblVypis.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblVypis.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblVypis.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblVypis.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblVypis.setHorizontalHeaderItem(4, item)
        self.btnSmazat = QtGui.QPushButton(self.centralwidget)
        self.btnSmazat.setGeometry(QtCore.QRect(260, 230, 75, 23))
        self.btnSmazat.setObjectName(_fromUtf8("btnSmazat"))
        self.btnPrepocitat = QtGui.QPushButton(self.centralwidget)
        self.btnPrepocitat.setGeometry(QtCore.QRect(350, 230, 75, 23))
        self.btnPrepocitat.setObjectName(_fromUtf8("btnPrepocitat"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 261, 211))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txtPredmet = QtGui.QLineEdit(self.frame)
        self.txtPredmet.setObjectName(_fromUtf8("txtPredmet"))
        self.gridLayout.addWidget(self.txtPredmet, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBoxPohyb = QtGui.QSpinBox(self.frame)
        self.spinBoxPohyb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBoxPohyb.setMinimum(-1000000)
        self.spinBoxPohyb.setMaximum(1000000)
        self.spinBoxPohyb.setSingleStep(100)
        self.spinBoxPohyb.setProperty("value", 0)
        self.spinBoxPohyb.setObjectName(_fromUtf8("spinBoxPohyb"))
        self.gridLayout.addWidget(self.spinBoxPohyb, 1, 1, 1, 1)
        self.btnZapis = QtGui.QPushButton(self.frame)
        self.btnZapis.setObjectName(_fromUtf8("btnZapis"))
        self.gridLayout.addWidget(self.btnZapis, 2, 1, 1, 1)
        self.matplot = MatplotlibWidget(self.centralwidget)
        self.matplot.setGeometry(QtCore.QRect(260, 270, 571, 300))
        self.matplot.setObjectName(_fromUtf8("matplot"))
        self.btnZapis.raise_()
        self.spinBoxPohyb.raise_()
        self.txtPredmet.raise_()
        self.btnZapis.raise_()
        self.spinBoxPohyb.raise_()
        self.label.raise_()
        self.txtPredmet.raise_()
        self.label_2.raise_()
        self.btnZapis.raise_()
        self.spinBoxPohyb.raise_()
        self.label.raise_()
        self.txtPredmet.raise_()
        self.label_2.raise_()
        self.tblVypis.raise_()
        self.btnSmazat.raise_()
        self.btnPrepocitat.raise_()
        self.frame.raise_()
        self.matplot.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tblVypis.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Datum", None))
        item = self.tblVypis.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Čas", None))
        item = self.tblVypis.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Předmět", None))
        item = self.tblVypis.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Pohyb", None))
        item = self.tblVypis.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Na účtě", None))
        self.btnSmazat.setText(_translate("MainWindow", "Smazat řádek", None))
        self.btnPrepocitat.setText(_translate("MainWindow", "Přepočítat", None))
        self.label.setText(_translate("MainWindow", "Za co:", None))
        self.label_2.setText(_translate("MainWindow", "Pohyb:", None))
        self.btnZapis.setText(_translate("MainWindow", "Zapiš", None))

from matplotlibwidget import MatplotlibWidget
