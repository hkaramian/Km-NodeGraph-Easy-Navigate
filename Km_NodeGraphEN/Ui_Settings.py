# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_v02 - SettingspHFwyN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Pyside Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer
from PysideImport import *

import os

class Ui_SettingsWindowUI(object):
    def setupUi(self, SettingsWindowUI):
        if not SettingsWindowUI.objectName():
            SettingsWindowUI.setObjectName(u"SettingsWindowUI")
        SettingsWindowUI.resize(635, 557)
        font = QFont()
        font.setFamily(u"Segoe UI")
        SettingsWindowUI.setFont(font)
        SettingsWindowUI.setStyleSheet(u"color: rgb(223, 223, 223);")
        self.centralwidget = QWidget(SettingsWindowUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 611, 541))
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
"	background-position: center;\n"
"	background-rep"
                        "eat: no-reperat;\n"
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
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover"
                        " {\n"
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

        self.label_8 = QLabel(self.frame_label_top_btns)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(20, 0))
        self.label_8.setMaximumSize(QSize(20, 20))
        self.label_8.setText(u"")
        self.label_8.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/cil-settings.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setMargin(0)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_title_bar_top.setFont(font1)
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
        self.frame_2.setGeometry(QRect(20, 59, 571, 271))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color: rgb(51, 54, 63);\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_ZoomScale = QLabel(self.frame_2)
        self.label_ZoomScale.setObjectName(u"label_ZoomScale")
        self.label_ZoomScale.setGeometry(QRect(180, 220, 41, 20))
        self.label_ZoomScale.setFont(font)
        self.label_ZoomScale.setText(u"1.2")
        self.checkBox_fade_effect = QCheckBox(self.frame_2)
        self.checkBox_fade_effect.setObjectName(u"checkBox_fade_effect")
        self.checkBox_fade_effect.setGeometry(QRect(50, 110, 211, 25))
        self.checkBox_fade_effect.setFont(font)
        self.checkBox_fade_effect.setText(u"Main Window Fade In Effect")
        self.checkBox_fade_effect.setChecked(True)
        self.checkBox_shake_effect = QCheckBox(self.frame_2)
        self.checkBox_shake_effect.setObjectName(u"checkBox_shake_effect")
        self.checkBox_shake_effect.setGeometry(QRect(50, 76, 161, 25))
        self.checkBox_shake_effect.setFont(font)
        self.checkBox_shake_effect.setText(u"Shake Effect")
        self.checkBox_shake_effect.setChecked(True)
        self.checkBox_zoom_effect = QCheckBox(self.frame_2)
        self.checkBox_zoom_effect.setObjectName(u"checkBox_zoom_effect")
        self.checkBox_zoom_effect.setGeometry(QRect(50, 40, 141, 25))
        self.checkBox_zoom_effect.setFont(font)
        self.checkBox_zoom_effect.setText(u"Zoom Effect")
        self.horizontalSlider_ZoomScale = QSlider(self.frame_2)
        self.horizontalSlider_ZoomScale.setObjectName(u"horizontalSlider_ZoomScale")
        self.horizontalSlider_ZoomScale.setGeometry(QRect(50, 220, 111, 22))
        self.horizontalSlider_ZoomScale.setStyleSheet(u"")
        self.horizontalSlider_ZoomScale.setMinimum(5)
        self.horizontalSlider_ZoomScale.setMaximum(20)
        self.horizontalSlider_ZoomScale.setSingleStep(1)
        self.horizontalSlider_ZoomScale.setValue(10)
        self.horizontalSlider_ZoomScale.setOrientation(Qt.Horizontal)
        self.lineEdit_shortcut = QLineEdit(self.frame_2)
        self.lineEdit_shortcut.setObjectName(u"lineEdit_shortcut")
        self.lineEdit_shortcut.setGeometry(QRect(107, 147, 91, 30))
        self.lineEdit_shortcut.setFont(font)
        self.lineEdit_shortcut.setStyleSheet(u"")
        self.lineEdit_shortcut.setText(u"shift+e")
        self.lineEdit_shortcut.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 151, 51, 20))
        self.label_6.setFont(font)
        self.label_6.setText(u"Shortcut")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 190, 181, 20))
        self.label.setFont(font)
        self.label.setText(u"Node Graph Zoom Scale")
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(280, 60, 1, 180))
        self.line.setStyleSheet(u"background-color: rgb(78, 85, 106);\n"
"width : 2px")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(340, 175, 101, 30))
        self.label_11.setFont(font)
        self.label_11.setText(u"Button Height :")
        self.lineEdit_columnn = QLineEdit(self.frame_2)
        self.lineEdit_columnn.setObjectName(u"lineEdit_columnn")
        self.lineEdit_columnn.setGeometry(QRect(450, 64, 61, 30))
        self.lineEdit_columnn.setFont(font)
        self.lineEdit_columnn.setText(u"3")
        self.lineEdit_columnn.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 64, 71, 30))
        self.label_5.setFont(font)
        self.label_5.setText(u"Columns : ")
        self.lineEdit_Rows = QLineEdit(self.frame_2)
        self.lineEdit_Rows.setObjectName(u"lineEdit_Rows")
        self.lineEdit_Rows.setGeometry(QRect(450, 101, 61, 30))
        self.lineEdit_Rows.setFont(font)
        self.lineEdit_Rows.setText(u"3")
        self.lineEdit_Rows.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(340, 138, 101, 30))
        self.label_10.setFont(font)
        self.label_10.setText(u"Button Width : ")
        self.lineEdit_Button_width = QLineEdit(self.frame_2)
        self.lineEdit_Button_width.setObjectName(u"lineEdit_Button_width")
        self.lineEdit_Button_width.setGeometry(QRect(450, 138, 61, 30))
        self.lineEdit_Button_width.setFont(font)
        self.lineEdit_Button_width.setText(u"110")
        self.lineEdit_Button_width.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(378, 40, 121, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(9)
        self.label_12.setFont(font2)
        self.label_12.setText(u"Bookmarks Grid ")
        self.lineEdit_ButtonHeight = QLineEdit(self.frame_2)
        self.lineEdit_ButtonHeight.setObjectName(u"lineEdit_ButtonHeight")
        self.lineEdit_ButtonHeight.setGeometry(QRect(450, 175, 61, 30))
        self.lineEdit_ButtonHeight.setFont(font)
        self.lineEdit_ButtonHeight.setText(u"50")
        self.lineEdit_ButtonHeight.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(340, 101, 71, 30))
        self.label_13.setFont(font)
        self.label_13.setText(u"Rows :")
        self.pushButton_save = QPushButton(self.frame_2)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(440, 220, 101, 35))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setWeight(50)
        self.pushButton_save.setFont(font3)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(126, 177, 85);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(140, 188, 100);\n"
