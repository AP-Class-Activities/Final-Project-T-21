from PyQt5 import QtCore, QtGui, QtWidgets


class CustomerMenu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.ButtonNew = QtWidgets.QPushButton(self.background)
        self.ButtonNew.setGeometry(QtCore.QRect(50, 200, 131, 81))
        self.ButtonNew.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.ButtonNew.setObjectName("ButtonNew")
        self.LogLabel = QtWidgets.QLabel(self.background)
        self.LogLabel.setGeometry(QtCore.QRect(260, 50, 351, 61))
        self.LogLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 15, 142);\n"
"font: 28pt \"MS Shell Dlg 2\";\n"
"")
        self.LogLabel.setText("")
        self.LogLabel.setObjectName("LogLabel")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1211, 161))
        self.label.setStyleSheet("background-color: rgb(100, 15, 142);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ButtonSetting = QtWidgets.QPushButton(self.background)
        self.ButtonSetting.setGeometry(QtCore.QRect(40, 710, 121, 71))
        self.ButtonSetting.setStyleSheet("border-radius:35px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.ButtonSetting.setObjectName("ButtonSetting")
        self.ButtonMore = QtWidgets.QPushButton(self.background)
        self.ButtonMore.setGeometry(QtCore.QRect(1000, 200, 131, 81))
        self.ButtonMore.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.ButtonMore.setObjectName("ButtonMore")
        self.ButtonElectronics = QtWidgets.QPushButton(self.background)
        self.ButtonElectronics.setGeometry(QtCore.QRect(230, 200, 331, 251))
        self.ButtonElectronics.setStyleSheet("border-radius:1px;\n"
"color: rgb(100, 15, 142);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.ButtonElectronics.setObjectName("ButtonElectronics")
        self.ButtonClothing = QtWidgets.QPushButton(self.background)
        self.ButtonClothing.setGeometry(QtCore.QRect(620, 200, 331, 251))
        self.ButtonClothing.setStyleSheet("border-radius:1px;\n"
"color: rgb(100, 15, 142);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.ButtonClothing.setObjectName("ButtonClothing")
        self.ButtonBooks = QtWidgets.QPushButton(self.background)
        self.ButtonBooks.setGeometry(QtCore.QRect(230, 510, 331, 251))
        self.ButtonBooks.setStyleSheet("border-radius:1px;\n"
"color: rgb(100, 15, 142);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.ButtonBooks.setObjectName("ButtonBooks")
        self.ButtonHomekitchen = QtWidgets.QPushButton(self.background)
        self.ButtonHomekitchen.setGeometry(QtCore.QRect(620, 510, 331, 251))
        self.ButtonHomekitchen.setStyleSheet("border-radius:1px;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 15, 142);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.ButtonHomekitchen.setObjectName("ButtonHomekitchen")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(0, -50, 231, 241))
        self.label_2.setStyleSheet("color: rgb(203, 203, 203);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.LogLabel.raise_()
        self.ButtonSetting.raise_()
        self.ButtonMore.raise_()
        self.ButtonClothing.raise_()
        self.ButtonBooks.raise_()
        self.ButtonHomekitchen.raise_()
        self.label_2.raise_()
        self.ButtonNew.raise_()
        self.ButtonElectronics.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.LogLabel.setText("Hi")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ButtonNew.setText(_translate("Dialog", "New"))
        self.ButtonSetting.setText(_translate("Dialog", "Setting"))
        self.ButtonMore.setText(_translate("Dialog", "More"))
        self.ButtonElectronics.setText(_translate("Dialog", "Electronics"))
        self.ButtonClothing.setText(_translate("Dialog", "Clothing"))
        self.ButtonBooks.setText(_translate("Dialog", "Books"))
        self.ButtonHomekitchen.setText(_translate("Dialog", "Home and Kitchen"))
        self.label_2.setText(_translate("Dialog", "Menu"))



class CustomerSignup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(480, 70, 221, 121))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 481, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.finallogin = QtWidgets.QPushButton(self.background)
        self.finallogin.setGeometry(QtCore.QRect(430, 550, 311, 81))
        self.finallogin.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.finallogin.setObjectName("finallogin")
        self.UserLine = QtWidgets.QLineEdit(self.background)
        self.UserLine.setGeometry(QtCore.QRect(420, 300, 341, 41))
        self.UserLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.UserLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UserLine.setObjectName("UserLine")
        self.PassLine = QtWidgets.QLineEdit(self.background)
        self.PassLine.setGeometry(QtCore.QRect(420, 380, 341, 41))
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
        self.label_4.setGeometry(QtCore.QRect(420, 340, 81, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.LogLabel = QtWidgets.QLabel(self.background)
        self.LogLabel.setGeometry(QtCore.QRect(470, 650, 351, 61))
        self.LogLabel.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.LogLabel.setText("")
        self.LogLabel.setObjectName("LogLabel")
        self.backtowelcome = QtWidgets.QPushButton(self.background)
        self.backtowelcome.setGeometry(QtCore.QRect(410, 510, 141, 31))
        self.backtowelcome.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color: rgb(179, 179, 179);\n"
"border-radius:20px;")
        self.backtowelcome.setObjectName("backtowelcome")
        self.ConfirmPassLine = QtWidgets.QLineEdit(self.background)
        self.ConfirmPassLine.setGeometry(QtCore.QRect(420, 460, 341, 41))
        self.ConfirmPassLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.ConfirmPassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassLine.setObjectName("ConfirmPassLine")
        self.label_5 = QtWidgets.QLabel(self.background)
        self.label_5.setGeometry(QtCore.QRect(420, 420, 141, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.finallogin.clicked.connect(self.SignCust)

    def SignCust(self):
        user = self.UserLine.text()
        password = self.PassLine.text()
        confirmpassword = self.ConfirmPassLine.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.LogLabel.setText("Please fill in all inputs")

        elif len(user)<5 or len(password)<5:
            self.LogLabel.setText("Please enter valid number of characters")

        elif password!=confirmpassword:
            self.LogLabel.setText("Passwords do not match")

        else:
            f = open('CustomerData.txt', 'r+')
            CustomerUsername = self.UserLine.text()
            CustomerPassword = self.PassLine.text()
            s = f.readlines()
            s = [j for i in s for j in i.split()]
            SignPossible = True
            for k in range(0, len(s), 2):
                if CustomerUsername == s[k]:
                    SignPossible = False
                    self.LogLabel.setText("Username and Password invalid")
                    break
            f.close()
            if SignPossible:
                f = open('CustomerData.txt', 'a+')
                f.write(f'{CustomerUsername} {CustomerPassword}\n')
                self.LogLabel.setText("SignUp Successful")
                f.close()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign up"))
        self.label_2.setText(_translate("Dialog", "Register a brand new Customer account"))
        self.finallogin.setText(_translate("Dialog", "Register"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))
        self.label_5.setText(_translate("Dialog", "Confirm Password"))


class OperatorSignup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(480, 70, 221, 121))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 481, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.finallogin = QtWidgets.QPushButton(self.background)
        self.finallogin.setGeometry(QtCore.QRect(430, 550, 311, 81))
        self.finallogin.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.finallogin.setObjectName("finallogin")
        self.UserLine = QtWidgets.QLineEdit(self.background)
        self.UserLine.setGeometry(QtCore.QRect(420, 300, 341, 41))
        self.UserLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.UserLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UserLine.setObjectName("UserLine")
        self.PassLine = QtWidgets.QLineEdit(self.background)
        self.PassLine.setGeometry(QtCore.QRect(420, 380, 341, 41))
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
        self.label_4.setGeometry(QtCore.QRect(420, 340, 81, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.LogLabel = QtWidgets.QLabel(self.background)
        self.LogLabel.setGeometry(QtCore.QRect(470, 650, 351, 61))
        self.LogLabel.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.LogLabel.setText("")
        self.LogLabel.setObjectName("LogLabel")
        self.backtowelcome = QtWidgets.QPushButton(self.background)
        self.backtowelcome.setGeometry(QtCore.QRect(410, 510, 141, 31))
        self.backtowelcome.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color: rgb(179, 179, 179);\n"
"border-radius:20px;")
        self.backtowelcome.setObjectName("backtowelcome")
        self.ConfirmPassLine = QtWidgets.QLineEdit(self.background)
        self.ConfirmPassLine.setGeometry(QtCore.QRect(420, 460, 341, 41))
        self.ConfirmPassLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.ConfirmPassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassLine.setObjectName("ConfirmPassLine")
        self.label_5 = QtWidgets.QLabel(self.background)
        self.label_5.setGeometry(QtCore.QRect(420, 420, 141, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.finallogin.clicked.connect(self.SignOper)

    def SignOper(self):
        user = self.UserLine.text()
        password = self.PassLine.text()
        confirmpassword = self.ConfirmPassLine.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.LogLabel.setText("Please fill in all inputs")

        elif len(user)<5 or len(password)<5:
            self.LogLabel.setText("Please enter valid number of characters")

        elif password!=confirmpassword:
            self.LogLabel.setText("Passwords do not match")

        else:
            f = open('OperatorData.txt', 'r+')
            OperatorUsername = self.UserLine.text()
            OperatorPassword = self.PassLine.text()
            s = f.readlines()
            s = [j for i in s for j in i.split()]
            SignPossible = True
            for k in range(0, len(s), 2):
                if OperatorUsername == s[k]:
                    SignPossible = False
                    self.LogLabel.setText("Username and Password invalid")
                    break
            f.close()
            if SignPossible:
                f = open('OperatorData.txt', 'a+')
                f.write(f'{OperatorUsername} {OperatorPassword}\n')
                self.LogLabel.setText("SignUp Successful")
                f.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign up"))
        self.label_2.setText(_translate("Dialog", "Register a brand new Operator account"))
        self.finallogin.setText(_translate("Dialog", "Register"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))
        self.label_5.setText(_translate("Dialog", "Confirm Password"))


class SellerSignup(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.background = QtWidgets.QWidget(Dialog)
        self.background.setGeometry(QtCore.QRect(-1, -1, 1201, 801))
        self.background.setStyleSheet("background-color:rgb(50, 50, 50);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(480, 70, 221, 121))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
                                 "color:rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 481, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                   "color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.finallogin = QtWidgets.QPushButton(self.background)
        self.finallogin.setGeometry(QtCore.QRect(430, 550, 311, 81))
        self.finallogin.setStyleSheet("border-radius:20px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 18pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(100, 15, 142);")
        self.finallogin.setObjectName("finallogin")
        self.UserLine = QtWidgets.QLineEdit(self.background)
        self.UserLine.setGeometry(QtCore.QRect(420, 300, 341, 41))
        self.UserLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";")
        self.UserLine.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.UserLine.setObjectName("UserLine")
        self.PassLine = QtWidgets.QLineEdit(self.background)
        self.PassLine.setGeometry(QtCore.QRect(420, 380, 341, 41))
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
        self.label_4.setGeometry(QtCore.QRect(420, 340, 81, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.ErrorLabel = QtWidgets.QLabel(self.background)
        self.ErrorLabel.setGeometry(QtCore.QRect(490, 650, 351, 61))
        self.ErrorLabel.setStyleSheet("color: rgb(255, 0, 4);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";")
        self.ErrorLabel.setText("")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.backtowelcome = QtWidgets.QPushButton(self.background)
        self.backtowelcome.setGeometry(QtCore.QRect(410, 510, 141, 31))
        self.backtowelcome.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                         "text-decoration: underline;\n"
                                         "color: rgb(179, 179, 179);\n"
                                         "border-radius:20px;")
        self.backtowelcome.setObjectName("backtowelcome")
        self.ConfirmPassLine = QtWidgets.QLineEdit(self.background)
        self.ConfirmPassLine.setGeometry(QtCore.QRect(420, 460, 341, 41))
        self.ConfirmPassLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "font: 10pt \"MS Shell Dlg 2\";")
        self.ConfirmPassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassLine.setObjectName("ConfirmPassLine")
        self.label_5 = QtWidgets.QLabel(self.background)
        self.label_5.setGeometry(QtCore.QRect(420, 420, 141, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.finallogin.clicked.connect(self.SignSeller)

    def SignSeller(self):
        user = self.UserLine.text()
        password = self.PassLine.text()
        confirmpassword = self.ConfirmPassLine.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.ErrorLabel.setText("Please fill in all inputs")

        elif len(user)<5 or len(password)<5:
            self.ErrorLabel.setText("Please enter valid number of characters")

        elif password!=confirmpassword:
            self.ErrorLabel.setText("Passwords do not match")

        else:
            f = open('SellerData.txt', 'r+')
            SellerUsername = self.UserLine.text()
            SellerPassword = self.PassLine.text()
            s = f.readlines()
            s = [j for i in s for j in i.split()]
            SignPossible = True
            for k in range(0, len(s), 2):
                if SellerUsername == s[k]:
                    SignPossible = False
                    self.ErrorLabel.setText("Username and Password invalid")
                    break
            f.close()
            if SignPossible:
                f = open('SellerData.txt', 'a+')
                f.write(f'{SellerUsername} {SellerPassword}\n')
                self.ErrorLabel.setText("SignUp Succesful")
                f.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign up"))
        self.label_2.setText(_translate("Dialog", "Register a brand new Seller account"))
        self.finallogin.setText(_translate("Dialog", "Register"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))
        self.label_5.setText(_translate("Dialog", "Confirm Password"))



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

        user = self.UserLine.text()
        password = self.PassLine.text()

        if len(user)==0 or len(password)==0:
            self.LogLabel.setText("Please fill in all inputs")
        else:
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


class LoginSeller(object):
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
        self.UserLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
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
        self.LogLabel.setGeometry(QtCore.QRect(470, 610, 351, 61))
        self.LogLabel.setStyleSheet("color: rgb(255, 0, 4);\n"
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

        self.finallogin.clicked.connect(self.LoginSell)


    def LoginSell(self):

        user = self.UserLine.text()
        password = self.PassLine.text()

        if len(user)==0 or len(password)==0:
            self.LogLabel.setText("Please fill in all inputs")

        else:
            SellerUsername = self.UserLine.text()
            SellerPassword = self.PassLine.text()
            users = open("SellerData.txt", "r")
            users = users.readlines()
            users = [u.replace('\n', '').split() for u in users]
            flag = False
            for i in range(len(users)):
                if SellerUsername == users[i][0] and SellerPassword == users[i][1]:
                    flag = True
                    self.LogLabel.setText("Login Successful")
                    break
            if flag == False:
                self.LogLabel.setText("Username and Password invalid")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Sign into seller account"))
        self.finallogin.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))


class LoginCustomer(object):
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
        self.UserLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
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
        self.LogLabel.setGeometry(QtCore.QRect(470, 610, 351, 61))
        self.LogLabel.setStyleSheet("color: rgb(255, 0, 4);\n"
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

        self.finallogin.clicked.connect(self.LoginCustom)

    def LoginCustom(self):

        user = self.UserLine.text()
        password = self.PassLine.text()

        if len(user)==0 or len(password)==0:
            self.LogLabel.setText("Please fill in all inputs")

        else:
            CustomerUsername = self.UserLine.text()
            CustomerPassword = self.PassLine.text()
            users = open("CustomerData.txt", "r")
            users = users.readlines()
            users = [u.replace('\n', '').split() for u in users]
            flag = False
            for i in range(len(users)):
                if CustomerUsername == users[i][0] and CustomerPassword == users[i][1]:
                    flag = True
                    self.switchtomenu()
                    break
            if flag == False:
                self.LogLabel.setText("Username and Password invalid")

    def switchtomenu(self):
        self.window = QtWidgets.QWidget()
        self.ui = CustomerMenu()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Sign into customer account"))
        self.finallogin.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.backtowelcome.setText(_translate("Dialog", "Back to previous page"))



class SignAs(object):
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
        self.gotologin = QtWidgets.QPushButton(self.background)
        self.gotologin.setGeometry(QtCore.QRect(150, 580, 261, 31))
        self.gotologin.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color: rgb(179, 179, 179);\n"
"border-radius:20px;")
        self.gotologin.setObjectName("gotologin")
        self.buttoncustomer = QtWidgets.QPushButton(self.background)
        self.buttoncustomer.setGeometry(QtCore.QRect(430, 360, 311, 81))
        self.buttoncustomer.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.buttoncustomer.setObjectName("buttoncustomer")
        self.buttonseller = QtWidgets.QPushButton(self.background)
        self.buttonseller.setGeometry(QtCore.QRect(100, 360, 311, 81))
        self.buttonseller.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(100, 15, 142);")
        self.buttonseller.setObjectName("buttonseller")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.gotologin.clicked.connect(self.GoToLogin)
        self.buttonseller.clicked.connect(self.GoToSellerSignup)
        self.buttonoperator.clicked.connect(self.GoToOperatorSignup)
        self.buttoncustomer.clicked.connect(self.GoToCustomerSignup)

    def GoToLogin(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginAs()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToSellerSignup(self):
        self.window = QtWidgets.QWidget()
        self.ui = SellerSignup()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToOperatorSignup(self):
        self.window = QtWidgets.QWidget()
        self.ui = OperatorSignup()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToCustomerSignup(self):
        self.window = QtWidgets.QWidget()
        self.ui = CustomerSignup()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Sign up as:"))
        self.buttonoperator.setText(_translate("Dialog", "Operator"))
        self.gotologin.setText(_translate("Dialog", "Already have an account? go to login page."))
        self.buttoncustomer.setText(_translate("Dialog", "Customer"))
        self.buttonseller.setText(_translate("Dialog", "Seller"))


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
        self.buttoncustomer = QtWidgets.QPushButton(self.background)
        self.buttoncustomer.setGeometry(QtCore.QRect(430, 360, 311, 81))
        self.buttoncustomer.setStyleSheet("border-radius:20px;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 18pt \"MS Shell Dlg 2\";\n"
                                          "background-color: rgb(100, 15, 142);")
        self.buttoncustomer.setObjectName("buttoncustomer")
        self.buttonseller = QtWidgets.QPushButton(self.background)
        self.buttonseller.setGeometry(QtCore.QRect(100, 360, 311, 81))
        self.buttonseller.setStyleSheet("border-radius:20px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 18pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(100, 15, 142);")
        self.buttonseller.setObjectName("buttonseller")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonoperator.clicked.connect(self.GoToOperator)
        self.buttoncustomer.clicked.connect(self.GoToCustomer)
        self.buttonseller.clicked.connect(self.GoToSeller)
        self.backtowelcome.clicked.connect(self.GoToWelcome)


    def GoToOperator(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginOperator()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToSeller(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginSeller()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToCustomer(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginCustomer()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToWelcome(self):
        self.window = QtWidgets.QWidget()
        self.ui = Welcome()
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
        self.buttonSignup = QtWidgets.QPushButton(self.background)
        self.buttonSignup.setGeometry(QtCore.QRect(440, 430, 311, 81))
        self.buttonSignup.setStyleSheet("border-radius:20px;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 15, 142);")
        self.buttonSignup.setObjectName("buttonSignup")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonMainLogin.clicked.connect(self.GoToLogin)
        self.buttonSignup.clicked.connect(self.GoToSignup)

    def GoToLogin(self):
        self.window = QtWidgets.QWidget()
        self.ui = LoginAs()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def GoToSignup(self):
        self.window = QtWidgets.QWidget()
        self.ui = SignAs()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "Sign in or create a new account"))
        self.buttonMainLogin.setText(_translate("Dialog", "Login"))
        self.buttonSignup.setText(_translate("Dialog", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Welcome()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
