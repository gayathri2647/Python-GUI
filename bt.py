# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form1(object):
    def setupUi(self, form1):
        form1.setObjectName("form1")
        form1.resize(669, 339)
        self.l1 = QtWidgets.QLabel(form1)
        self.l1.setGeometry(QtCore.QRect(0, 20, 671, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(form1)
        self.l2.setGeometry(QtCore.QRect(140, 100, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(form1)
        self.l3.setGeometry(QtCore.QRect(140, 170, 171, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l3.setObjectName("l3")
        self.cb1 = QtWidgets.QComboBox(form1)
        self.cb1.setGeometry(QtCore.QRect(320, 170, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cb1.setFont(font)
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.cb1.addItem("")
        self.l4 = QtWidgets.QLabel(form1)
        self.l4.setGeometry(QtCore.QRect(220, 260, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.l4.setFont(font)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4.setObjectName("l4")

        self.retranslateUi(form1)
        QtCore.QMetaObject.connectSlotsByName(form1)
        #my work
        self.cb1.currentIndexChanged.connect(self.fn1)

    def fn1(self):
        a=self.cb1.currentText()
        if a=="NON AC SEATER":
            self.l4.setText("Rs.700")
        elif a=="AC SEATER":
            self.l4.setText("Rs.900")
        elif a=="NON AC SLEEPER":
            self.l4.setText("Rs.950")
        elif a=="AC SLEEPER":
            self.l4.setText("Rs.1200")
        

    def retranslateUi(self, form1):
        _translate = QtCore.QCoreApplication.translate
        form1.setWindowTitle(_translate("form1", "BUS TICKET PRICE"))
        self.l1.setText(_translate("form1", "NAGERCOIL TO CHENNAI"))
        self.l2.setText(_translate("form1", "BUS TICKET RATE"))
        self.l3.setText(_translate("form1", "Select Type:"))
        self.cb1.setItemText(0, _translate("form1", "NON AC SEATER"))
        self.cb1.setItemText(1, _translate("form1", "AC SEATER"))
        self.cb1.setItemText(2, _translate("form1", "NON AC SLEEPER"))
        self.cb1.setItemText(3, _translate("form1", "AC SLEEPER"))
        self.l4.setText(_translate("form1", "Rs. 700"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QWidget()
    ui = Ui_form1()
    ui.setupUi(form1)
    form1.show()
    sys.exit(app.exec_())
