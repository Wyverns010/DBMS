# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fifa2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from back import Database
#from connector import Actions

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.db = Database()
        #self.act = Actions()
        self.mainW = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 671)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 1151, 631))
        self.tabWidget.setAutoFillBackground(False)
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
        font.setPointSize(20)
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
        self.tableView_players = QtWidgets.QTableWidget(self.Players_tab)
        self.tableView_players.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_players.setObjectName("tableView_players")
        #self.tableView_players.setForeground(QBrush(QColor(255,255,255)))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Players_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 510, 571, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_players_rm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_players_rm.setObjectName("pushButton_players_rm")
        self.horizontalLayout.addWidget(self.pushButton_players_rm)
        self.pushButton_players_rm.clicked.connect(self.players_delete)

        self.pushButton_players_peek = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_players_peek.setObjectName("pushButton_teams_peek")
        self.pushButton_players_peek.setText("peek")
        self.horizontalLayout.addWidget(self.pushButton_players_peek)
        self.pushButton_players_peek.clicked.connect(self.players_peek)

        self.pushButton_players_up = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_players_up.setObjectName("pushButton_players_up")
        self.horizontalLayout.addWidget(self.pushButton_players_up)
        self.pushButton_players_up.clicked.connect(self.players_update)

        self.pushButton_players_vw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_players_vw.setObjectName("pushButton_players_vw")
        self.horizontalLayout.addWidget(self.pushButton_players_vw)
        self.pushButton_players_vw.clicked.connect(self.players_view)

        self.pushButton_players_in = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_players_in.setObjectName("pushButton_players_in")
        self.horizontalLayout.addWidget(self.pushButton_players_in)
        self.pushButton_players_in.clicked.connect(self.players_insert)

        self.formLayoutWidget = QtWidgets.QWidget(self.Players_tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 571, 481))
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
        #self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
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
        self.textEdit_players_nm = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_nm.setObjectName("textEdit_players_nm")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_nm)
        self.textEdit_players_cntry = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_cntry.setObjectName("textEdit_players_cntry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_cntry)
        self.textEdit_players_pos = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_pos.setObjectName("textEdit_players_pos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_pos)
        self.textEdit_players_age = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_age.setObjectName("textEdit_players_age")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_age)
        self.textEdit_players_ht = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_ht.setObjectName("textEdit_players_ht")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_ht)
        self.textEdit_players_wt = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_wt.setObjectName("textEdit_players_wt")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_wt)
        self.textEdit_players_rtng = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_players_rtng.setObjectName("textEdit_players_rtng")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit_players_rtng)
        self.tabWidget.addTab(self.Players_tab, "")
        self.Teams_tab = QtWidgets.QWidget()
        self.Teams_tab.setObjectName("Teams_tab")
        self.tableView_teams = QtWidgets.QTableWidget(self.Teams_tab)
        self.tableView_teams.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_teams.setObjectName("tableView_teams")
        #----------------------------------------------------------------
        #self.x = self.tableView_teams.currentRow()
        #print("------>",str(self.x))
        #self.y = self.tableView_teams.currentColumn()
        #print("------>",str(self.y))

        #----------------------------------------------------------------
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Teams_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 340, 591, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_teams_rm = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_teams_rm.setObjectName("pushButton_teams_rm")
        self.horizontalLayout_2.addWidget(self.pushButton_teams_rm)
        self.pushButton_teams_rm.clicked.connect(self.teams_delete)


        self.pushButton_teams_peek = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_teams_peek.setObjectName("pushButton_teams_peek")
        self.pushButton_teams_peek.setText("peek")

        self.horizontalLayout_2.addWidget(self.pushButton_teams_peek)
        self.pushButton_teams_peek.clicked.connect(self.teams_peek)

        self.pushButton_teams_up = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_teams_up.setObjectName("pushButton_teams_up")
        self.horizontalLayout_2.addWidget(self.pushButton_teams_up)
        self.pushButton_teams_up.clicked.connect(self.teams_update)
        self.pushButton_teams_vw = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_teams_vw.setObjectName("pushButton_teams_vw")
        #self.psuhButton_teams_vw.clicked.connect(self.teams_view)
        self.horizontalLayout_2.addWidget(self.pushButton_teams_vw)
        self.pushButton_teams_vw.clicked.connect(self.teams_view)
        self.pushButton_teams_in = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_teams_in.setObjectName("pushButton_teams_in")
        self.horizontalLayout_2.addWidget(self.pushButton_teams_in)

        self.pushButton_teams_in.clicked.connect(self.teams_insert)
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
        self.textEdit_teams_nm = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_teams_nm.setObjectName("textEdit_teams_nm")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_teams_nm)
        self.textEdit_teams_cntry = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_teams_cntry.setObjectName("textEdit_teams_cntry")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_teams_cntry)
        # self.textEdit_teams_cptn = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        # self.textEdit_teams_cptn.setObjectName("textEdit_teams_cptn")
        # self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_teams_cptn)
        self.tabWidget.addTab(self.Teams_tab, "")
        self.Bookings_tab = QtWidgets.QWidget()
        self.Bookings_tab.setObjectName("Bookings_tab")
        self.tableView_bookings = QtWidgets.QTableWidget(self.Bookings_tab)
        self.tableView_bookings.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_bookings.setObjectName("tableView_bookings")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Bookings_tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 360, 581, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.pushButton_bookings_rm = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        # self.pushButton_bookings_rm.setObjectName("pushButton_bookings_rm")
        # self.horizontalLayout_3.addWidget(self.pushButton_bookings_rm)

        self.pushButton_bookings_peek = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_bookings_peek.setObjectName("pushButton_bookings_peek")
        self.pushButton_bookings_peek.setText("peek")
        self.horizontalLayout_3.addWidget(self.pushButton_bookings_peek)
        self.pushButton_bookings_peek.clicked.connect(self.bookings_peek)

        self.pushButton_bookings_up = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_bookings_up.setObjectName("pushButton_bookings_up")
        self.horizontalLayout_3.addWidget(self.pushButton_bookings_up)
        self.pushButton_bookings_up.clicked.connect(self.bookings_update)

        self.pushButton_bookings_vw = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_bookings_vw.setObjectName("pushButton_bookings_vw")
        self.horizontalLayout_3.addWidget(self.pushButton_bookings_vw)
        self.pushButton_bookings_vw.clicked.connect(self.bookings_view)

        self.pushButton_bookings_in = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_bookings_in.setObjectName("pushButton_bookings_in")
        self.horizontalLayout_3.addWidget(self.pushButton_bookings_in)
        self.pushButton_bookings_in.clicked.connect(self.bookings_insert)

        self.formLayoutWidget_3 = QtWidgets.QWidget(self.Bookings_tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 581, 346))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.textEdit_bookings_nm = QtWidgets.QTextEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_bookings_nm.sizePolicy().hasHeightForWidth())
        self.textEdit_bookings_nm.setSizePolicy(sizePolicy)
        self.textEdit_bookings_nm.setObjectName("textEdit_bookings_nm")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_bookings_nm)
        self.textEdit_bookings_yc = QtWidgets.QTextEdit(self.formLayoutWidget_3)
        self.textEdit_bookings_yc.setObjectName("textEdit_bookings_yc")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_bookings_yc)
        self.textEdit_bookings_rc = QtWidgets.QTextEdit(self.formLayoutWidget_3)
        self.textEdit_bookings_rc.setObjectName("textEdit_bookings_rc")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_bookings_rc)
        self.tabWidget.addTab(self.Bookings_tab, "")
        self.Matches_tab = QtWidgets.QWidget()
        self.Matches_tab.setObjectName("Matches_tab")
        self.tableView_matches = QtWidgets.QTableWidget(self.Matches_tab)
        self.tableView_matches.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_matches.setObjectName("tableView_matches")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Matches_tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 470, 571, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_matches_rm = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_matches_rm.setObjectName("pushButton_matches_rm")
        self.horizontalLayout_4.addWidget(self.pushButton_matches_rm)
        self.pushButton_matches_rm.clicked.connect(self.matches_delete)

        self.pushButton_matches_peek = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_matches_peek.setObjectName("pushButton_teams_peek")
        self.pushButton_matches_peek.setText("peek")
        self.horizontalLayout_4.addWidget(self.pushButton_matches_peek)
        self.pushButton_matches_peek.clicked.connect(self.matches_peek)

        self.pushButton_matches_up = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_matches_up.setObjectName("pushButton_matches_up")
        self.horizontalLayout_4.addWidget(self.pushButton_matches_up)
        self.pushButton_matches_up.clicked.connect(self.matches_update)

        self.pushButton_matches_vw = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_matches_vw.setObjectName("pushButton_matches_vw")
        self.horizontalLayout_4.addWidget(self.pushButton_matches_vw)
        self.pushButton_matches_vw.clicked.connect(self.matches_view)

        self.pushButton_matches_in = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_matches_in.setObjectName("pushButton_matches_in")
        self.horizontalLayout_4.addWidget(self.pushButton_matches_in)
        self.pushButton_matches_in.clicked.connect(self.matches_insert)

        self.formLayoutWidget_4 = QtWidgets.QWidget(self.Matches_tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 571, 452))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.textEdit_matches_mn = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.textEdit_matches_mn.setObjectName("textEdit_matches_mn")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_matches_mn)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.textEdit_matches_t1 = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.textEdit_matches_t1.setObjectName("textEdit_matches_t1")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_matches_t1)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.textEdit_matches_t2 = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.textEdit_matches_t2.setObjectName("textEdit_matches_t2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_matches_t2)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.textEdit_matches_loc = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.textEdit_matches_loc.setObjectName("textEdit_matches_loc")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_matches_loc)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.textEdit_matches_dt = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.textEdit_matches_dt.setStyleSheet("color: rgb(136, 138, 133);")
        self.textEdit_matches_dt.setObjectName("textEdit_matches_dt")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_matches_dt)
        self.tabWidget.addTab(self.Matches_tab, "")
        self.match_goals = QtWidgets.QWidget()
        self.match_goals.setObjectName("match_goals")
        self.tableView_match_goals = QtWidgets.QTableWidget(self.match_goals)
        self.tableView_match_goals.setGeometry(QtCore.QRect(610, 10, 511, 581))
        self.tableView_match_goals.setObjectName("tableView_match_goals")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.match_goals)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 380, 571, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # self.pushButton_match_goals_rm = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        # self.pushButton_match_goals_rm.setObjectName("pushButton_match_goals_rm")
        # self.horizontalLayout_5.addWidget(self.pushButton_match_goals_rm)
        #
        # self.pushButton_match_goals_peek = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        # self.pushButton_match_goals_peek.setObjectName("pushButton_match_goals_peek")
        # self.pushButton_match_goals_peek.setText("peek")
        # self.horizontalLayout_5.addWidget(self.pushButton_match_goals_peek)
        # self.pushButton_match_goals_peek.clicked.connect(self.match_goals_peek)
        #
        # self.pushButton_match_goals_up = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        # self.pushButton_match_goals_up.setObjectName("pushButton_match_goals_up")
        # self.horizontalLayout_5.addWidget(self.pushButton_match_goals_up)
        self.pushButton_match_goals_vw = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_match_goals_vw.setObjectName("pushButton_match_goals_vw")
        self.horizontalLayout_5.addWidget(self.pushButton_match_goals_vw)
        self.pushButton_match_goals_vw.clicked.connect(self.match_goals_view)

        self.pushButton_match_goals_in = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_match_goals_in.setObjectName("pushButton_match_goals_in")
        self.horizontalLayout_5.addWidget(self.pushButton_match_goals_in)
        self.pushButton_match_goals_in.clicked.connect(self.match_goals_insert)

        self.formLayoutWidget_5 = QtWidgets.QWidget(self.match_goals)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 571, 281))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_24.setObjectName("label_24")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.textEdit_match_goals_nm = QtWidgets.QTextEdit(self.formLayoutWidget_5)
        self.textEdit_match_goals_nm.setObjectName("textEdit_match_goals_nm")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_match_goals_nm)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.textEdit_match_goals_t = QtWidgets.QTextEdit(self.formLayoutWidget_5)
        self.textEdit_match_goals_t.setObjectName("textEdit_match_goals_t")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_match_goals_t)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_26.setObjectName("label_26")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.textEdit_match_goals_mno = QtWidgets.QTextEdit(self.formLayoutWidget_5)
        self.textEdit_match_goals_mno.setObjectName("textEdit_match_goals_mno")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_match_goals_mno)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_27.setObjectName("label_27")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.textEdit_match_goals_gls = QtWidgets.QTextEdit(self.formLayoutWidget_5)
        self.textEdit_match_goals_gls.setObjectName("textEdit_match_goals_gls")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_match_goals_gls)
        self.tabWidget.addTab(self.match_goals, "")
        self.Scorers_tab = QtWidgets.QWidget()
        self.Scorers_tab.setObjectName("Scorers_tab")
        self.label_3 = QtWidgets.QLabel(self.Scorers_tab)
        self.label_3.setGeometry(QtCore.QRect(180, 0, 631, 601))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("20032336-0-image-m-42_1571743623584.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_21 = QtWidgets.QLabel(self.Scorers_tab)
        self.label_21.setGeometry(QtCore.QRect(250, 10, 651, 41))
        font = QtGui.QFont()
        font.setFamily("Norasi")
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.Scorers_tab)
        self.label_23.setGeometry(QtCore.QRect(0, -10, 311, 611))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("crop.jpeg"))
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.Scorers_tab)
        self.label_22.setGeometry(QtCore.QRect(720, 0, 431, 601))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("ronaldo-portugal-world-cup-russia-2018.jpg"))
        self.label_22.setObjectName("label_22")
        self.tableWidget_scorers = QtWidgets.QTableWidget(self.Scorers_tab)
        self.tableWidget_scorers.setGeometry(QtCore.QRect(290, 190, 461, 311))
        self.tableWidget_scorers.setMinimumSize(QtCore.QSize(256, 0))
        self.tableWidget_scorers.setRowCount(20)
        self.tableWidget_scorers.setColumnCount(2)
        self.tableWidget_scorers.setObjectName("tableWidget_scorers")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_scorers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_scorers.setHorizontalHeaderItem(1, item)
        self.tableWidget_scorers.horizontalHeader().setDefaultSectionSize(210)
        self.label_3.raise_()
        self.label_23.raise_()
        self.label_22.raise_()
        self.label_21.raise_()
        self.tableWidget_scorers.raise_()


        val = self.db.view_score()
        #self.tableWidget_scorers.setRowCount(0)
        #self.tableWidget_scorers.setColumnCount(5)
        for i,row in enumerate(val):
            self.tableView_bookings.insertRow(i)
            print("-----"+str(i))
            for j,data in enumerate(row):
                print("-----"+str(j))
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget_scorers.setItem(i,j,item)
                print(str(data))

        self.tabWidget.addTab(self.Scorers_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        # very important
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FIFA Manager 1.01"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("MainWindow", "Home"))
        self.pushButton_players_rm.setText(_translate("MainWindow", "Remove"))
        self.pushButton_players_up.setText(_translate("MainWindow", "Update"))
        self.pushButton_players_vw.setText(_translate("MainWindow", "View"))
        self.pushButton_players_in.setText(_translate("MainWindow", "Insert"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Country"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.label_6.setText(_translate("MainWindow", "Age"))
        self.label_7.setText(_translate("MainWindow", "Height"))
        self.label_8.setText(_translate("MainWindow", "Weight"))
        self.label_9.setText(_translate("MainWindow", "Rating"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Players_tab), _translate("MainWindow", "Players"))
        self.pushButton_teams_rm.setText(_translate("MainWindow", "Remove"))
        self.pushButton_teams_up.setText(_translate("MainWindow", "Update"))
        self.pushButton_teams_vw.setText(_translate("MainWindow", "View"))
        self.pushButton_teams_in.setText(_translate("MainWindow", "Insert"))
        self.label_10.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Country"))
        # self.label_12.setText(_translate("MainWindow", "Captain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Teams_tab), _translate("MainWindow", "Teams"))
        #self.pushButton_bookings_rm.setText(_translate("MainWindow", "Remove"))
        self.pushButton_bookings_up.setText(_translate("MainWindow", "Update"))
        self.pushButton_bookings_vw.setText(_translate("MainWindow", "View"))
        self.pushButton_bookings_in.setText(_translate("MainWindow", "Insert"))
        self.label_13.setText(_translate("MainWindow", "Name"))
        self.label_14.setText(_translate("MainWindow", "Yellow Cards"))
        self.label_15.setText(_translate("MainWindow", "Red Cards"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Bookings_tab), _translate("MainWindow", "Bookings"))
        self.pushButton_matches_rm.setText(_translate("MainWindow", "Remove"))
        self.pushButton_matches_up.setText(_translate("MainWindow", "Update"))
        self.pushButton_matches_vw.setText(_translate("MainWindow", "View"))
        self.pushButton_matches_in.setText(_translate("MainWindow", "Insert"))
        self.label_16.setText(_translate("MainWindow", "Match No."))
        self.label_17.setText(_translate("MainWindow", "Team 1"))
        self.label_18.setText(_translate("MainWindow", "Team 2"))
        self.label_19.setText(_translate("MainWindow", "Location"))
        self.label_20.setText(_translate("MainWindow", "Date & time"))
        self.textEdit_matches_dt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">yyyy/mm/dd hh:mm:ss</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Matches_tab), _translate("MainWindow", "Matches"))
        #self.pushButton_match_goals_rm.setText(_translate("MainWindow", "Remove"))
        #self.pushButton_match_goals_up.setText(_translate("MainWindow", "Update"))
        self.pushButton_match_goals_vw.setText(_translate("MainWindow", "View"))
        self.pushButton_match_goals_in.setText(_translate("MainWindow", "Insert"))
        self.label_24.setText(_translate("MainWindow", "Name"))
        self.label_25.setText(_translate("MainWindow", "Team"))
        self.label_26.setText(_translate("MainWindow", "Match No."))
        self.label_27.setText(_translate("MainWindow", "Goals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.match_goals), _translate("MainWindow", "Match Goals"))
        self.label_21.setText(_translate("MainWindow", "TOP GOAL SCORERS OF THE LEAGUE"))
        item = self.tableWidget_scorers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget_scorers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GOALS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scorers_tab), _translate("MainWindow", "Scorers"))

    def players_view(self):
        val = self.db.view_players()
        #self.tableView_players.setRowCount(2)
        self.tableView_players.setRowCount(0)
        self.tableView_players.setColumnCount(7)
        for i,row in enumerate(val):
            self.tableView_players.insertRow(i)
            print("-----"+str(i))
            for j,data in enumerate(row):
                print("-----"+str(j))
                #self.tableView_players.insertColumn(j)
                item = QtWidgets.QTableWidgetItem(str(data))
                #item.setBackground(QtGui.QBrush(QtGui.QColor(255,255,255)))
                self.tableView_players.setItem(i,j,item)
                print(str(data))

    def teams_view(self):
        val = self.db.view_teams()
        self.tableView_teams.setRowCount(0)
        self.tableView_teams.setColumnCount(3)
        for i,row in enumerate(val):
            self.tableView_teams.insertRow(i)
            #print("-----"+str(i))
            for j,data in enumerate(row):
                #print("-----"+str(j))
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableView_teams.setItem(i,j,item)
                #print(str(data))

    def matches_view(self):
        val = self.db.view_matches()
        self.tableView_matches.setRowCount(0)
        self.tableView_matches.setColumnCount(5)
        for i,row in enumerate(val):
            self.tableView_matches.insertRow(i)
            print("-----"+str(i))
            for j,data in enumerate(row):
                print("-----"+str(j))
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableView_matches.setItem(i,j,item)
                print(str(data))

    def bookings_view(self):
        val = self.db.view_bookings()
        self.tableView_bookings.setRowCount(0)
        self.tableView_bookings.setColumnCount(3)
        for i,row in enumerate(val):
            self.tableView_bookings.insertRow(i)
            print("-----"+str(i))
            for j,data in enumerate(row):
                print("-----"+str(j))
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableView_bookings.setItem(i,j,item)
                print(str(data))

    def match_goals_view(self):
        val = self.db.view_scorers()
        self.tableView_match_goals.setRowCount(0)
        self.tableView_match_goals.setColumnCount(4)
        for i,row in enumerate(val):
            self.tableView_match_goals.insertRow(i)
            print("-----"+str(i))
            for j,data in enumerate(row):
                print("-----"+str(j))
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableView_match_goals.setItem(i,j,item)
                print(str(data))


    def players_insert(self):
        player_name = self.textEdit_players_nm.toPlainText()
        print(player_name)

        player_country = self.textEdit_players_cntry.toPlainText()
        player_pos = self.textEdit_players_pos.toPlainText()
        player_age = self.textEdit_players_age.toPlainText()
        player_ht = self.textEdit_players_ht.toPlainText()
        player_wt = self.textEdit_players_wt.toPlainText()
        player_rating = self.textEdit_players_rtng.toPlainText()

        self.db.insert_players(player_name,player_country,
                                player_pos,player_age,player_ht,
                                player_wt,player_rating)

        self.textEdit_players_nm.setPlainText("")
        self.textEdit_players_age.setPlainText("")
        self.textEdit_players_pos.setPlainText("")
        self.textEdit_players_wt.setPlainText("")
        self.textEdit_players_ht.setPlainText("")
        self.textEdit_players_rtng.setPlainText("")
        self.textEdit_players_cntry.setPlainText("")

    def teams_insert(self):
        name = self.textEdit_teams_nm.toPlainText()
        #print(player_name)

        player_country = self.textEdit_teams_cntry.toPlainText()
        # player_captain = self.textEdit_teams_cptn.toPlainText()

        self.db.insert_teams(name,player_country)

    def matches_insert(self):
        match_id = self.textEdit_matches_mn.toPlainText()
        print("--------",type(match_id))
        match_id = int(match_id)

        team1 = self.textEdit_matches_t1.toPlainText()
        team2 = self.textEdit_matches_t2.toPlainText()
        loc = self.textEdit_matches_loc.toPlainText()
        date = self.textEdit_matches_dt.toPlainText()

        self.db.insert_matches(match_id,team1,team2,loc,date)

    def bookings_insert(self):

        name= self.textEdit_bookings_nm.toPlainText()
        yc = self.textEdit_bookings_yc.toPlainText()
        rc = self.textEdit_bookings_rc.toPlainText()


        self.db.insert_bookings(name,yc,rc)

    def match_goals_insert(self):

        name= self.textEdit_match_goals_nm.toPlainText()
        team = self.textEdit_match_goals_t.toPlainText()
        mno = self.textEdit_match_goals_mno.toPlainText()
        gl = self.textEdit_match_goals_gls.toPlainText()


        self.db.insert_goals(name,team,mno,gl)

        val = self.db.view_score()
        #self.tableWidget_scorers.setRowCount(0)
        #self.tableWidget_scorers.setColumnCount(5)
        for i,row in enumerate(val):
            self.tableView_bookings.insertRow(i)
            print("-----"+str(i))
            for j,data in enumerate(row):
                print("-----"+str(j))
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget_scorers.setItem(i,j,item)
                print(str(data))


    def teams_peek(self):
        self.x = self.tableView_teams.currentRow()
        self.y = self.tableView_teams.currentColumn()
        print("------"+str(self.x)+"-----"+str(self.y))
        num_rows = self.tableView_teams.rowCount()
        num_columns = self.tableView_teams.columnCount()

        try:
            self.textEdit_teams_nm.setPlainText(self.tableView_teams.item(self.x,0).text())
            self.textEdit_teams_cntry.setPlainText(self.tableView_teams.item(self.x,1).text())
            # self.textEdit_teams_cptn.setPlainText(self.tableView_teams.item(self.x,2).text())
        except:
            pass

    def players_peek(self):
        self.x = self.tableView_players.currentRow()
        self.y = self.tableView_players.currentColumn()
        #print("------"+str(self.x)+"-----"+str(self.y))
        num_rows = self.tableView_players.rowCount()
        num_columns = self.tableView_players.columnCount()

        try:
            self.textEdit_players_nm.setPlainText(self.tableView_players.item(self.x,0).text())
            self.textEdit_players_cntry.setPlainText(self.tableView_players.item(self.x,1).text())
            self.textEdit_players_pos.setPlainText(self.tableView_players.item(self.x,2).text())
            self.textEdit_players_age.setPlainText(self.tableView_players.item(self.x,3).text())
            self.textEdit_players_ht.setPlainText(self.tableView_players.item(self.x,4).text())
            self.textEdit_players_wt.setPlainText(self.tableView_players.item(self.x,5).text())
            self.textEdit_players_rtng.setPlainText(self.tableView_players.item(self.x,6).text())
        except:
            pass

    def bookings_peek(self):
        self.x = self.tableView_bookings.currentRow()
        self.y = self.tableView_bookings.currentColumn()
        #print("------"+str(self.x)+"-----"+str(self.y))
        num_rows = self.tableView_bookings.rowCount()
        num_columns = self.tableView_bookings.columnCount()

        try:
            self.textEdit_bookings_nm.setPlainText(self.tableView_bookings.item(self.x,0).text())
            self.textEdit_bookings_yc.setPlainText(self.tableView_bookings.item(self.x,1).text())
            self.textEdit_bookings_rc.setPlainText(self.tableView_bookings.item(self.x,2).text())
        except:
            pass

    def match_goals_peek(self):
        self.x = self.tableView_match_goals.currentRow()
        self.y = self.tableView_match_goals.currentColumn()
        #print("------"+str(self.x)+"-----"+str(self.y))
        num_rows = self.tableView_match_goals.rowCount()
        num_columns = self.tableView_match_goals.columnCount()

        try:
            self.textEdit_match_goals_nm.setPlainText(self.tableView_match_goals.item(self.x,0).text())
            self.textEdit_match_goals_t.setPlainText(self.tableView_match_goals.item(self.x,1).text())
            self.textEdit_match_goals_mno.setPlainText(self.tableView_match_goals.item(self.x,2).text())
            self.textEdit_match_goals_gls.setPlainText(self.tableView_match_goals.item(self.x,3).text())
        except:
            pass

    def matches_peek(self):
        self.x = self.tableView_matches.currentRow()
        self.y = self.tableView_matches.currentColumn()
        #print("------"+str(self.x)+"-----"+str(self.y))
        num_rows = self.tableView_matches.rowCount()
        num_columns = self.tableView_matches.columnCount()

        try:
            self.textEdit_matches_mn.setPlainText(self.tableView_matches.item(self.x,0).text())
            self.textEdit_matches_t1.setPlainText(self.tableView_matches.item(self.x,1).text())
            self.textEdit_matches_t2.setPlainText(self.tableView_matches.item(self.x,2).text())
            self.textEdit_matches_loc.setPlainText(self.tableView_matches.item(self.x,3).text())
            self.textEdit_matches_dt.setPlainText(self.tableView_matches.item(self.x,4).text())

        except:
            pass

    def teams_update(self):

        name = self.textEdit_teams_nm.toPlainText()
        player_country = self.textEdit_teams_cntry.toPlainText()
        # player_captain = self.textEdit_teams_cptn.toPlainText()

        self.db.update_team(name,player_country)

    def players_update(self):

        name = self.textEdit_players_nm.toPlainText()
        country = self.textEdit_players_cntry.toPlainText()
        pos = self.textEdit_players_pos.toPlainText()
        age = self.textEdit_players_age.toPlainText()
        ht = self.textEdit_players_ht.toPlainText()
        wt = self.textEdit_players_wt.toPlainText()
        rt = self.textEdit_players_rtng.toPlainText()

        self.db.update_player(name,country,pos,age,ht,wt,rt)

    def matches_update(self):

        mno = self.textEdit_matches_mn.toPlainText()
        t1 = self.textEdit_matches_t1.toPlainText()
        t2 = self.textEdit_matches_t2.toPlainText()
        loc = self.textEdit_matches_loc.toPlainText()
        dt = self.textEdit_matches_dt.toPlainText()

        self.db.update_match(mno,t1,t2,loc,dt)

    def bookings_update(self):

        name = self.textEdit_bookings_nm.toPlainText()
        yc = self.textEdit_bookings_yc.toPlainText()
        rc = self.textEdit_bookings_rc.toPlainText()

        self.db.update_booking(name,yc,rc)

    def teams_delete(self):

        name = self.textEdit_teams_nm.toPlainText()
        player_country = self.textEdit_teams_cntry.toPlainText()
        # player_captain = self.textEdit_teams_cptn.toPlainText()

        self.db.delete_team(name)

        self.textEdit_teams_nm.setPlainText("")
        self.textEdit_teams_cntry.setPlainText("")
        # self.textEdit_teams_cptn.setPlainText("")

    def players_delete(self):

        name = self.textEdit_players_nm.toPlainText()

        self.db.delete_player(name)

        self.textEdit_players_nm.setPlainText("")
        self.textEdit_players_age.setPlainText("")
        self.textEdit_players_pos.setPlainText("")
        self.textEdit_players_wt.setPlainText("")
        self.textEdit_players_ht.setPlainText("")
        self.textEdit_players_rtng.setPlainText("")
        self.textEdit_players_cntry.setPlainText("")

    def matches_delete(self):

        mno = self.textEdit_matches_mn.toPlainText()

        self.db.delete_match(mn)

        self.textEdit_matches_dt.setPlainText("")
        self.textEdit_matches_mn.setPlainText("")
        self.textEdit_matches_t1.setPlainText("")
        self.textEdit_matches_t2.setPlainText("")
        self.textEdit_matches_loc.setPlainText("")







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
