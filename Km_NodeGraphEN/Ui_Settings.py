# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_v02 - SettingsmtIZoa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SettingsWindowUI(object):
    def setupUi(self, SettingsWindowUI):
        if not SettingsWindowUI.objectName():
            SettingsWindowUI.setObjectName(u"SettingsWindowUI")
        SettingsWindowUI.resize(573, 439)
        self.centralwidget = QWidget(SettingsWindowUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 531, 251))
        self.checkBox_fade_effect = QCheckBox(self.groupBox)
        self.checkBox_fade_effect.setObjectName(u"checkBox_fade_effect")
        self.checkBox_fade_effect.setGeometry(QRect(40, 100, 161, 17))
        self.checkBox_fade_effect.setChecked(True)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 180, 161, 20))
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(230, 60, 16, 131))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.horizontalSlider_ZoomScale = QSlider(self.groupBox)
        self.horizontalSlider_ZoomScale.setObjectName(u"horizontalSlider_ZoomScale")
        self.horizontalSlider_ZoomScale.setGeometry(QRect(40, 210, 111, 22))
        self.horizontalSlider_ZoomScale.setMinimum(1)
        self.horizontalSlider_ZoomScale.setMaximum(3)
        self.horizontalSlider_ZoomScale.setValue(2)
        self.horizontalSlider_ZoomScale.setOrientation(Qt.Horizontal)
        self.checkBox_shake_effect = QCheckBox(self.groupBox)
        self.checkBox_shake_effect.setObjectName(u"checkBox_shake_effect")
        self.checkBox_shake_effect.setGeometry(QRect(40, 70, 91, 17))
        self.checkBox_shake_effect.setChecked(True)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 140, 51, 20))
        self.lineEdit_shortcut = QLineEdit(self.groupBox)
        self.lineEdit_shortcut.setObjectName(u"lineEdit_shortcut")
        self.lineEdit_shortcut.setGeometry(QRect(100, 140, 91, 20))
        self.checkBox_zoom_effect = QCheckBox(self.groupBox)
        self.checkBox_zoom_effect.setObjectName(u"checkBox_zoom_effect")
        self.checkBox_zoom_effect.setGeometry(QRect(40, 40, 91, 17))
        self.label_ZoomScale = QLabel(self.groupBox)
        self.label_ZoomScale.setObjectName(u"label_ZoomScale")
        self.label_ZoomScale.setGeometry(QRect(170, 210, 31, 20))
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(340, 30, 121, 20))
        self.lineEdit_columnn = QLineEdit(self.groupBox)
        self.lineEdit_columnn.setObjectName(u"lineEdit_columnn")
        self.lineEdit_columnn.setGeometry(QRect(390, 60, 61, 20))
        self.lineEdit_columnn.setAlignment(Qt.AlignCenter)
        self.lineEdit_Rows = QLineEdit(self.groupBox)
        self.lineEdit_Rows.setObjectName(u"lineEdit_Rows")
        self.lineEdit_Rows.setGeometry(QRect(390, 90, 61, 20))
        self.lineEdit_Rows.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 60, 71, 20))
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(300, 90, 71, 20))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 120, 91, 20))
        self.lineEdit_Button_width = QLineEdit(self.groupBox)
        self.lineEdit_Button_width.setObjectName(u"lineEdit_Button_width")
        self.lineEdit_Button_width.setGeometry(QRect(390, 120, 61, 20))
        self.lineEdit_Button_width.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(300, 150, 91, 20))
        self.lineEdit_ButtonHeight = QLineEdit(self.groupBox)
        self.lineEdit_ButtonHeight.setObjectName(u"lineEdit_ButtonHeight")
        self.lineEdit_ButtonHeight.setGeometry(QRect(390, 150, 61, 20))
        self.lineEdit_ButtonHeight.setAlignment(Qt.AlignCenter)
        self.pushButton_save = QPushButton(self.groupBox)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(400, 200, 101, 35))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(0, 170, 127);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 197, 145);\n"
