# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_v02 - Bookmarks ListumliZW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Pyside Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer
from PysideImport import *

import os

class Ui_EditBookmarksWindowUI(object):
    def setupUi(self, EditBookmarksWindowUI):
        if not EditBookmarksWindowUI.objectName():
            EditBookmarksWindowUI.setObjectName(u"EditBookmarksWindowUI")
        EditBookmarksWindowUI.resize(633, 545)
        self.centralwidget = QWidget(EditBookmarksWindowUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 611, 521))
        self.frame.setStyleSheet(u"QLabel {\n"
"color: rgb(223, 223, 223);\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(61, 64, 71);\n"
"	border-radius : 10px;\n"
"}\n"
"\n"
"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(40, 43, 50);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(40, 43, 50);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(61, 64, 71);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(255, 212, 95);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
" "
                        "    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(../Km_NodeGraphEN/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
""
                        "QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
""
                        "	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(255, 212, 95);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(255, 222, 110);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 212, 95);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, "
                        "59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_top_btns = QFrame(self.frame)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setGeometry(QRect(0, 0, 611, 42))
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(40, 43, 50);\n"
"border-bottom-left-radius: 1px;\n"
"border-bottom-right-radius: 1px;")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.label_16 = QLabel(self.frame_label_top_btns)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(3, 16777215))

        self.horizontalLayout_10.addWidget(self.label_16)

        self.label_9 = QLabel(self.frame_label_top_btns)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(20, 0))
        self.label_9.setMaximumSize(QSize(20, 20))
        self.label_9.setText(u"")
        self.label_9.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/cil-menu.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(0)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")
        self.label_title_bar_top.setText(u"Km NodeGraph Easy Navigate")
        self.label_title_bar_top.setMargin(5)

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.frame_btns_right)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_minimize.sizePolicy().hasHeightForWidth())
        self.pushButton_minimize.setSizePolicy(sizePolicy1)
        self.pushButton_minimize.setMinimumSize(QSize(40, 0))
        self.pushButton_minimize.setMaximumSize(QSize(40, 16777215))
        self.pushButton_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 55, 65);\n"
"	border-radius : 0px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(40, 50, 62);\n"
"}")
        self.pushButton_minimize.setText(u"")
        icon = QIcon()
        icon.addFile(os.path.dirname(__file__)+"/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.pushButton_minimize)

        self.pushButton_close = QPushButton(self.frame_btns_right)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy1.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy1)
        self.pushButton_close.setMinimumSize(QSize(40, 0))
        self.pushButton_close.setMaximumSize(QSize(40, 16777215))
        self.pushButton_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 55, 65);\n"
"	border-top-right-radius: 10px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(40, 50, 62);\n"
"}")
        self.pushButton_close.setText(u"")
        icon1 = QIcon()
        icon1.addFile(os.path.dirname(__file__)+"/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.pushButton_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 59, 571, 425))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color: rgb(51, 54, 63);\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 5, 571, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_2.setText(u"Edit Bookmarks")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.tableWidget_BookmarksList = QTableWidget(self.frame_2)
        if (self.tableWidget_BookmarksList.columnCount() < 4):
            self.tableWidget_BookmarksList.setColumnCount(4)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_BookmarksList.rowCount() < 2):
            self.tableWidget_BookmarksList.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setItem(1, 2, __qtablewidgetitem11)
        self.tableWidget_BookmarksList.setObjectName(u"tableWidget_BookmarksList")
        self.tableWidget_BookmarksList.setGeometry(QRect(10, 33, 551, 331))
        self.tableWidget_BookmarksList.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(51, 54, 63);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(61, 64, 71);\n"
"	border-bottom: 1px solid rgb(51, 54, 63);\n"
"	color : rgb(190, 190, 198);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color:  rgb(61, 64, 71);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color:  rgb(61, 64, 71);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(40, 43, 50);\n"
"	background-color: rgb(40, 43, 50);\n"
"	border-radius: 15px;\n"
"	color : rgb(190, 190, 198);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(255, 212, 95);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(61, 64, 71);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(51, 54, 63);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(61, 64, 71"
                        ");\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(61, 64, 71);\n"
