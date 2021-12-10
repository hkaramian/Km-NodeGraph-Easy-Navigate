"""Main controller"""

#
# Km NodeGraph Easy Navigate v2.0
#
# Developed By Hossein Karamian
# 
# www.kmworks.ir
# kmworks.call@gmail.com
#    _  __  __  __ 
#   | |/ / |  \/  |
#   | ' /  | \  / |
#   |  <   | |\/| |
#   |_|\_\ |_|  |_|
#


"""
Dev Notes : 
Logic and design : 
    - we save bookmarks data as nuke settings knobs. create a knob for each bookmark
    - a bookmark data is a json(python dict) that we store it as a single string in knob value. 
    - knob name is based on this fermula : "KM_NGJ_NN_"+bookmarkNodeName  | Example : "KM_NGJ_NN_Write2" , "KM_NGJ_NN_Backdrop3"
    - for getting a bookmark data , we get the value of the knob and pars the string and convert it to dict using json function (json.loads(bookmarkDataString))

GUI : 
using pyside2 library & nuke python panels
panels(windows) : 
    - Pyside2 | Main (including bookmarks & main menu buttons(templates,settings,edit bookmarks))
    - Pyside2 | Settings
    - Pyside2 | Templates
    - Pyside2 | Edit Bookmarks
    - Nuke Python Panel : Add New Bookmark

Data managment : 
    - all of things about getting and saving data happens in model.py 
    - we store plugin setting data in settings.json file
    - as said above , save bookmark data as nuke settings knobs
    - store each template as a seperate file in "templates" directory
    - Bookmark data structur : {"nodeName": "", "title": "", "index": "", "shortcut": ""}
    - Settings data structur : {
                                    "zoomEffect": "Disable",
                                    "shakeEffect": "Enable",
                                    "mainWindowFadeInEffect": "Enable",
                                    "shortcut": "shift+e",
                                    "nodeGraphZoomScale": "1.2",
                                    "templateGlobalOverride": "Disable",
                                    "templateNameForGlobalOverride": "Template1",
                                    "bookmarksGridColumns": "3",
                                    "bookmarksGridRows": "3",
                                }
    - Template file structur : {
                                    name : "templateName",
                                    filename : "fileName"
                                    bookmarks : {
                                        1: {"nodeName": "", "title": "", "index": "", "shortcut": ""},
                                        2: {"nodeName": "", "title": "", "index": "", "shortcut": ""},
                                        3: {"nodeName": "", "title": "", "index": "", "shortcut": ""},
                                        4: {"nodeName": "", "title": "", "index": "", "shortcut": ""},
                                        5: {"nodeName": "", "title": "", "index": "", "shortcut": ""},
                                        .
                                        .
                                        .
                                    }
                                }

"""


# Import Nuke Libraries
from re import template
import nuke  
import nukescripts

# Import built-in Libraries
import math
import os
import threading
import time
import subprocess
import datetime
import json

# Pyside Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer
from PysideImport import *

# Import local libs
import model
from Ui_Settings import Ui_SettingsWindowUI
from constants import BOOKMARK_KNOB_PREFIX