"	border: 2px solidrgb(0, 197, 145);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 170, 127);\n"
"	border: 2px solid rgb(0, 170, 127);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Km_NodeGraphEN/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon)
        self.pushButton_setDefault = QPushButton(self.groupBox)
        self.pushButton_setDefault.setObjectName(u"pushButton_setDefault")
        self.pushButton_setDefault.setGeometry(QRect(270, 200, 101, 35))
        self.pushButton_setDefault.setFont(font)
        self.pushButton_setDefault.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Km_NodeGraphEN/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setDefault.setIcon(icon1)
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 270, 531, 131))
        self.pushButton_OpenPDF = QPushButton(self.groupBox_7)
        self.pushButton_OpenPDF.setObjectName(u"pushButton_OpenPDF")
        self.pushButton_OpenPDF.setGeometry(QRect(400, 95, 111, 23))
        self.label_icon_2 = QLabel(self.groupBox_7)
        self.label_icon_2.setObjectName(u"label_icon_2")
        self.label_icon_2.setGeometry(QRect(420, 15, 87, 71))
        self.label_icon_2.setFrameShape(QFrame.NoFrame)
        self.label_icon_2.setPixmap(QPixmap(u"../Km_NodeGraphEN/icons/mouse.png"))
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 55, 227, 20))
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 89, 171, 19))
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 30, 227, 19))
        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 90, 227, 19))
        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(220, 10, 171, 81))
        self.label_15.setWordWrap(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 400, 531, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_plugins_version = QLabel(self.layoutWidget)
        self.label_plugins_version.setObjectName(u"label_plugins_version")

        self.horizontalLayout_2.addWidget(self.label_plugins_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_credit = QLabel(self.layoutWidget)
        self.label_credit.setObjectName(u"label_credit")

        self.verticalLayout.addWidget(self.label_credit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 3)
        SettingsWindowUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindowUI)

        QMetaObject.connectSlotsByName(SettingsWindowUI)
    # setupUi

    def retranslateUi(self, SettingsWindowUI):
        SettingsWindowUI.setWindowTitle(QCoreApplication.translate("SettingsWindowUI", u"Km NodeGraph Easy Navigate : Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWindowUI", u"settings", None))
        self.checkBox_fade_effect.setText(QCoreApplication.translate("SettingsWindowUI", u"Main Window Fade In Effect", None))
        self.label.setText(QCoreApplication.translate("SettingsWindowUI", u"Node Graph Zoom Scale", None))
        self.checkBox_shake_effect.setText(QCoreApplication.translate("SettingsWindowUI", u"Shake Effect", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWindowUI", u"Shortcut", None))
        self.lineEdit_shortcut.setText(QCoreApplication.translate("SettingsWindowUI", u"shift+e", None))
        self.checkBox_zoom_effect.setText(QCoreApplication.translate("SettingsWindowUI", u"Zoom Effect", None))
        self.label_ZoomScale.setText(QCoreApplication.translate("SettingsWindowUI", u"1.2", None))
        self.label_12.setText(QCoreApplication.translate("SettingsWindowUI", u"Bookmarks Grid ", None))
        self.lineEdit_columnn.setText(QCoreApplication.translate("SettingsWindowUI", u"3", None))
        self.lineEdit_Rows.setText(QCoreApplication.translate("SettingsWindowUI", u"3", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindowUI", u"Columns : ", None))
        self.label_13.setText(QCoreApplication.translate("SettingsWindowUI", u"Rows :", None))
        self.label_10.setText(QCoreApplication.translate("SettingsWindowUI", u"Button Width : ", None))
        self.lineEdit_Button_width.setText(QCoreApplication.translate("SettingsWindowUI", u"110", None))
        self.label_11.setText(QCoreApplication.translate("SettingsWindowUI", u"Button Height :", None))
        self.lineEdit_ButtonHeight.setText(QCoreApplication.translate("SettingsWindowUI", u"50", None))
        self.pushButton_save.setText(QCoreApplication.translate("SettingsWindowUI", u"  Save", None))
        self.pushButton_setDefault.setText(QCoreApplication.translate("SettingsWindowUI", u"Reset", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("SettingsWindowUI", u"Tips", None))
        self.pushButton_OpenPDF.setText(QCoreApplication.translate("SettingsWindowUI", u"Open PDF Help", None))
        self.label_icon_2.setText("")
        self.label_4.setText(QCoreApplication.translate("SettingsWindowUI", u"                         Assign New Bookmark", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindowUI", u"Right Button  :    Remove", None))
        self.label_9.setText(QCoreApplication.translate("SettingsWindowUI", u"Left Button    :  Jump to Bookmark", None))
        self.label_14.setText(QCoreApplication.translate("SettingsWindowUI", u"Middle Button :   Edit", None))
        self.label_15.setText(QCoreApplication.translate("SettingsWindowUI", u"Assign Bookmark : Select a node or backdrop, Then click on an empty bookmark to assign", None))
        self.label_plugins_version.setText(QCoreApplication.translate("SettingsWindowUI", u"Km NodeGraph Easy Navigate v2.0", None))
        self.label_credit.setText(QCoreApplication.translate("SettingsWindowUI", u"By Hossein Karamian", None))
    # retranslateUi

