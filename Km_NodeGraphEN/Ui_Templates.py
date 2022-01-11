# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_v02 - TemplatesbXjwBY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Pyside Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer
from PysideImport import *

import os

class Ui_TemplatesWindowUI(object):
    def setupUi(self, TemplatesWindowUI):
        if not TemplatesWindowUI.objectName():
            TemplatesWindowUI.setObjectName(u"TemplatesWindowUI")
        TemplatesWindowUI.resize(906, 410)
        TemplatesWindowUI.setStyleSheet(u"color: rgb(223, 223, 223);")
        self.centralwidget = QWidget(TemplatesWindowUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(12, 12, 885, 391))
        self.frame.setStyleSheet(u"QFrame {\n"
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
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border"
                        ": none;\n"
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
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
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
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar:"
                        ":sub-line:vertical {\n"
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
"QRadioButton::indicator {\n"
"    border: 3px soli"
                        "d rgb(52, 59, 72);\n"
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
"    bord"
                        "er-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
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
        self.frame_top_btns.setGeometry(QRect(0, 0, 885, 42))
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

        self.label_10 = QLabel(self.frame_label_top_btns)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(20, 0))
        self.label_10.setMaximumSize(QSize(20, 20))
        self.label_10.setText(u"")
        self.label_10.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/cil-star.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(0)

        self.horizontalLayout_10.addWidget(self.label_10)

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
        self.frame_2.setGeometry(QRect(20, 63, 551, 291))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color: rgb(51, 54, 63);\n"
"border-radius: 5px;\n"
"}\n"
"QListWidget {\n"
"	background-color: rgb(63, 68, 88);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QListWidget::item {\n"
"padding: 5px;\n"
"}\n"
"QListWidget::item:hover {\n"
"padding: 5px;\n"
"	background-color: rgb(83, 89, 115);\n"
"}\n"
"QListWidget::item:selected {\n"
"	padding: 5px;\n"
"	background-color: rgb(83, 89, 115);\n"
"	color: rgb(223, 223, 223);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_remove = QPushButton(self.frame_2)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setGeometry(QRect(40, 244, 101, 35))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_remove.setFont(font1)
        self.pushButton_remove.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(57, 65, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_remove.setText(u"Remove")
        icon2 = QIcon()
        icon2.addFile(os.path.dirname(__file__)+"/icons/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_remove.setIcon(icon2)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 5, 571, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setText(u"BookMark Templates")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 33, 61, 21))
        self.label_3.setText(u"Templates:")
        self.listWidget_templateList = QListWidget(self.frame_2)
        QListWidgetItem(self.listWidget_templateList)
        QListWidgetItem(self.listWidget_templateList)
        QListWidgetItem(self.listWidget_templateList)
        QListWidgetItem(self.listWidget_templateList)
        self.listWidget_templateList.setObjectName(u"listWidget_templateList")
        self.listWidget_templateList.setGeometry(QRect(40, 60, 221, 171))
        self.listWidget_templateList.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 33, 141, 21))
        self.label_8.setText(u"Selected Template Items:")
        self.listWidget_templateItems = QListWidget(self.frame_2)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        self.listWidget_templateItems.setObjectName(u"listWidget_templateItems")
        self.listWidget_templateItems.setGeometry(QRect(290, 60, 221, 171))
        self.pushButton_load = QPushButton(self.frame_2)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setGeometry(QRect(160, 244, 101, 35))
        self.pushButton_load.setFont(font1)
        self.pushButton_load.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(57, 65, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_load.setText(u"Load")
        icon3 = QIcon()
        icon3.addFile(os.path.dirname(__file__)+"/icons/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_load.setIcon(icon3)
        self.checkBox_for_fake_focus = QCheckBox(self.frame_2)
        self.checkBox_for_fake_focus.setObjectName(u"checkBox_for_fake_focus")
        self.checkBox_for_fake_focus.setGeometry(QRect(20, 10, 0, 17))
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 353, 841, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_plugins_version = QLabel(self.layoutWidget)
        self.label_plugins_version.setObjectName(u"label_plugins_version")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        self.label_plugins_version.setFont(font3)
        self.label_plugins_version.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_plugins_version.setText(u"Km NodeGraph Easy Navigate v2.0")

        self.horizontalLayout_2.addWidget(self.label_plugins_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_credit = QLabel(self.layoutWidget)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setFont(font3)
        self.label_credit.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_credit.setText(u"By Hossein Karamian")
        self.label_credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_credit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 3)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(590, 63, 271, 291))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"background-color: rgb(51, 54, 63);\n"
"border-radius: 5px;\n"
"}\n"
"QListWidget {\n"
"	background-color: rgb(63, 68, 88);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QListWidget::item {\n"
"padding: 5px;\n"
"}\n"
"QListWidget::item:hover {\n"
"padding: 5px;\n"
"	background-color: rgb(83, 89, 115);\n"
"}\n"
"QListWidget::item:selected {\n"
"	padding: 5px;\n"
"	background-color: rgb(83, 89, 115);\n"
"	color: rgb(223, 223, 223);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 2, 271, 31))
        self.label_18.setFont(font2)
        self.label_18.setText(u"Add New Template")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.listWidget_newTemplateItems = QListWidget(self.frame_4)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        self.listWidget_newTemplateItems.setObjectName(u"listWidget_newTemplateItems")
        self.listWidget_newTemplateItems.setGeometry(QRect(20, 54, 221, 151))
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 181, 21))
        self.label_5.setText(u" Current Project Bookmarks:")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 216, 101, 21))
        self.label_4.setText(u"Template Name :")
        self.lineEdit_templateName = QLineEdit(self.frame_4)
        self.lineEdit_templateName.setObjectName(u"lineEdit_templateName")
        self.lineEdit_templateName.setGeometry(QRect(130, 213, 121, 30))
        self.lineEdit_templateName.setText(u"")
        self.pushButton_add = QPushButton(self.frame_4)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(90, 249, 101, 35))
        self.pushButton_add.setFont(font1)
        self.pushButton_add.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(57, 65, 80);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_add.setText(u"Add")
        icon4 = QIcon()
        icon4.addFile(os.path.dirname(__file__)+"/icons/cil-medical-cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon4)
        self.frame_top_btns.raise_()
        self.layoutWidget.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        TemplatesWindowUI.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.checkBox_for_fake_focus, self.pushButton_remove)
        QWidget.setTabOrder(self.pushButton_remove, self.listWidget_templateItems)
        QWidget.setTabOrder(self.listWidget_templateItems, self.listWidget_templateList)
        QWidget.setTabOrder(self.listWidget_templateList, self.pushButton_load)
        QWidget.setTabOrder(self.pushButton_load, self.listWidget_newTemplateItems)
        QWidget.setTabOrder(self.listWidget_newTemplateItems, self.lineEdit_templateName)
        QWidget.setTabOrder(self.lineEdit_templateName, self.pushButton_add)
        QWidget.setTabOrder(self.pushButton_add, self.pushButton_close)
        QWidget.setTabOrder(self.pushButton_close, self.pushButton_minimize)

        self.retranslateUi(TemplatesWindowUI)

        QMetaObject.connectSlotsByName(TemplatesWindowUI)
    # setupUi

    def retranslateUi(self, TemplatesWindowUI):
        TemplatesWindowUI.setWindowTitle(QCoreApplication.translate("TemplatesWindowUI", u"Km NodeGraph Easy Navigate : BookMarks Templates", None))
        self.label_16.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("TemplatesWindowUI", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("TemplatesWindowUI", u"Close", None))
