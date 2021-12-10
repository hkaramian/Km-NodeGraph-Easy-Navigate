# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_v02 - TemplatesKsqUVU.ui'
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


class Ui_TemplatesWindowUI(object):
    def setupUi(self, TemplatesWindowUI):
        if not TemplatesWindowUI.objectName():
            TemplatesWindowUI.setObjectName(u"TemplatesWindowUI")
        TemplatesWindowUI.resize(506, 621)
        self.centralwidget = QWidget(TemplatesWindowUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 20, 481, 551))
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 20, 461, 241))
        self.pushButton_load = QPushButton(self.groupBox_6)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setGeometry(QRect(130, 200, 81, 23))
        self.pushButton_remove = QPushButton(self.groupBox_6)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setGeometry(QRect(30, 200, 81, 23))
        self.listWidget_templateList = QListWidget(self.groupBox_6)
        QListWidgetItem(self.listWidget_templateList)
        QListWidgetItem(self.listWidget_templateList)
        QListWidgetItem(self.listWidget_templateList)
        QListWidgetItem(self.listWidget_templateList)
        self.listWidget_templateList.setObjectName(u"listWidget_templateList")
        self.listWidget_templateList.setGeometry(QRect(20, 60, 201, 121))
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 61, 21))
        self.listWidget_templateItems = QListWidget(self.groupBox_6)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        QListWidgetItem(self.listWidget_templateItems)
        self.listWidget_templateItems.setObjectName(u"listWidget_templateItems")
        self.listWidget_templateItems.setGeometry(QRect(240, 60, 201, 121))
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 30, 141, 21))
        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(240, 280, 231, 251))
        self.pushButton_add = QPushButton(self.groupBox_4)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(80, 210, 81, 23))
        self.listWidget_newTemplateItems = QListWidget(self.groupBox_4)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        QListWidgetItem(self.listWidget_newTemplateItems)
        self.listWidget_newTemplateItems.setObjectName(u"listWidget_newTemplateItems")
        self.listWidget_newTemplateItems.setGeometry(QRect(10, 50, 201, 121))
        self.lineEdit_templateName = QLineEdit(self.groupBox_4)
        self.lineEdit_templateName.setObjectName(u"lineEdit_templateName")
        self.lineEdit_templateName.setGeometry(QRect(112, 180, 101, 20))
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 180, 101, 21))
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 181, 21))
        self.groupBox = QGroupBox(self.groupBox_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 280, 211, 251))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 100, 181, 16))
        self.checkBox_TemplateOverride = QCheckBox(self.groupBox)
        self.checkBox_TemplateOverride.setObjectName(u"checkBox_TemplateOverride")
        self.checkBox_TemplateOverride.setGeometry(QRect(30, 70, 181, 31))
        self.comboBox_TemplateOverride = QComboBox(self.groupBox)
        self.comboBox_TemplateOverride.addItem("")
        self.comboBox_TemplateOverride.addItem("")
        self.comboBox_TemplateOverride.addItem("")
        self.comboBox_TemplateOverride.addItem("")
        self.comboBox_TemplateOverride.setObjectName(u"comboBox_TemplateOverride")
        self.comboBox_TemplateOverride.setGeometry(QRect(60, 160, 101, 22))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 140, 141, 16))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 570, 481, 36))
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
        TemplatesWindowUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(TemplatesWindowUI)

        QMetaObject.connectSlotsByName(TemplatesWindowUI)
    # setupUi

    def retranslateUi(self, TemplatesWindowUI):
        TemplatesWindowUI.setWindowTitle(QCoreApplication.translate("TemplatesWindowUI", u"Km NodeGraph Easy Navigate : BookMarks Templates", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TemplatesWindowUI", u"BookMark Templates", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TemplatesWindowUI", u"List", None))
        self.pushButton_load.setText(QCoreApplication.translate("TemplatesWindowUI", u"Load", None))
        self.pushButton_remove.setText(QCoreApplication.translate("TemplatesWindowUI", u"Remove", None))

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

        self.label_3.setText(QCoreApplication.translate("TemplatesWindowUI", u"Templates:", None))

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

        self.label_8.setText(QCoreApplication.translate("TemplatesWindowUI", u"Selected Template Items:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TemplatesWindowUI", u"Add New Template", None))
        self.pushButton_add.setText(QCoreApplication.translate("TemplatesWindowUI", u"Add", None))

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

        self.label_4.setText(QCoreApplication.translate("TemplatesWindowUI", u"Template Name :", None))
        self.label_5.setText(QCoreApplication.translate("TemplatesWindowUI", u" Current Project Bookmarks:", None))
        self.groupBox.setTitle(QCoreApplication.translate("TemplatesWindowUI", u"Global Override", None))
        self.label_7.setText(QCoreApplication.translate("TemplatesWindowUI", u"(Use a template for all projects)", None))
        self.checkBox_TemplateOverride.setText(QCoreApplication.translate("TemplatesWindowUI", u"Template Global Override", None))
        self.comboBox_TemplateOverride.setItemText(0, QCoreApplication.translate("TemplatesWindowUI", u"Template 1", None))
        self.comboBox_TemplateOverride.setItemText(1, QCoreApplication.translate("TemplatesWindowUI", u"Template 2", None))
        self.comboBox_TemplateOverride.setItemText(2, QCoreApplication.translate("TemplatesWindowUI", u"Template 3", None))
        self.comboBox_TemplateOverride.setItemText(3, QCoreApplication.translate("TemplatesWindowUI", u"Template 4", None))

        self.label_9.setText(QCoreApplication.translate("TemplatesWindowUI", u"Select Template :", None))
        self.label_plugins_version.setText(QCoreApplication.translate("TemplatesWindowUI", u"Km NodeGraph Easy Navigate v2.0", None))
        self.label_credit.setText(QCoreApplication.translate("TemplatesWindowUI", u"By Hossein Karamian", None))
    # retranslateUi

