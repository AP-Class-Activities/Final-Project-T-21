from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(126, 126, 126);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(470, 80, 271, 121))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(410, 190, 371, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.background)
        self.pushButton.setGeometry(QtCore.QRect(440, 320, 311, 81))
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.background)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 430, 311, 81))
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Wellcome"))
        self.label_2.setText(_translate("Dialog", "Sign in or create a new account"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