#endif // QT_CONFIG(tooltip)

        __sortingEnabled = self.listWidget_templateList.isSortingEnabled()
        self.listWidget_templateList.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_templateList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("TemplatesWindowUI", u"Template 1", None));
        ___qlistwidgetitem1 = self.listWidget_templateList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("TemplatesWindowUI", u"Template 2", None));
        ___qlistwidgetitem2 = self.listWidget_templateList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("TemplatesWindowUI", u"Template 3", None));
        ___qlistwidgetitem3 = self.listWidget_templateList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("TemplatesWindowUI", u"Template 4", None));
        self.listWidget_templateList.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget_templateItems.isSortingEnabled()
        self.listWidget_templateItems.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.listWidget_templateItems.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("TemplatesWindowUI", u"Despill", None));
        ___qlistwidgetitem5 = self.listWidget_templateItems.item(1)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("TemplatesWindowUI", u"Key - Detail", None));
        ___qlistwidgetitem6 = self.listWidget_templateItems.item(2)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("TemplatesWindowUI", u"Render", None));
        ___qlistwidgetitem7 = self.listWidget_templateItems.item(3)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("TemplatesWindowUI", u"Plate", None));
        ___qlistwidgetitem8 = self.listWidget_templateItems.item(4)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("TemplatesWindowUI", u"Key - Core", None));
        ___qlistwidgetitem9 = self.listWidget_templateItems.item(5)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("TemplatesWindowUI", u"Clean", None));
        self.listWidget_templateItems.setSortingEnabled(__sortingEnabled1)

        self.checkBox_for_fake_focus.setText(QCoreApplication.translate("TemplatesWindowUI", u"CheckBox", None))

        __sortingEnabled2 = self.listWidget_newTemplateItems.isSortingEnabled()
        self.listWidget_newTemplateItems.setSortingEnabled(False)
        ___qlistwidgetitem10 = self.listWidget_newTemplateItems.item(0)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("TemplatesWindowUI", u"Despill", None));
        ___qlistwidgetitem11 = self.listWidget_newTemplateItems.item(1)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("TemplatesWindowUI", u"Key - Detail", None));
        ___qlistwidgetitem12 = self.listWidget_newTemplateItems.item(2)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("TemplatesWindowUI", u"Render", None));
        ___qlistwidgetitem13 = self.listWidget_newTemplateItems.item(3)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("TemplatesWindowUI", u"Plate", None));
        ___qlistwidgetitem14 = self.listWidget_newTemplateItems.item(4)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("TemplatesWindowUI", u"Key - Core", None));
        ___qlistwidgetitem15 = self.listWidget_newTemplateItems.item(5)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("TemplatesWindowUI", u"Clean", None));
        self.listWidget_newTemplateItems.setSortingEnabled(__sortingEnabled2)

    # retranslateUi

