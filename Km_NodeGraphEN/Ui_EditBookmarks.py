# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel_v02 - Bookmarks ListYOUAbY.ui'
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

import os 

class Ui_EditBookmarksWindowUI(object):
    def setupUi(self, EditBookmarksWindowUI):
        if not EditBookmarksWindowUI.objectName():
            EditBookmarksWindowUI.setObjectName(u"EditBookmarksWindowUI")
        EditBookmarksWindowUI.resize(599, 492)
        self.centralwidget = QWidget(EditBookmarksWindowUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 561, 371))
        self.tableWidget_BookmarksList = QTableWidget(self.groupBox)
        if (self.tableWidget_BookmarksList.columnCount() < 4):
            self.tableWidget_BookmarksList.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_BookmarksList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
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
        self.tableWidget_BookmarksList.setGeometry(QRect(20, 20, 521, 341))
        self.tableWidget_BookmarksList.setShowGrid(True)
        self.tableWidget_BookmarksList.setGridStyle(Qt.DashLine)
        self.tableWidget_BookmarksList.setSortingEnabled(True)
        self.tableWidget_BookmarksList.setWordWrap(True)
        self.tableWidget_BookmarksList.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_BookmarksList.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_BookmarksList.horizontalHeader().setHighlightSections(True)
        self.tableWidget_BookmarksList.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_BookmarksList.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_BookmarksList.verticalHeader().setVisible(False)
        self.tableWidget_BookmarksList.verticalHeader().setDefaultSectionSize(30)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 450, 561, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_plugins_version = QLabel(self.layoutWidget)
        self.label_plugins_version.setObjectName(u"label_plugins_version")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.label_plugins_version.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_plugins_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 390, 561, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_shiftUp = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_shiftUp.setObjectName(u"pushButton_shiftUp")
        self.pushButton_shiftUp.setMinimumSize(QSize(35, 35))
        self.pushButton_shiftUp.setMaximumSize(QSize(35, 35))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.pushButton_shiftUp.setFont(font1)
        self.pushButton_shiftUp.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(os.path.dirname(__file__)+"/icons/cil-arrow-circle-top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_shiftUp.setIcon(icon)
        self.pushButton_shiftUp.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_shiftUp)

        self.pushButton_shiftDown = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_shiftDown.setObjectName(u"pushButton_shiftDown")
        self.pushButton_shiftDown.setMinimumSize(QSize(35, 35))
        self.pushButton_shiftDown.setMaximumSize(QSize(35, 35))
        self.pushButton_shiftDown.setFont(font1)
        self.pushButton_shiftDown.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(os.path.dirname(__file__)+"/icons/cil-arrow-circle-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_shiftDown.setIcon(icon1)
        self.pushButton_shiftDown.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_shiftDown)

        self.pushButton_AddBookmark = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_AddBookmark.setObjectName(u"pushButton_AddBookmark")
        self.pushButton_AddBookmark.setMinimumSize(QSize(35, 35))
        self.pushButton_AddBookmark.setMaximumSize(QSize(35, 35))
        self.pushButton_AddBookmark.setFont(font1)
        self.pushButton_AddBookmark.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(os.path.dirname(__file__)+"/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_AddBookmark.setIcon(icon2)
        self.pushButton_AddBookmark.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_AddBookmark)

        self.pushButton_removeItem = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_removeItem.setObjectName(u"pushButton_removeItem")
        self.pushButton_removeItem.setMinimumSize(QSize(35, 35))
        self.pushButton_removeItem.setMaximumSize(QSize(35, 35))
        self.pushButton_removeItem.setFont(font1)
        self.pushButton_removeItem.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(os.path.dirname(__file__)+"/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_removeItem.setIcon(icon3)
        self.pushButton_removeItem.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_removeItem)

        self.pushButton_createFromBackdrops = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_createFromBackdrops.setObjectName(u"pushButton_createFromBackdrops")
        self.pushButton_createFromBackdrops.setMinimumSize(QSize(35, 35))
        self.pushButton_createFromBackdrops.setMaximumSize(QSize(35, 35))
        self.pushButton_createFromBackdrops.setFont(font1)
        self.pushButton_createFromBackdrops.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(os.path.dirname(__file__)+"/icons/cil-smile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_createFromBackdrops.setIcon(icon4)
        self.pushButton_createFromBackdrops.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_createFromBackdrops)

        self.pushButton_reset = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setMinimumSize(QSize(35, 35))
        self.pushButton_reset.setMaximumSize(QSize(35, 35))
        self.pushButton_reset.setFont(font1)
        self.pushButton_reset.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(os.path.dirname(__file__)+"/icons/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_reset.setIcon(icon5)
        self.pushButton_reset.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_reset)

        EditBookmarksWindowUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditBookmarksWindowUI)

        QMetaObject.connectSlotsByName(EditBookmarksWindowUI)
    # setupUi

    def retranslateUi(self, EditBookmarksWindowUI):
        EditBookmarksWindowUI.setWindowTitle(QCoreApplication.translate("EditBookmarksWindowUI", u"Km NodeGraph Easy Navigate : Edit Bookmarks", None))
        self.groupBox.setTitle(QCoreApplication.translate("EditBookmarksWindowUI", u"Bookmarks List", None))
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

        self.label_plugins_version.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"Km NodeGraph Easy Navigate v2.0", None))
        self.label_8.setText(QCoreApplication.translate("EditBookmarksWindowUI", u"By Hossein Karamian", None))
#if QT_CONFIG(tooltip)
        self.pushButton_shiftUp.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Change order (move up)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_shiftUp.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_shiftDown.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Change order (move down)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_shiftDown.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_AddBookmark.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Change order (move down)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_AddBookmark.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_removeItem.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Remove (Set Empty) Selected Bookmark", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_removeItem.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_createFromBackdrops.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Create Bookmarks From Backdrops", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_createFromBackdrops.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_reset.setToolTip(QCoreApplication.translate("EditBookmarksWindowUI", u"Remove (Set Empty) All Bookmarks", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_reset.setText("")
    # retranslateUi