class MainWindow(QWidget):
    """Main Navigation Window, Includes Bookmark buttons"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.settings = model.Settings().Load()

        bookmarksGridColumns = int(self.settings["bookmarksGridColumns"])# defualt : 3*3
        bookmarksGridRows = int(self.settings["bookmarksGridRows"]) # defualt : 3*3
        boomarkButtonWidth= int(self.settings["bookmarksButtonWidth"]) # defualt : 110, 50
        bookmarkButtonHeight = int(self.settings["bookmarksButtonHeight"]) # defualt : 110, 50
        numberOfBoomarks = bookmarksGridColumns * bookmarksGridRows

        bookmarkButtonsMargin = 70 # extera Space For Bookmark Buttons Margin
        menuBarHeight = 30 # menu bar icons under bookmarks (settings , template, edit )
        width = bookmarksGridColumns * boomarkButtonWidth + bookmarkButtonsMargin # standard value : 400 for 3*3
        height = bookmarksGridRows * bookmarkButtonHeight + bookmarkButtonsMargin  # standard value : 250 for 3*3
        
        self.setFixedSize(width, height + menuBarHeight)
        #QDesktopWidget().screenGeometry(-1).width()
        #screenHeight = QDesktopWidget().screenGeometry(-1).height()
        #QCursor.pos().x()
        offset = QPoint(width * 0.5, height * 1 + 30)
        self.move(QCursor.pos() - offset)
        self.setContentsMargins(0,0,0,0)

        # create main layout
        mainVerticalLayout = QVBoxLayout(self)
        mainVerticalLayout.setContentsMargins(0, 0, 0, 0)

        # Boomarks Buttons Layout
        bookmarksLayoutWidget = QWidget()
        bookmarksLayoutWidget.setContentsMargins(0,0,0,0)
        bookmarksLayoutWidget.setMinimumSize(QSize(width, height))
        bookmarksLayoutWidget.setMaximumSize(QSize(width, height))
        bookmarksLayout = QGridLayout(bookmarksLayoutWidget)
        bookmarksLayout.setContentsMargins(0,0,0,0)
        columnCounter, rowCounter = 0, 0

        allBookmarksData = model.Bookmarks.Load()
        # Template Global Override 
        if self.settings["templateGlobalOverride"] == "Enable" :
            templateFileName = self.settings["globalOverrideTemplateFileName"]
            if model.BookmarkTemplates.GetATemplateData(templateFileName) :
                allBookmarksData = model.BookmarkTemplates.GetATemplateData(templateFileName)["bookmarks"].values()

        for index in range(0, numberOfBoomarks):
            isEmpty = True
            for bookmarkData in allBookmarksData :
                if int(bookmarkData["index"]) == index:
                    isEmpty = False
                    bookmarkButtonInstance = BookmarkButton(bookmarkData,self,boomarkButtonWidth,bookmarkButtonHeight)
                    bookmarksLayout.addWidget(bookmarkButtonInstance, rowCounter, columnCounter)
            # Create Empty Bookmark Button
            if isEmpty:
                bookmarkData = {"nodeName": "empty","title": "", "index": index, "shortcut" : ""}
                bookmarkButtonInstance = BookmarkButton(bookmarkData,self,boomarkButtonWidth,bookmarkButtonHeight)
                bookmarksLayout.addWidget(bookmarkButtonInstance, rowCounter, columnCounter)
            #print "row : " + str(row_counter)
            #print "column : "+str(column_counter)
            if columnCounter > (bookmarksGridColumns - 2) :
                rowCounter += 1
                columnCounter = 0
            else:
                columnCounter += 1

        # Menu Buttons layout
        menuButtonsLayoutWidget = MainMenuWidget()
        menuButtonsLayoutWidget.setMinimumHeight(40)
        menuButtonsLayoutWidget.setMaximumHeight(40)

        # add bookmarks layout and main menu layout to main layout
        mainVerticalLayout.setSpacing(0)
        mainVerticalLayout.addWidget(bookmarksLayoutWidget)
        mainVerticalLayout.addWidget(menuButtonsLayoutWidget)
        
        # set main layout
        self.setLayout(mainVerticalLayout)

        # Opacity(Fade In) Effect
        finalOpacity = 0.9
        self.SetWindowProperties()
        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(0)
        self.setGraphicsEffect(self.effect)
        self.fade = QPropertyAnimation(self.effect, 'opacity'.encode())  # encode is utf-8 by default      
        self.fade.setDuration(300)
        self.fade.setStartValue(0)
        self.fade.setEndValue(finalOpacity)
        self.fade.start()

    def SetWindowProperties(self):
        """Set window falgs and focused widget."""
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.Tool)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # make sure the widgets closes when it loses focus
        self.installEventFilter(self)
        #self.input.setFocus()

    def keyPressEvent(self, event):  # pylint: disable=invalid-name
        """Route key press event to certain behaviors.

        Args:
            event (QEvent): PySide key press event.

        """
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Alt:
            self.close()

        self.close()

    def eventFilter(self, object, event):
        if event.type() in [QEvent.WindowDeactivate, QEvent.FocusOut]:
            self.close()
            return True
        return False



class BookmarkButton(QLabel):
    """Bookmark Button in main navigation window \n
    nodeName : NodeName or set "empty" if it's not an assigned \n
    index : order & position in bookmarks ==> values :  integer number(0,1,2,..) """
    def __init__(self, bookmarkData,parrent,width=70,height=70):
        super(BookmarkButton, self).__init__()
        self.myParrent = parrent
        self.index = bookmarkData["index"]
        self.nodeName = bookmarkData["nodeName"]
        self.bookmarkData = bookmarkData
        
        self.mainPosX = 0
        self.mainPosY = 0
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking(True)
        #width , height = 70 , 70
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setStyleSheet("""background:gray; border-radius: 10px;
                            color:white ; border:2px red ; font-size:12px;""")
        self.setText(bookmarkData["title"])
        self.setWordWrap(True)


    def enterEvent(self, event): 
        self.setStyleSheet("""background:orange; border-radius: 10px;
                            color:white ;font-size:12px;""")

    def leaveEvent(self, event):  
        self.setStyleSheet("""background:gray; border-radius: 10px;
                            color:white;font-size:12px;""")
      
    def JumpToTargetAndShakeNode(self,targetNodeName):
        #Jump :
        TargetNode = nuke.toNode(targetNodeName)
        xC = TargetNode.xpos() + TargetNode.screenWidth()/2
        yC = TargetNode.ypos() + TargetNode.screenHeight()/2
        nuke.zoom( 1, [ xC, yC ])
        #Shake :
        moveValue = 5  
        for i in range( 0, 8 ):
            moveValue = moveValue * -1
            TargetNode.setXpos(int(TargetNode["xpos"].getValue())+ moveValue)
            time.sleep( 0.05 )
            #print move_value
            #print(datetime.datetime.now())

    def JumpToTargetWithZoomEffect(self,targetNodeName):
        TargetNode = nuke.toNode(targetNodeName)
        zoom = 0.1  
        for i in range( 0, 200 ):
            time.sleep( 0.0001 )
            #print(datetime.datetime.now())
            xC = TargetNode.xpos() + TargetNode.screenWidth()/2
            yC = TargetNode.ypos() + TargetNode.screenHeight()/2
            zoom = zoom + 0.05
            if zoom > 1:
                break
            nuke.zoom( zoom, [ xC, yC ])

    def JumpToTargetWithoutEffect(self,targetNodeName):
        TargetNode = nuke.toNode(targetNodeName)
        xC = TargetNode.xpos() + TargetNode.screenWidth()/2
        yC = TargetNode.ypos() + TargetNode.screenHeight()/2
        nuke.zoom( 1, [ xC, yC ])

    def mousePressEvent(self, event):
        navigationEffect = "JumpAndShake"
        navigationEffect = "ZoomIn"
        if event.buttons() == Qt.LeftButton:
            # define new bookmark if this button is empty
            if self.nodeName == "empty" :  
                if nuke.selectedNodes() == [] :
                    nuke.message("First select a node to define new bookmark")
                else:                    
                    ### find selected node
                    selectedNode = nuke.selectedNode() 
                    for boomarkNodeName in nuke.selectedNodes() : 
                        selectedNode = boomarkNodeName

                    bookmarkKnobName = BOOKMARK_KNOB_PREFIX + selectedNode['name'].getValue()
                    if not nuke.root().knob(bookmarkKnobName):
                        newBookMarkWindowInstance = NewBookMarkWindow("empty","add",self.index)
                        newBookMarkWindowInstance.setMinimumSize(300, 50)
                        if newBookMarkWindowInstance.showModalDialog() :
                            bookmarkNodeName = newBookMarkWindowInstance.NodeName.getValue()
                            bookmarkTitle = newBookMarkWindowInstance.Title.getValue()
                            bookmarkIndex = int(newBookMarkWindowInstance.Index.getValue())
                            bookmarkShortcut = newBookMarkWindowInstance.Shortcut.getValue()
                            model.Bookmarks.AddNewBookmark(bookmarkNodeName,bookmarkTitle,bookmarkIndex,bookmarkShortcut)
                    else :
                        nuke.message("Selected node exists in the list, you can delete or edite that")
            # jump to bookmark
            else :
                if self.myParrent.settings["zoomEffect"] == "Enable":
                    threading.Thread( target=self.JumpToTargetWithZoomEffect, args=(self.nodeName,)).start()
                else:
                    self.JumpToTargetWithoutEffect(self.nodeName)

                if self.myParrent.settings["shakeEffect"] == "Enable":
                    threading.Thread( target=self.JumpToTargetAndShakeNode, args=(self.nodeName,)).start()
             
        if event.buttons() == Qt.RightButton:
            if self.nodeName != "empty":
                if nuke.ask("Remove "+self.bookmarkData["title"]+" Bookmark ?"):
                    model.Bookmarks.removeABookmark(self.nodeName)

        if event.buttons() == Qt.MiddleButton:
            if self.nodeName != "empty" :
                newBookMarkWindowInstance = NewBookMarkWindow(self.nodeName,"edit",0)
                newBookMarkWindowInstance.setMinimumSize(300, 50)
                if newBookMarkWindowInstance.showModalDialog() :
                    index = int(newBookMarkWindowInstance.Index.getValue())
                    title = newBookMarkWindowInstance.Title.getValue()
                    shortcut = newBookMarkWindowInstance.Shortcut.getValue()
                    bookmarkData = {"nodeName": self.nodeName,"title": title, "index": index, "shortcut" : shortcut}
                    model.Bookmarks.UpdateBookmarkData(bookmarkData)

        self.myParrent.close()





class MainMenuWidget(QWidget):
    """Main """

    def __init__(self):
        super(MainMenuWidget, self).__init__()

        self.menuButtonsLayout = QHBoxLayout(self)
        self.menuButtonsLayout.setSpacing(6)
        self.menuButtonsLayout.setObjectName(u"horizontalLayout_2")
        self.menuButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.menuButtonsLayout.addItem(self.horizontalSpacer_4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.pushButton_Templates = QPushButton(self)
        self.pushButton_Templates.setObjectName(u"pushButton_close_5")
        self.pushButton_Templates.setMinimumSize(QSize(23, 23))
        self.pushButton_Templates.setMaximumSize(QSize(23, 23))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        self.pushButton_Templates.setFont(font)
        self.pushButton_Templates.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(128, 146, 177);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(128, 146, 177);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(97, 110, 134);\n"
"	border: 2px solid rgb(97, 110, 134);\n"
"}")
        icon = QIcon()
        icon.addFile(os.path.dirname(__file__)+"/icons/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Templates.setIcon(icon)
        self.pushButton_Templates.setIconSize(QSize(16, 16))
        self.pushButton_settings = QPushButton(self)
        self.pushButton_settings.setObjectName(u"pushButton_close_4")
        self.pushButton_settings.setMinimumSize(QSize(23, 23))
        self.pushButton_settings.setMaximumSize(QSize(23, 23))
        self.pushButton_settings.setBaseSize(QSize(0, 0))
        self.pushButton_settings.setFont(font)
        self.pushButton_settings.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(128, 146, 177);\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(128, 146, 177);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(97, 110, 134);\n"
"	border: 2px solid rgb(97, 110, 134);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(os.path.dirname(__file__)+"/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_settings.setIcon(icon1)
        self.pushButton_settings.setIconSize(QSize(16, 16))
        self.pushButton_EditBookmarks = QPushButton(self)
        self.pushButton_EditBookmarks.setObjectName(u"pushButton_close_3")
        self.pushButton_EditBookmarks.setMinimumSize(QSize(28, 28))
        self.pushButton_EditBookmarks.setMaximumSize(QSize(28, 28))
        self.pushButton_EditBookmarks.setFont(font)
        self.pushButton_EditBookmarks.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(128, 146, 177);\n"
"	border-radius: 12px;	\n"
"	background-color: rgb(128, 146, 177);\n"
"	color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(97, 110, 134);\n"
"	border: 2px solid rgb(97, 110, 134);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(os.path.dirname(__file__)+"/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_EditBookmarks.setIcon(icon2)
        self.pushButton_EditBookmarks.setIconSize(QSize(20, 20))
        self.horizontalLayout_3.addWidget(self.pushButton_Templates)
        self.horizontalLayout_3.addWidget(self.pushButton_EditBookmarks)
        self.horizontalLayout_3.addWidget(self.pushButton_settings)
        self.menuButtonsLayout.addLayout(self.horizontalLayout_3)
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.menuButtonsLayout.addItem(self.horizontalSpacer_5)
        self.menuButtonsLayout.setStretch(0, 30)
        self.menuButtonsLayout.setStretch(2, 30)

        # main menu buttons click event | Setting Signals
        self.pushButton_settings.clicked.connect(self.OpenSettingsWindow)
        self.pushButton_Templates.clicked.connect(self.OpenTemplatesWindow)
        self.pushButton_EditBookmarks.clicked.connect(self.OpenEditBookmarksWindow)


    def OpenSettingsWindow(self) : 
        global settingsWindowInstance
        settingsWindowInstance = SettingsWindow()
        settingsWindowInstance.show()
        
    def OpenTemplatesWindow(self) : 
        self.templatesWindowInstance = TemplatesWindow()
        self.templatesWindowInstance.show()

    def OpenEditBookmarksWindow(self) : 
        self.editBookmarksInstance = EditBookmarks()
        self.editBookmarksInstance.show()



class NewBookMarkWindow(nukescripts.PythonPanel):
    """window for add new bookmark"""
    def __init__(self,nodeName,type,index):
        nukescripts.PythonPanel.__init__(self, 'Define New Bookmark')
        if type == "add":
            ### find selected node
            selectedNode = nuke.selectedNode() 
            for node in nuke.selectedNodes() : 
                selectedNode = node

            # define input knobs
            self.NodeName = nuke.EvalString_Knob("NodeName", "Node Name")
            self.Title = nuke.EvalString_Knob("BookMarkTitle", "BookMark Title")
            self.Index = nuke.Int_Knob("Index", "Index")
            self.Shortcut = nuke.EvalString_Knob("BookMarkShortcut", "BookMark Shortcut")

            # get node lable value for title
            selectedNodeLable = nuke.toNode(selectedNode['name'].getValue())["label"].getValue()
            if selectedNodeLable != "":
                title = selectedNodeLable
            else:
                title = selectedNode['name'].getValue()

            self.Title.setValue(title)
            self.NodeName.setValue(selectedNode['name'].getValue())
            self.NodeName.setEnabled(False)
            self.Index.setEnabled(False)
            self.Index.setValue(index)
            self.addKnob(self.Title)
            self.addKnob(self.NodeName)
            self.addKnob(self.Index)
            self.addKnob(self.Shortcut)
            self.setMinimumSize(500,500)

        if type == "edit":
            # define input knobs
            self.NodeName = nuke.EvalString_Knob("NodeName", "Node Name")
            self.Title = nuke.EvalString_Knob("BookMarkTitle", "BookMark Title")
            self.Index = nuke.Int_Knob("Index", "Index")
            self.Shortcut = nuke.EvalString_Knob("BookMarkShortcut", "BookMark Shortcut")

            bookmarkData = model.Bookmarks.getBookmarkData(nodeName)
            self.Title.setValue(bookmarkData["title"])
            self.NodeName.setValue(nodeName)
            self.NodeName.setEnabled(False)
            self.Index.setEnabled(False)
            self.Index.setValue(int(bookmarkData["index"]))
            self.Shortcut.setValue(bookmarkData["shortcut"])

            self.addKnob(self.Title)
            self.addKnob(self.NodeName)
            self.addKnob(self.Index)
            self.addKnob(self.Shortcut)
            self.setMinimumSize(500,500)




class SettingsWindow(QMainWindow,Ui_SettingsWindowUI):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)
        self.settings = model.Settings().Load()
        # Setup UI
        self.horizontalSlider_ZoomScale.setMinimum(5) 
        self.horizontalSlider_ZoomScale.setMaximum(30)
        self.horizontalSlider_ZoomScale.setSingleStep(1)
        self.horizontalSlider_ZoomScale.valueChanged.connect(self.SliderLabelUpdate)
        self.label_credit.setText('''<a href='http://www.kmworks.ir' style='color: rgb(200, 200, 200);text-decoration: none;'>By Hossein Karamian</a>''')
        self.label_credit.setOpenExternalLinks(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # Signals
        self.pushButton_save.clicked.connect(self.applySettings)
        self.pushButton_setDefault.clicked.connect(self.SetDefault)
        self.pushButton_OpenPDF.clicked.connect(self.open_documentation)

        
        self.updateUI()

    def updateUI(self):

        if self.settings["shakeEffect"] == "Enable" :
            self.checkBox_shake_effect.setChecked(True)
        else :
            self.checkBox_shake_effect.setChecked(False)

        if self.settings["zoomEffect"] == "Enable" :
            self.checkBox_zoom_effect.setChecked(True)
        else :
            self.checkBox_zoom_effect.setChecked(False)

        if self.settings["mainWindowFadeInEffect"] == "Enable" :
            self.checkBox_fade_effect.setChecked(True)
        else :
            self.checkBox_fade_effect.setChecked(False)
  
        self.horizontalSlider_ZoomScale.setValue(float(self.settings["nodeGraphZoomScale"]) * 10.0)
        self.SliderLabelUpdate()
        self.lineEdit_shortcut.setText(self.settings["shortcut"])
        self.lineEdit_columnn.setText(self.settings["bookmarksGridColumns"])
        self.lineEdit_Rows.setText(self.settings["bookmarksGridRows"])
        self.lineEdit_Button_width.setText(self.settings["bookmarksButtonWidth"])
        self.lineEdit_ButtonHeight.setText(self.settings["bookmarksButtonHeight"])

    def SliderLabelUpdate(self):
        zoomScale = self.horizontalSlider_ZoomScale.value() / 10.0
        self.label_ZoomScale.setText(str(zoomScale))

    def applySettings(self): 
        if self.checkBox_shake_effect.isChecked():
            self.settings["shakeEffect"] = "Enable"
        else:
            self.settings["shakeEffect"] = "Disable"
        if self.checkBox_zoom_effect.isChecked():
            self.settings["zoomEffect"] = "Enable"
        else:
            self.settings["zoomEffect"] = "Disable"
        if self.checkBox_fade_effect.isChecked():
            self.settings["mainWindowFadeInEffect"] = "Enable"
        else:
            self.settings["mainWindowFadeInEffect"] = "Disable"
        self.settings["shortcut"] = self.lineEdit_shortcut.text() 
        self.settings["nodeGraphZoomScale"] = self.label_ZoomScale.text()
        self.settings["bookmarksGridColumns"] = self.lineEdit_columnn.text()
        self.settings["bookmarksGridRows"] = self.lineEdit_Rows.text()
        self.settings["bookmarksButtonWidth"] = self.lineEdit_Button_width.text()
        self.settings["bookmarksButtonHeight"] = self.lineEdit_ButtonHeight.text()

        model.Settings().Save(self.settings)
        menu = nuke.menu("Nuke")
        Km_NGJ = menu.addMenu("KmTools")
        Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraph_Easy_Navigate.start()",self.settings["shortcut"])
        self.close()

    def SetDefault(self) : 
        self.settings["shakeEffect"] = "Disable"
        self.settings["zoomEffect"] = "Disable"
        self.settings["mainWindowFadeInEffect"] = "Enable"
        self.settings["shortcut"] = "shift+e"
        self.settings["nodeGraphZoomScale"] = "1"
        self.settings["bookmarksGridColumns"] = "3"
        self.settings["bookmarksGridRows"] = "3"
        self.settings["bookmarksButtonWidth"] = "110"
        self.settings["bookmarksButtonHeight"] = "50"

        model.Settings().Save(self.settings)
        menu = nuke.menu("Nuke")
        Km_NGJ = menu.addMenu("KmTools")
        Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraph_Easy_Navigate.start()",self.settings["shortcut"])
        self.updateUI()

    def open_documentation(self):
        subprocess.Popen(os.path.dirname(__file__)+"/UserGuide.pdf",shell=True)



from Ui_Templates import Ui_TemplatesWindowUI

class TemplatesWindow(QMainWindow,Ui_TemplatesWindowUI):
    def __init__(self,parent=None):
        super(TemplatesWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint) # disable resize
        self.label_credit.setText('''<a href='http://www.kmworks.ir' style='color: rgb(200, 200, 200);text-decoration: none;'>By Hossein Karamian</a>''')
        self.label_credit.setOpenExternalLinks(True)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # UpdateUI
        self.UpdateUI()

        # Signals
        self.pushButton_remove.clicked.connect(self.removeTemplate)
        self.pushButton_load.clicked.connect(self.LoadTemplate)
        self.pushButton_add.clicked.connect(self.AddTemplate)
        self.comboBox_TemplateOverride.currentIndexChanged.connect(self.ComboBoxTemplateOverrideChange)
        self.checkBox_TemplateOverride.stateChanged['int'].connect(self.CheckBoxTemplateOverrideChange)

        self.listWidget_templateList.currentItemChanged.connect(self.selectedTemplateItemsListUpdateUI)

    def UpdateUI(self) :
        self.settings = model.Settings().Load()
        currentProjectBookmarks = model.Bookmarks.Load()
        self.templatesList = model.BookmarkTemplates.Load()

        # clear widgets
        self.listWidget_templateItems.clear() 
        self.listWidget_newTemplateItems.clear() # clear list widget
        self.listWidget_templateList.clear() # clear list widget
        self.comboBox_TemplateOverride.clear()

        # new Template Items listWidget 
        itemCounter = 0
        for bookmarkItem in currentProjectBookmarks : 
            QListWidgetItem(self.listWidget_newTemplateItems)
            self.listWidget_newTemplateItems.item(itemCounter).setText(bookmarkItem["title"])
            itemCounter += 1

        # templates list
        self.overrideTemplateIndex = -1 # if override template file not exits
        itemCounter = 0
        for templateItem in self.templatesList : 
            QListWidgetItem(self.listWidget_templateList)
            self.listWidget_templateList.item(itemCounter).setText(templateItem["templateName"])
            self.comboBox_TemplateOverride.addItem(templateItem["templateName"])
            if templateItem["fileName"] == self.settings["globalOverrideTemplateFileName"] : 
                self.overrideTemplateIndex = itemCounter
            itemCounter += 1
  
        if self.overrideTemplateIndex != -1 :
            self.comboBox_TemplateOverride.setCurrentIndex(self.overrideTemplateIndex)

        if self.settings["templateGlobalOverride"] == "Enable" :
            self.checkBox_TemplateOverride.setChecked(True)
            self.comboBox_TemplateOverride.setEnabled(True)
        else :
            self.checkBox_TemplateOverride.setChecked(False)
            self.comboBox_TemplateOverride.setEnabled(False)


        
        
    def CheckBoxTemplateOverrideChange(self):
        if self.checkBox_TemplateOverride.isChecked():
            self.comboBox_TemplateOverride.setEnabled(True)
            self.settings["templateGlobalOverride"] = "Enable"
        else : 
            self.comboBox_TemplateOverride.setEnabled(False)
            self.settings["templateGlobalOverride"] = "Disable"
        if self.comboBox_TemplateOverride.count != 0 :
            currentIndex = self.comboBox_TemplateOverride.currentIndex()
            self.settings["globalOverrideTemplateFileName"] = self.templatesList[currentIndex]["fileName"]
        model.Settings.Save(self.settings)

    def ComboBoxTemplateOverrideChange(self):
        currentIndex = self.comboBox_TemplateOverride.currentIndex()
        self.settings["globalOverrideTemplateFileName"] = self.templatesList[currentIndex]["fileName"]
        model.Settings.Save(self.settings)       
        
    def selectedTemplateItemsListUpdateUI(self):
        self.listWidget_templateItems.clear() 
        self.templatesList = model.BookmarkTemplates.Load()
        selectedTemplateIndex = self.listWidget_templateList.currentRow()
        selectedTemplate = self.templatesList[selectedTemplateIndex]
        itemCounter = 0
        for bookmarkItem in selectedTemplate["bookmarks"].values() : 
            QListWidgetItem(self.listWidget_templateItems)
            self.listWidget_templateItems.item(itemCounter).setText(bookmarkItem["title"])
            itemCounter += 1
    
    def removeTemplate(self):
        self.templatesList = model.BookmarkTemplates.Load()
        if self.templatesList == [] : return True
        selectedTemplateIndex = self.listWidget_templateList.currentRow()
        selectedTemplate = self.templatesList[selectedTemplateIndex]
        model.BookmarkTemplates.DeleteTemplateFile(selectedTemplate["fileName"])
        self.UpdateUI()
    
    def LoadTemplate(self) : 
        self.templatesList = model.BookmarkTemplates.Load()
        if self.templatesList == [] : return True
        selectedTemplateIndex = self.listWidget_templateList.currentRow()
        selectedTemplate = self.templatesList[selectedTemplateIndex]
        #self.setWindowState(Qt.WindowState.WindowNoState)
        if nuke.ask("Load \""+selectedTemplate["templateName"]+"\" Bookmark Template ? \n(current bookmarks will removed and replace with this template)"):
            model.Bookmarks.ResetBookmarks() # remove current bookmarks in this project
            for bookmarkItem in selectedTemplate["bookmarks"].values() :  
                model.Bookmarks.AddNewBookmark(bookmarkItem["nodeName"],bookmarkItem["title"],bookmarkItem["index"],bookmarkItem["shortcut"]) 
            #self.show() #setWindowState(Qt::WindowState::WindowActive); // Bring window to foreground
            #self.setWindowState(Qt.WindowState.WindowActive) # bring back window to front
            self.raise_()
            self.UpdateUI()
            self.listWidget_templateList.setCurrentRow(selectedTemplateIndex)

    def AddTemplate(self) :
        templateName = self.lineEdit_templateName.text()
        if (templateName != "" and templateName != " "):
            model.BookmarkTemplates.AddNew(templateName)
            self.UpdateUI()
            self.label_4.setStyleSheet("color: rgb(255, 255, 255)")
            templateName = self.lineEdit_templateName.setText("")           
        else :
            self.label_4.setStyleSheet("color: rgb(255, 20, 20)")





from Ui_EditBookmarks import Ui_EditBookmarksWindowUI

class EditBookmarks(QMainWindow,Ui_EditBookmarksWindowUI):
    def __init__(self,parent=None):
        super(EditBookmarks, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # UpdateUI
        self.UpdateUI()

        self.pushButton_reset.clicked.connect(self.resetBookmarks)
        self.pushButton_removeItem.clicked.connect(self.removeABookmark)
        self.pushButton_shiftUp.clicked.connect(self.ShiftUpBookmark)
        self.pushButton_shiftDown.clicked.connect(self.ShiftDownBookmark)
        self.pushButton_createFromBackdrops.clicked.connect(self.createBookmarksFromBackdrops)
        self.pushButton_AddBookmark.clicked.connect(self.AddNewBookmark)

        #self.listWidget_templateList.currentItemChanged.connect(self.selectedTemplateItemsListUpdateUI) 


    def AddNewBookmark(self):
        if nuke.selectedNodes() == [] :
            # self.msg=QMessageBox()
            # self.msg.setIcon(QMessageBox.Information)
            # self.msg.setText("This is Message")
            # self.msg.setInformativeText("Are You Sure?")
            # self.msg.show()
            # self.msg.raise_()
            # self.msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            return True

        selectedRow = self.tableWidget_BookmarksList.currentRow()
        nodeNameColumn = self.tableWidget_BookmarksList.item(selectedRow,1).text()
        if nodeNameColumn != " - "  : # check if not empty remove older bookmarks
            model.Bookmarks.removeABookmark(nodeNameColumn)          
        ### find selected node
        selectedNode = nuke.selectedNode() 
        for node in nuke.selectedNodes() : 
            selectedNode = node
        bookmarkKnobName = BOOKMARK_KNOB_PREFIX + selectedNode['name'].getValue()
        if not nuke.root().knob(bookmarkKnobName):
            bookmarkNodeName = selectedNode['name'].getValue()
            bookmarkTitle = selectedNode['label'].getValue()
            if (bookmarkTitle == "" or bookmarkTitle == " ") :
                bookmarkTitle = bookmarkNodeName
            bookmarkIndex = selectedRow
            bookmarkShortcut = ""
            model.Bookmarks.AddNewBookmark(bookmarkNodeName,bookmarkTitle,bookmarkIndex,bookmarkShortcut)
            self.UpdateUI()
        else :
            nuke.message("Selected node exists in the list, you can delete or edite that")
        self.raise_()

    def createBookmarksFromBackdrops(self):
        if nuke.ask("Create Bookmarks from backdrops ? \nAll the bookmarks in this project will removed"):
            model.Bookmarks.ResetBookmarks()
            allBackdrops = nuke.allNodes("BackdropNode")
            counter = 0
            for backdropNode in allBackdrops : 
                bookmarkNodeName = backdropNode['name'].getValue()
                bookmarkTitle = backdropNode['label'].getValue()
                if (bookmarkTitle == "" or bookmarkTitle == " ") :
                    bookmarkTitle = bookmarkNodeName
                bookmarkIndex = counter
                bookmarkShortcut = ""
                model.Bookmarks.AddNewBookmark(bookmarkNodeName,bookmarkTitle,bookmarkIndex,bookmarkShortcut)
                counter += 1
            self.UpdateUI()
            self.raise_()

    def removeABookmark(self) : 
        selectedRow = self.tableWidget_BookmarksList.currentRow()
        nodeName = self.tableWidget_BookmarksList.item(selectedRow,1).text()
        model.Bookmarks.removeABookmark(nodeName)
        self.UpdateUI()

    def ShiftUpBookmark(self):
        selectedIndex = self.tableWidget_BookmarksList.currentRow()
        if selectedIndex < 1 : return True # check if it's first row
        if self.tableWidget_BookmarksList.item(selectedIndex,1).text() == " - " : return True # check if selected row is a empty bookmark

        row = selectedIndex
        SelectedRowItems = [self.tableWidget_BookmarksList.item(row,0).text(),self.tableWidget_BookmarksList.item(row,1).text(),self.tableWidget_BookmarksList.item(row,2).text(),self.tableWidget_BookmarksList.item(row,3).text()]
        row = selectedIndex - 1 # up row
        UpRowItems = [self.tableWidget_BookmarksList.item(row,0).text(),self.tableWidget_BookmarksList.item(row,1).text(),self.tableWidget_BookmarksList.item(row,2).text(),self.tableWidget_BookmarksList.item(row,3).text()]
        if UpRowItems[1] != " - "  : # check if empty bookmark .   UpRowItems[1] => nodeName
            model.Bookmarks.removeABookmark(UpRowItems[1]) # remove
            model.Bookmarks.AddNewBookmark(UpRowItems[1],UpRowItems[2],selectedIndex,UpRowItems[3]) # copy up row to selected row
        
        model.Bookmarks.removeABookmark(SelectedRowItems[1]) # remove
        model.Bookmarks.AddNewBookmark(SelectedRowItems[1],SelectedRowItems[2],selectedIndex-1,SelectedRowItems[3]) # copy selected row to up row
        currentColumn = self.tableWidget_BookmarksList.currentColumn()
        self.tableWidget_BookmarksList.setCurrentCell(selectedIndex-1,currentColumn) # shift up selected cell
        self.UpdateUI()

    def ShiftDownBookmark(self):
        selectedIndex = self.tableWidget_BookmarksList.currentRow()
        if selectedIndex >= model.Bookmarks.getTotalBookmarksCount()-1 : return True # check if it's last row
        if self.tableWidget_BookmarksList.item(selectedIndex,1).text() == " - " : return True # check if selected row is a empty bookmark

        row = selectedIndex
        SelectedRowItems = [self.tableWidget_BookmarksList.item(row,0).text(),self.tableWidget_BookmarksList.item(row,1).text(),self.tableWidget_BookmarksList.item(row,2).text(),self.tableWidget_BookmarksList.item(row,3).text()]
        row = selectedIndex + 1 # down row
        DownRowItems = [self.tableWidget_BookmarksList.item(row,0).text(),self.tableWidget_BookmarksList.item(row,1).text(),self.tableWidget_BookmarksList.item(row,2).text(),self.tableWidget_BookmarksList.item(row,3).text()]
        if DownRowItems[1] != " - "  : # check if empty bookmark
            model.Bookmarks.removeABookmark(DownRowItems[1]) # remove
            model.Bookmarks.AddNewBookmark(DownRowItems[1],DownRowItems[2],selectedIndex,DownRowItems[3]) # copy down row to selected row
        
        model.Bookmarks.removeABookmark(SelectedRowItems[1]) # remove
        model.Bookmarks.AddNewBookmark(SelectedRowItems[1],SelectedRowItems[2],selectedIndex + 1,SelectedRowItems[3]) # copy selected row to down row
        currentColumn = self.tableWidget_BookmarksList.currentColumn()
        self.tableWidget_BookmarksList.setCurrentCell(selectedIndex + 1,currentColumn) # shift down selected cell 
        self.UpdateUI()
        
        
    def resetBookmarks(self):
        if nuke.ask("Remove all bookmarks in the current project ? "):
            model.Bookmarks.ResetBookmarks()
            self.UpdateUI()
        self.raise_()

    def UpdateUI(self) :
        #self.tableWidget_BookmarksList.clear()

        # new Template Items listWidget 
        currentProjectBookmarks = model.Bookmarks.Load()
        settings = model.Settings.Load()
        numberOfBookmarks = int(settings["bookmarksGridColumns"]) * int(settings["bookmarksGridRows"])

        self.tableWidget_BookmarksList.setRowCount(numberOfBookmarks)
        self.tableWidget_BookmarksList.setColumnWidth(0,70)
        self.tableWidget_BookmarksList.setColumnWidth(1,180)
        self.tableWidget_BookmarksList.setColumnWidth(2,180)
        self.tableWidget_BookmarksList.setColumnWidth(3,80)
        self.tableWidget_BookmarksList.horizontalHeaderItem(0).setText("Index \n(Order)")
        for index in range(numberOfBookmarks):
            nodeName = " - "
            title = " - "
            shortcut = " - "
            isEmpty = True
            # find if any bookmark exits for this index
            for bookmarkData in currentProjectBookmarks :
                if int(bookmarkData["index"]) == index:
                    isEmpty = False
                    nodeName = bookmarkData["nodeName"]
                    title = bookmarkData["title"]
                    shortcut = bookmarkData["shortcut"]

            item = self.CreateWidgetItemAndSetFlags(str(index),True)
            self.tableWidget_BookmarksList.setItem(index,0,item) # index column
            item = self.CreateWidgetItemAndSetFlags(nodeName,True)
            self.tableWidget_BookmarksList.setItem(index,1,item) # nodeName column
            item = self.CreateWidgetItemAndSetFlags(title,isEmpty)
            self.tableWidget_BookmarksList.setItem(index,2,item) # title column
            item = self.CreateWidgetItemAndSetFlags(shortcut,isEmpty)
            self.tableWidget_BookmarksList.setItem(index,3,item) # shortcut column

    def CreateWidgetItemAndSetFlags(self,text,IsDisable=False) :
        widgetItem = QTableWidgetItem()
        if IsDisable : widgetItem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
        widgetItem.setText(text)
        widgetItem.setTextAlignment(Qt.AlignCenter)
        return widgetItem


            
 ################################################################################
## ui_  .py changes needed for new version from qt designer : 
## add import os 
## Replace  : 
## u"../Km_NodeGraphEN/icons
## os.path.dirname(__file__)+"/icons


def showSettings():
    global settingsWindowInstance
    settingsWindowInstance = SettingsWindow()
    settingsWindowInstance.show()

def start():
    """Start up function for MainWindow"""
    global mainWindowInstance  # pylint: disable=global-statement
    mainWindowInstance = MainWindow()
    mainWindowInstance.show()