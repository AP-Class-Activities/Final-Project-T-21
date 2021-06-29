from PyQt5 import QtCore, QtGui, QtWidgets

class LoginOperator(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(520, 70, 141, 121))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
                                 "color:rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(400, 190, 381, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                   "color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.finallogin = QtWidgets.QPushButton(self.background)
        self.finallogin.setGeometry(QtCore.QRect(430, 510, 311, 81))
        self.finallogin.setStyleSheet("border-radius:20px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 18pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(100, 15, 142);")
        self.finallogin.setObjectName("finallogin")
        self.UserLine = QtWidgets.QLineEdit(self.background)
        self.UserLine.setGeometry(QtCore.QRect(420, 300, 341, 51))
        self.UserLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";")
        self.UserLine.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.UserLine.setObjectName("UserLine")
        self.PassLine = QtWidgets.QLineEdit(self.background)
        self.PassLine.setGeometry(QtCore.QRect(420, 400, 341, 51))
        self.PassLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";")
        self.PassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassLine.setObjectName("PassLine")
        self.label_3 = QtWidgets.QLabel(self.background)
        self.label_3.setGeometry(QtCore.QRect(420, 260, 81, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.background)
        self.label_4.setGeometry(QtCore.QRect(420, 360, 81, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.LogLabel = QtWidgets.QLabel(self.background)
        self.LogLabel.setGeometry(QtCore.QRect(471, 610, 351, 61))
        self.LogLabel.setStyleSheet("color: rgb(255, 0, 4);\n"
                                   "\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.LogLabel.setText("")
        self.LogLabel.setObjectName("LogLabel")
        self.backtowelcome = QtWidgets.QPushButton(self.background)
        self.backtowelcome.setGeometry(QtCore.QRect(410, 460, 141, 31))
        self.backtowelcome.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                         "text-decoration: underline;\n"
                                         "color: rgb(179, 179, 179);\n"
                                         "border-radius:20px;")
        self.backtowelcome.setObjectName("backtowelcome")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.finallogin.clicked.connect(self.LoginOper)

    def LoginOper(self):
        OperatorUsername = self.UserLine.text()
        OperatorPassword = self.PassLine.text()
        users = open("OperatorData.txt","r")
        users = users.readlines()
        users = [u.replace('\n','').split() for u in users]
        flag = False
        for i in range(len(users)):
            if OperatorUsername == users[i][0] and OperatorPassword == users[i][1]:
                flag = True
                self.LogLabel.setText("Login Succesful")
                break
        if flag == False:
            self.LogLabel.setText("Username and Password invalid")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Sign into operator account"))
        self.finallogin.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))


class LoginAs(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(380, 220, 411, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.buttonoperator = QtWidgets.QPushButton(self.background)
        self.buttonoperator.setGeometry(QtCore.QRect(760, 360, 311, 81))
        self.buttonoperator.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.buttonoperator.setObjectName("buttonoperator")
        self.backtowelcome = QtWidgets.QPushButton(self.background)
        self.backtowelcome.setGeometry(QtCore.QRect(150, 580, 141, 31))
        self.backtowelcome.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color: rgb(179, 179, 179);\n"
"border-radius:20px;")
        self.backtowelcome.setObjectName("backtowelcome")
        self.buttonseller = QtWidgets.QPushButton(self.background)
        self.buttonseller.setGeometry(QtCore.QRect(430, 360, 311, 81))
        self.buttonseller.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.buttonseller.setObjectName("buttonseller")
        self.buttoncustomer = QtWidgets.QPushButton(self.background)
        self.buttoncustomer.setGeometry(QtCore.QRect(100, 360, 311, 81))
        self.buttoncustomer.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.buttoncustomer.setObjectName("buttoncustomer")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonoperator.clicked.connect(self.GoToOperator)

    def GoToOperator(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginOperator()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Login as :"))
        self.buttonoperator.setText(_translate("Dialog", "Operator"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))
        self.buttonseller.setText(_translate("Dialog", "Seller"))
        self.buttoncustomer.setText(_translate("Dialog", "Customer"))


class Welcome(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(470, 70, 261, 121))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(410, 190, 371, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white")
        self.label_2.setObjectName("label_2")
        self.buttonMainLogin = QtWidgets.QPushButton(self.background)
        self.buttonMainLogin.setGeometry(QtCore.QRect(440, 320, 311, 81))
        self.buttonMainLogin.setStyleSheet("border-radius:20px;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 15, 142);;")
        self.buttonMainLogin.setObjectName("buttonMainLogin")
        self.pushButton_2 = QtWidgets.QPushButton(self.background)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 430, 311, 81))
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 15, 142);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonMainLogin.clicked.connect(self.GoToLogin)

    def GoToLogin(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginAs()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "Sign in or create a new account"))
        self.buttonMainLogin.setText(_translate("Dialog", "Login"))
        self.pushButton_2.setText(_translate("Dialog", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Welcome()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