"    border-right: 1px solid rgb(61, 64, 71);\n"
"	font-size : 13px\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(102, 157, 178);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(102, 157, 178);\n"
"	background-color: rgb(102, 157, 178);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color : rgb(255, 255, 255);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(61, 64, 71);\n"
"}\n"
"")
        self.tableWidget_BookmarksList.setFrameShape(QFrame.NoFrame)
        self.tableWidget_BookmarksList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_BookmarksList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_BookmarksList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_BookmarksList.setShowGrid(True)
        self.tableWidget_BookmarksList.setGridStyle(Qt.SolidLine)
        self.tableWidget_BookmarksList.setSortingEnabled(False)
        self.tableWidget_BookmarksList.setWordWrap(True)
        self.tableWidget_BookmarksList.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_BookmarksList.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_BookmarksList.horizontalHeader().setHighlightSections(True)
        self.tableWidget_BookmarksList.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_BookmarksList.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_BookmarksList.verticalHeader().setVisible(False)
        self.tableWidget_BookmarksList.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_BookmarksList.verticalHeader().setStretchLastSection(False)
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 370, 561, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_shiftUp = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_shiftUp.setObjectName(u"pushButton_shiftUp")
        self.pushButton_shiftUp.setMinimumSize(QSize(35, 35))
        self.pushButton_shiftUp.setMaximumSize(QSize(35, 35))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        self.pushButton_shiftUp.setFont(font3)
        self.pushButton_shiftUp.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(140, 188, 100);\n"
"	border: 2px solid rgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_shiftUp.setText(u"")
        icon2 = QIcon()
        icon2.addFile(os.path.dirname(__file__)+"/icons/cil-arrow-circle-top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_shiftUp.setIcon(icon2)
        self.pushButton_shiftUp.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_shiftUp)

        self.pushButton_shiftDown = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_shiftDown.setObjectName(u"pushButton_shiftDown")
        self.pushButton_shiftDown.setMinimumSize(QSize(35, 35))
        self.pushButton_shiftDown.setMaximumSize(QSize(35, 35))
        self.pushButton_shiftDown.setFont(font3)
        self.pushButton_shiftDown.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(140, 188, 100);\n"
"	border: 2px solid rgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_shiftDown.setText(u"")
        icon3 = QIcon()
        icon3.addFile(os.path.dirname(__file__)+"/icons/cil-arrow-circle-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_shiftDown.setIcon(icon3)
        self.pushButton_shiftDown.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_shiftDown)

        self.pushButton_AddBookmark = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_AddBookmark.setObjectName(u"pushButton_AddBookmark")
        self.pushButton_AddBookmark.setMinimumSize(QSize(35, 35))
        self.pushButton_AddBookmark.setMaximumSize(QSize(35, 35))
        self.pushButton_AddBookmark.setFont(font3)
        self.pushButton_AddBookmark.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(140, 188, 100);\n"
"	border: 2px solid rgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_AddBookmark.setText(u"")
        icon4 = QIcon()
        icon4.addFile(os.path.dirname(__file__)+"/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_AddBookmark.setIcon(icon4)
        self.pushButton_AddBookmark.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_AddBookmark)

        self.pushButton_removeItem = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_removeItem.setObjectName(u"pushButton_removeItem")
        self.pushButton_removeItem.setMinimumSize(QSize(35, 35))
        self.pushButton_removeItem.setMaximumSize(QSize(35, 35))
        self.pushButton_removeItem.setFont(font3)
        self.pushButton_removeItem.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(140, 188, 100);\n"
"	border: 2px solid rgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_removeItem.setText(u"")
        icon5 = QIcon()
        icon5.addFile(os.path.dirname(__file__)+"/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_removeItem.setIcon(icon5)
        self.pushButton_removeItem.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_removeItem)

        self.pushButton_createFromBackdrops = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_createFromBackdrops.setObjectName(u"pushButton_createFromBackdrops")
        self.pushButton_createFromBackdrops.setMinimumSize(QSize(35, 35))
        self.pushButton_createFromBackdrops.setMaximumSize(QSize(35, 35))
        self.pushButton_createFromBackdrops.setFont(font3)
        self.pushButton_createFromBackdrops.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(140, 188, 100);\n"
