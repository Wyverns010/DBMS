# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fifa2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 1151, 631))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.label_home = QtWidgets.QLabel(self.home_tab)
        self.label_home.setGeometry(QtCore.QRect(0, 0, 1151, 611))
        font = QtGui.QFont()
        font.setFamily("Linux Libertine Initials O")
        font.setPointSize(18)
        self.label_home.setFont(font)
        self.label_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_home.setFrameShape(QtWidgets.QFrame.Box)
        self.label_home.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_home.setText("")
        self.label_home.setPixmap(QtGui.QPixmap("1200px-Panoramic_santiago_bernabeu.jpg"))
        self.label_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home.setObjectName("label_home")
        self.label = QtWidgets.QLabel(self.home_tab)
        self.label.setGeometry(QtCore.QRect(370, 320, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(211, 215, 207);")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.home_tab, "")
        self.Players_tab = QtWidgets.QWidget()
        self.Players_tab.setObjectName("Players_tab")
        self.tableView = QtWidgets.QTableView(self.Players_tab)
        self.tableView.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Players_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 510, 571, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.formLayoutWidget = QtWidgets.QWidget(self.Players_tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 571, 471))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        self.textEdit_6 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_6)
        self.textEdit_7 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_7.setObjectName("textEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit_7)
        self.tabWidget.addTab(self.Players_tab, "")
        self.Teams_tab = QtWidgets.QWidget()
        self.Teams_tab.setObjectName("Teams_tab")
        self.tableView_2 = QtWidgets.QTableView(self.Teams_tab)
        self.tableView_2.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_2.setObjectName("tableView_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Teams_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 340, 591, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.Teams_tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 571, 224))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.textEdit_8 = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_8.setObjectName("textEdit_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_8)
        self.textEdit_9 = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_9.setObjectName("textEdit_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_9)
        self.textEdit_10 = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_10.setObjectName("textEdit_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_10)
        self.tabWidget.addTab(self.Teams_tab, "")
        self.Bookings = QtWidgets.QWidget()
        self.Bookings.setObjectName("Bookings")
        self.tableView_3 = QtWidgets.QTableView(self.Bookings)
        self.tableView_3.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_3.setObjectName("tableView_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Bookings)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 360, 581, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.Bookings)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 581, 341))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.tabWidget.addTab(self.Bookings, "")
        self.Matches_tab = QtWidgets.QWidget()
        self.Matches_tab.setObjectName("Matches_tab")
        self.pushButton_13 = QtWidgets.QPushButton(self.Matches_tab)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 90, 115, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tableView_4 = QtWidgets.QTableView(self.Matches_tab)
        self.tableView_4.setGeometry(QtCore.QRect(230, 30, 361, 341))
        self.tableView_4.setObjectName("tableView_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.Matches_tab)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 30, 115, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.Matches_tab)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 210, 115, 30))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.Matches_tab)
        self.pushButton_16.setGeometry(QtCore.QRect(20, 150, 115, 30))
        self.pushButton_16.setObjectName("pushButton_16")
        self.tabWidget.addTab(self.Matches_tab, "")
        self.Scorers_tab = QtWidgets.QWidget()
        self.Scorers_tab.setObjectName("Scorers_tab")
        self.label_3 = QtWidgets.QLabel(self.Scorers_tab)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 671, 631))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("fifa/20032336-0-image-m-42_1571743623584.jpg"))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.Scorers_tab)
        self.tableWidget.setGeometry(QtCore.QRect(160, 50, 291, 271))
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tabWidget.addTab(self.Scorers_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FIFA Manager 1.01"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.pushButton_4.setText(_translate("MainWindow", "View"))
        self.pushButton.setText(_translate("MainWindow", "Insert"))
        self.pushButton_3.setText(_translate("MainWindow", "Update"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Country"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.label_6.setText(_translate("MainWindow", "Age"))
        self.label_7.setText(_translate("MainWindow", "Height"))
        self.label_8.setText(_translate("MainWindow", "Weight"))
        self.label_9.setText(_translate("MainWindow", "Rating"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Players_tab), _translate("MainWindow", "Players"))
        self.pushButton_8.setText(_translate("MainWindow", "Update"))
        self.pushButton_7.setText(_translate("MainWindow", "View"))
        self.pushButton_5.setText(_translate("MainWindow", "Remove"))
        self.pushButton_6.setText(_translate("MainWindow", "Insert"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Country"))
        self.label_12.setText(_translate("MainWindow", "Captain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Teams_tab), _translate("MainWindow", "Teams"))
        self.pushButton_11.setText(_translate("MainWindow", "View"))
        self.pushButton_12.setText(_translate("MainWindow", "Update"))
        self.pushButton_9.setText(_translate("MainWindow", "Remove"))
        self.pushButton_10.setText(_translate("MainWindow", "Insert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bookings), _translate("MainWindow", "Bookings"))
        self.pushButton_13.setText(_translate("MainWindow", "Remove"))
        self.pushButton_14.setText(_translate("MainWindow", "Insert"))
        self.pushButton_15.setText(_translate("MainWindow", "View"))
        self.pushButton_16.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Matches_tab), _translate("MainWindow", "Matches"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scorers_tab), _translate("MainWindow", "Scorers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