"	border: 2px solidrgb(140, 188, 100);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(126, 177, 85);\n"
"	border: 2px solid rgb(126, 177, 85);\n"
"}")
        self.pushButton_save.setText(u"  Save")
        icon2 = QIcon()
        icon2.addFile(os.path.dirname(__file__)+"/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon2)
        self.pushButton_setDefault = QPushButton(self.frame_2)
        self.pushButton_setDefault.setObjectName(u"pushButton_setDefault")
        self.pushButton_setDefault.setGeometry(QRect(310, 220, 101, 35))
        self.pushButton_setDefault.setFont(font3)
        self.pushButton_setDefault.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_setDefault.setText(u"Reset")
        icon3 = QIcon()
        icon3.addFile(os.path.dirname(__file__)+"/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setDefault.setIcon(icon3)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 5, 571, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(13)
        self.label_2.setFont(font4)
        self.label_2.setText(u"Settings")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 350, 571, 151))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"background-color:rgb(51, 54, 63);\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 2, 571, 31))
        self.label_7.setFont(font4)
        self.label_7.setText(u"Tips")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 80, 227, 19))
        self.label_14.setFont(font)
        self.label_14.setText(u"<strong>Middle Button :</strong>   Edit")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 30, 227, 19))
        self.label_9.setFont(font)
        self.label_9.setText(u"<strong>Left Button    :  </strong>Jump to Bookmark")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(97, 50, 131, 20))
        self.label_4.setFont(font)
        self.label_4.setText(u"Assign New Bookmark")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 171, 19))
        self.label_3.setFont(font)
        self.label_3.setText(u"<strong>Right Button  : </strong>   Remove")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(360, 32, 181, 61))
        self.label_15.setFont(font)
        self.label_15.setText(u"<strong>Assign Bookmark :</strong> Select a node or backdrop, Then click on an empty bookmark button to assign")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.pushButton_OpenPDF = QPushButton(self.frame_3)
        self.pushButton_OpenPDF.setObjectName(u"pushButton_OpenPDF")
        self.pushButton_OpenPDF.setGeometry(QRect(233, 110, 130, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(10)
        self.pushButton_OpenPDF.setFont(font5)
        self.pushButton_OpenPDF.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_OpenPDF.setText(u"Open PDF Help")
        icon4 = QIcon()
        icon4.addFile(os.path.dirname(__file__)+"/icons/cil-lightbulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_OpenPDF.setIcon(icon4)
        self.label_icon_2 = QLabel(self.frame_3)
        self.label_icon_2.setObjectName(u"label_icon_2")
        self.label_icon_2.setGeometry(QRect(270, 40, 31, 41))
        self.label_icon_2.setFrameShape(QFrame.NoFrame)
        self.label_icon_2.setText(u"")
        self.label_icon_2.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/cil-mouse.png"))
        self.label_icon_2.setScaledContents(False)
        self.pushButton_BuyMeACoffee = QPushButton(self.frame_3)
        self.pushButton_BuyMeACoffee.setObjectName(u"pushButton_BuyMeACoffee")
        self.pushButton_BuyMeACoffee.setGeometry(QRect(394, 110, 130, 31))
        self.pushButton_BuyMeACoffee.setFont(font5)
        self.pushButton_BuyMeACoffee.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_BuyMeACoffee.setText(u"Buy Me a Coffee")
        icon5 = QIcon()
        icon5.addFile(os.path.dirname(__file__)+"/icons/cil-heart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_BuyMeACoffee.setIcon(icon5)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(230, 90, 141, 20))
        self.label_17.setFont(font)
        self.label_17.setText(u"Learn all in 3 minutes")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(390, 90, 141, 20))
        self.label_18.setFont(font)
        self.label_18.setText(u"Do you like this tool?")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 504, 571, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_plugins_version = QLabel(self.layoutWidget)
        self.label_plugins_version.setObjectName(u"label_plugins_version")
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        self.label_plugins_version.setFont(font6)
        self.label_plugins_version.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_plugins_version.setText(u"Km NodeGraph Easy Navigate v2.0")

        self.horizontalLayout_2.addWidget(self.label_plugins_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_credit = QLabel(self.layoutWidget)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setFont(font6)
        self.label_credit.setStyleSheet(u"color: rgb(200, 200, 200);")
        self.label_credit.setText(u"By Hossein Karamian")
        self.label_credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_credit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 3)
        SettingsWindowUI.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.checkBox_zoom_effect, self.checkBox_shake_effect)
        QWidget.setTabOrder(self.checkBox_shake_effect, self.checkBox_fade_effect)
        QWidget.setTabOrder(self.checkBox_fade_effect, self.lineEdit_shortcut)
        QWidget.setTabOrder(self.lineEdit_shortcut, self.horizontalSlider_ZoomScale)
        QWidget.setTabOrder(self.horizontalSlider_ZoomScale, self.lineEdit_columnn)
        QWidget.setTabOrder(self.lineEdit_columnn, self.lineEdit_Rows)
        QWidget.setTabOrder(self.lineEdit_Rows, self.lineEdit_Button_width)
        QWidget.setTabOrder(self.lineEdit_Button_width, self.lineEdit_ButtonHeight)
        QWidget.setTabOrder(self.lineEdit_ButtonHeight, self.pushButton_save)
        QWidget.setTabOrder(self.pushButton_save, self.pushButton_setDefault)
        QWidget.setTabOrder(self.pushButton_setDefault, self.pushButton_OpenPDF)
        QWidget.setTabOrder(self.pushButton_OpenPDF, self.pushButton_BuyMeACoffee)
        QWidget.setTabOrder(self.pushButton_BuyMeACoffee, self.pushButton_minimize)
        QWidget.setTabOrder(self.pushButton_minimize, self.pushButton_close)

        self.retranslateUi(SettingsWindowUI)

        QMetaObject.connectSlotsByName(SettingsWindowUI)
    # setupUi

    def retranslateUi(self, SettingsWindowUI):
        SettingsWindowUI.setWindowTitle(QCoreApplication.translate("SettingsWindowUI", u"Km NodeGraph Easy Navigate - Settings", None))
        self.label_16.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("SettingsWindowUI", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("SettingsWindowUI", u"Close", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