"	border: 2px solid rgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_createFromBackdrops.setText(u"")
        icon6 = QIcon()
        icon6.addFile(os.path.dirname(__file__)+"/icons/cil-smile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_createFromBackdrops.setIcon(icon6)
        self.pushButton_createFromBackdrops.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_createFromBackdrops)

        self.pushButton_reset = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setMinimumSize(QSize(35, 35))
        self.pushButton_reset.setMaximumSize(QSize(35, 35))
        self.pushButton_reset.setFont(font3)
        self.pushButton_reset.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(140, 188, 100);\n"
"	border: 2px solid rgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_reset.setText(u"")
        icon7 = QIcon()
        icon7.addFile(os.path.dirname(__file__)+"/icons/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_reset.setIcon(icon7)
        self.pushButton_reset.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_reset)

        self.checkBox_for_fake_focus = QCheckBox(self.frame_2)
        self.checkBox_for_fake_focus.setObjectName(u"checkBox_for_fake_focus")
        self.checkBox_for_fake_focus.setGeometry(QRect(70, 10, 0, 0))
        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 483, 571, 36))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_plugins_version = QLabel(self.layoutWidget_2)
        self.label_plugins_version.setObjectName(u"label_plugins_version")
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        self.label_plugins_version.setFont(font4)
        self.label_plugins_version.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_plugins_version.setText(u"Km NodeGraph Easy Navigate v2.0")

        self.horizontalLayout_3.addWidget(self.label_plugins_version)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_credit = QLabel(self.layoutWidget_2)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setFont(font4)
        self.label_credit.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_credit.setText(u"By Hossein Karamian")
        self.label_credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_credit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 28)
        self.horizontalLayout_3.setStretch(2, 3)
        self.frame_top_btns.raise_()
        self.layoutWidget_2.raise_()
        self.frame_2.raise_()
        EditBookmarksWindowUI.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.checkBox_for_fake_focus, self.pushButton_minimize)
        QWidget.setTabOrder(self.pushButton_minimize, self.pushButton_shiftUp)
        QWidget.setTabOrder(self.pushButton_shiftUp, self.pushButton_shiftDown)
        QWidget.setTabOrder(self.pushButton_shiftDown, self.pushButton_AddBookmark)
        QWidget.setTabOrder(self.pushButton_AddBookmark, self.pushButton_removeItem)
        QWidget.setTabOrder(self.pushButton_removeItem, self.pushButton_createFromBackdrops)
        QWidget.setTabOrder(self.pushButton_createFromBackdrops, self.pushButton_reset)
        QWidget.setTabOrder(self.pushButton_reset, self.pushButton_close)
        QWidget.setTabOrder(self.pushButton_close, self.tableWidget_BookmarksList)

        self.retranslateUi(EditBookmarksWindowUI)

        QMetaObject.connectSlotsByName(EditBookmarksWindowUI)
    # setupUi

    def retranslateUi(self, EditBookmarksWindowUI):
        EditBookmarksWindowUI.setWindowTitle(QCoreApplication.translate("EditBookmarksWindowUI", u"Km NodeGraph Easy Navigate : Edit Bookmarks", None))
        self.label_16.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Close", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableWidget_BookmarksList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"Index (Order)", None));
        ___qtablewidgetitem1 = self.tableWidget_BookmarksList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"Node Name", None));
        ___qtablewidgetitem2 = self.tableWidget_BookmarksList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"Title", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Copy url to clipboard", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.tableWidget_BookmarksList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"Shortcut", None));
        ___qtablewidgetitem4 = self.tableWidget_BookmarksList.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget_BookmarksList.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"2", None));

        __sortingEnabled = self.tableWidget_BookmarksList.isSortingEnabled()
        self.tableWidget_BookmarksList.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget_BookmarksList.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget_BookmarksList.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"test", None));
        ___qtablewidgetitem8 = self.tableWidget_BookmarksList.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"2", None));
        ___qtablewidgetitem9 = self.tableWidget_BookmarksList.item(1, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"tt", None));
        self.tableWidget_BookmarksList.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.pushButton_shiftUp.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Change order (move up)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_shiftDown.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Change order (move down)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_AddBookmark.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Assign Selected Node to Selected Bookmark", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_removeItem.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Remove (Set Empty) Selected Bookmark", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_createFromBackdrops.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Create Bookmarks From Backdrops", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_reset.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Remove (Set Empty) All Bookmarks", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_for_fake_focus.setText("")
    # retranslateUi

