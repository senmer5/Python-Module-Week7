# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("\n"
"background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(219, 384, 361, 50))
        self.pushButton_login.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 2px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_login_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_login_exit.setGeometry(QtCore.QRect(220, 450, 361, 50))
        self.pushButton_login_exit.setStyleSheet("QPushButton {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    font-family: 14pt \"Symbol\";\n"
"    color: black; /* Siyah yazı rengi */\n"
"    background: rgba(0, 84, 147, 128);\n"
"    border-radius: 8px; /* Köşe yuvarlama */\n"
"    padding: 8px; /* Küçük padding */\n"
"    border: 2px solid black; /* İnce siyah çerçeve */\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(145, 145, 145); \n"
"    /* Hover durumunda gölgeyi değiştirmek için */\n"
"}")
        self.pushButton_login_exit.setObjectName("pushButton_login_exit")
        self.label_login_username = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login_username.setGeometry(QtCore.QRect(220, 250, 151, 45))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(24)
        self.label_login_username.setFont(font)
        self.label_login_username.setObjectName("label_login_username")
        self.label_login_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login_password.setGeometry(QtCore.QRect(220, 310, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(24)
        self.label_login_password.setFont(font)
        self.label_login_password.setObjectName("label_login_password")
        self.lineEdit_username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(390, 250, 191, 35))
        self.lineEdit_username.setStyleSheet("QLineEdit {\n"
"    font-size: 18px;\n"
"    font-family: \"Symbol\";\n"
"    color: #333;\n"
"    background-color: #fff;\n"
"    border: 1px solid #2c3e50;\n"
"    border-radius: 1px;\n"
"    padding: 1px;\n"
" \n"
"}\n"
"QLineEdit:placeholder {\n"
"    color: rgba(150, 150, 150, 0.8);\n"
"    font-style: italic;\n"
"}\n"
"")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(390, 310, 191, 35))
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"    font-size: 18px;\n"
"    font-family: \"Symbol\";\n"
"    color: #333;\n"
"    background-color: #fff;\n"
"    border: 1px solid #2c3e50;\n"
"    border-radius: 1px;\n"
"    padding: 1px;\n"
" \n"
"}\n"
"QLineEdit:placeholder {\n"
"    color: rgba(150, 150, 150, 0.8);\n"
"    font-style: italic;\n"
"}")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_login_baslik = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login_baslik.setGeometry(QtCore.QRect(250, 130, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label_login_baslik.setFont(font)
        self.label_login_baslik.setStyleSheet("font: 40pt \"Symbol\";")
        self.label_login_baslik.setObjectName("label_login_baslik")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 821, 91))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("foto2.png"))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_login.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_login_exit.setText(_translate("MainWindow", "EXIT"))
        self.label_login_username.setText(_translate("MainWindow", "USERNAME"))
        self.label_login_password.setText(_translate("MainWindow", "PASSWORD"))
        self.label_login_baslik.setText(_translate("MainWindow", "CRM PROJECT"))
