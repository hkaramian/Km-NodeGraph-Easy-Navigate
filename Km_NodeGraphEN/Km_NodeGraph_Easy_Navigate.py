"""Main controller"""

#
# Km NodeGraph Easy Navigate v1.2
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


# Import Nuke Libraries
import nuke  
import nukescripts

# Import built-in Libraries
import math
import os
import threading
import time
import datetime
import json

# Pyside Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer
from PysideImport import *

# Import local libs
from Ui_Settings import Ui_Form
import model

class BookmarkButton(QLabel):
    """Bookmark Button in main navigation window \n
    id : type of bookmark ==> values : empty, nodeName, icon \n
    index : order & position in bookmarks ==> values :  integer number(0,1,2,..) """
    def __init__(self, id,parrent,index):
        super(BookmarkButton, self).__init__()
        self.myParrent = parrent
        self.index = index
        self.id = id
        
        self.mainPosX = 0
        self.mainPosY = 0
        self.nodeName = "node name"
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking(True)
        self.setFixedWidth(70)
        self.setFixedHeight(70)
        self.setStyleSheet("""background:gray;
                            color:white ; border:2px red ; font-size:14px;""")
        self.setText("Final Render")
        self.setWordWrap(True)

    def SetNodeName(self,nodeName):
        self.nodeName = nodeName

    def enterEvent(self, event): 
        self.setStyleSheet("""background:orange;
                            color:white ;font-size:18px;""")

    def leaveEvent(self, event):  
        self.setStyleSheet("""background:gray;
                            color:white;font-size:14px;""")
      
    def JumpToTargetAndShakeNode(self,TargetNode):
        #Jump :
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

    def JumpToTargetWithZoomEffect(self,TargetNode):
        zoom = 0.1  
        for i in range( 0, 200 ):
            time.sleep( 0.0001 )
            #print(datetime.datetime.now())
            node = TargetNode
            xC = node.xpos() + node.screenWidth()/2
            yC = node.ypos() + node.screenHeight()/2
            zoom = zoom + 0.05
            if zoom > 1:
                break
            nuke.zoom( zoom, [ xC, yC ])

    def JumpToTargetWithoutEffect(self,TargetNode):
        node = TargetNode
        xC = node.xpos() + node.screenWidth()/2
        yC = node.ypos() + node.screenHeight()/2
        nuke.zoom( 1, [ xC, yC ])

    def mousePressEvent(self, event):
        navigationEffect = "JumpAndShake"
        navigationEffect = "ZoomIn"
        if event.buttons() == Qt.LeftButton:
            if self.id == "icon" :
                global settingsWindowInstance
                settingsWindowInstance = SettingsWindow()
                settingsWindowInstance.show()
            if self.id == "empty" :
                if nuke.selectedNodes() == [] :
                    nuke.message("First select a node to define new Shortcut")
                else:                    
                    selected_node = nuke.selectedNode() 
                    if not nuke.root().knob("KM_NGJ_NN_"+selected_node['name'].getValue()):
                        newBookMarkWindowInstance = NewBookMarkWindow("empty","add",self.index)
                        newBookMarkWindowInstance.setMinimumSize(300, 50)
                        if newBookMarkWindowInstance.showModalDialog() :
                            if not nuke.root().knob("KM_NGJ_NN_"+newBookMarkWindowInstance.NodeName.getValue()):
                                #print (p.Title.getValue())
                                #print (p.NodeName.getValue())
                                #print (p.Index.getValue())
                                nuke.root().addKnob(nuke.EvalString_Knob("KM_NGJ_NN_"+newBookMarkWindowInstance.NodeName.getValue(), "Title"))
                                nuke.root().knob("KM_NGJ_NN_"+newBookMarkWindowInstance.NodeName.getValue()).setValue(newBookMarkWindowInstance.Title.getValue())
                                nuke.root().knob("KM_NGJ_NN_"+newBookMarkWindowInstance.NodeName.getValue()).setVisible(False)
                                nuke.root().addKnob(nuke.Int_Knob("KM_NGJ_Index_"+newBookMarkWindowInstance.NodeName.getValue(), "Title"))
                                nuke.root().knob("KM_NGJ_Index_"+newBookMarkWindowInstance.NodeName.getValue()).setValue(int(newBookMarkWindowInstance.Index.getValue()))
                                nuke.root().knob("KM_NGJ_Index_"+newBookMarkWindowInstance.NodeName.getValue()).setVisible(False)
                    else :
                        nuke.message("Selected node exists in the list, you can delete or edite that")
            if self.id != "empty" and self.id != "icon":
                node = nuke.toNode(self.id.replace('KM_NGJ_NN_', ''))

                nuke.root().knob("KM_NGJ_NN_"+node['name'].getValue())
                if self.myParrent.settings["zoomEffect"] == "Enable":
                    threading.Thread( target=self.JumpToTargetWithZoomEffect, args=(node,)).start()
                else:
                    self.JumpToTargetWithoutEffect(node)

                if self.myParrent.settings["shakeEffect"] == "Enable":
                    threading.Thread( target=self.JumpToTargetAndShakeNode, args=(node,)).start()
             
        if event.buttons() == Qt.RightButton:
            if self.id != "empty" and self.id != "icon":
                nodeName = self.id.replace('KM_NGJ_NN_', '')
                knobName1 = "KM_NGJ_NN_"+nodeName
                knobName2 = "KM_NGJ_Index_"+nodeName
                if nuke.ask("Remove "+nuke.root().knob("KM_NGJ_NN_"+self.id).getValue()+" Bookmark ?"):
                    nuke.root().removeKnob(nuke.root().knobs()[knobName1])
                    nuke.root().removeKnob(nuke.root().knobs()[knobName2])
                else :
                    pass

        if event.buttons() == Qt.MiddleButton:
            if self.id != "empty" and self.id != "icon":
                nodeName = self.id.replace('KM_NGJ_NN_', '')
                newBookMarkWindowInstance = NewBookMarkWindow(nodeName,"edit",0)
                newBookMarkWindowInstance.setMinimumSize(300, 50)
                if newBookMarkWindowInstance.showModalDialog() :
                    nuke.root().knob("KM_NGJ_NN_"+newBookMarkWindowInstance.NodeName.getValue()).setValue(newBookMarkWindowInstance.Title.getValue())
                    nuke.root().knob("KM_NGJ_NN_"+newBookMarkWindowInstance.NodeName.getValue()).setVisible(False)
                    nuke.root().knob("KM_NGJ_Index_"+newBookMarkWindowInstance.NodeName.getValue()).setValue(int(newBookMarkWindowInstance.Index.getValue()))
                    nuke.root().knob("KM_NGJ_Index_"+newBookMarkWindowInstance.NodeName.getValue()).setVisible(False)

        self.myParrent.close()

        

class NewBookMarkWindow(nukescripts.PythonPanel):
    """window for add new bookmark"""
    def __init__(self,nodeName,type,index):
        nukescripts.PythonPanel.__init__(self, 'Define New Bookmark')
        if type == "add":
            ### find selected node
            selectedNode = nuke.selectedNode() 
            for node in nuke.selectedNodes() : 
                selectedNode = node
            ##print selected_node['name'].getValue() 
            self.Title = nuke.EvalString_Knob("node_name2", "BookMark Name")
            title = ""
            if nuke.toNode(selectedNode['name'].getValue())["label"].getValue() != "":
                title = nuke.toNode(selectedNode['name'].getValue())["label"].getValue()
            else:
                title = selectedNode['name'].getValue()
            self.Title.setValue(title)
            self.NodeName = nuke.EvalString_Knob("node_name2", "Node Name")
            self.NodeName.setValue(selectedNode['name'].getValue())
            self.NodeName.setEnabled(False)
            self.Index = nuke.Int_Knob("node_name", "Index")
            self.Index.setEnabled(False)
            self.Index.setValue(index)
            self.addKnob(self.Title)
            self.addKnob(self.NodeName)
            self.addKnob(self.Index)
            self.setMinimumSize(500,500)

        if type == "edit":
            self.Title = nuke.EvalString_Knob("node_name2", "BookMark Name")
            self.Title.setValue(nuke.root().knob("KM_NGJ_NN_"+nodeName).getValue())
            self.NodeName = nuke.EvalString_Knob("node_name2", "Node Name")
            self.NodeName.setValue(nodeName)
            self.NodeName.setEnabled(False)
            self.Index = nuke.Int_Knob("node_name", "Index")
            self.Index.setEnabled(False)
            self.Index.setValue(int(nuke.root().knob("KM_NGJ_Index_"+nodeName).getValue()))
            self.addKnob(self.Title)
            self.addKnob(self.NodeName)
            self.addKnob(self.Index)
            self.setMinimumSize(500,500)


class MainWindow(QWidget):
    """Main Navigation Window, Includes Bookmark buttons"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.settings = model.Settings().Load()

        width, height = 500, 400
        self.setFixedSize(width, height)
        offset = QPoint(width * 0.5, height * 0.5)
        self.move(QCursor.pos() - offset)

        grid = QGridLayout()
        grid.setContentsMargins(50,50,50,50)
        self.setLayout(grid)

        columnCounter, rowCounter = 0, 0

        settingKnobs = nuke.root().knobs()
        for n in range(0, 9):
            if columnCounter == 1 and rowCounter == 1:
                columnCounter += 1
                continue

            isEmpty = True
            for x in settingKnobs :
                if "KM_NGJ_NN_" in x:
                    #print "hast"
                    nodeName = x.replace('KM_NGJ_NN_', '')
                    #print nodeName
                    if int(nuke.root().knob("KM_NGJ_Index_"+nodeName).getValue()) == n:
                        isEmpty = False
                        bookmarkButtonInstance = BookmarkButton(nodeName,self,n)
                        bookmarkButtonInstance.SetNodeName(x)
                        bookmarkButtonInstance.setText(nuke.root().knob(x).getValue())
                        grid.addWidget(bookmarkButtonInstance, rowCounter, columnCounter)

            if isEmpty:
                bookmarkButtonInstance = BookmarkButton("empty",self,n)
                bookmarkButtonInstance.SetNodeName("empty")
                bookmarkButtonInstance.setText("")
                grid.addWidget(bookmarkButtonInstance, rowCounter, columnCounter)
            #print "row : " + str(row_counter)
            #print "column : "+str(column_counter)
            if columnCounter > 1:
                rowCounter += 1
                columnCounter = 0

            else:
                columnCounter += 1
  
        centerLogoButton = BookmarkButton("icon",self,4)
        centerLogoButton.setText("")
        centerLogoButton.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/icon.jpg"))
        centerLogoButton.setObjectName("label_icon")
        grid.addWidget(centerLogoButton, 1, 1)

        self.SetWindowProperties()

        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(0)
        self.setGraphicsEffect(self.effect)
        self.fade = QPropertyAnimation(self.effect, 'opacity'.encode())  # encode is utf-8 by default      
        self.fade.setDuration(300)
        self.fade.setStartValue(0)
        self.fade.setEndValue(1)
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
            #nuke.activeViewer().node()['channels'].setValue('rgba')
            self.close()

        self.close()

    def eventFilter(self, object, event):
        if event.type() in [QEvent.WindowDeactivate, QEvent.FocusOut]:
            self.close()
            return True
        return False


class SettingsWindow(QWidget,Ui_Form):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)
        self.settings = model.Settings().Load()
        self.updateUI()

        self.label_9.setText('''<a href='http://www.kmworks.ir' style='color:#555273;text-decoration: none;'>www.kmworks.ir</a>''')
        self.label_9.setOpenExternalLinks(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.pushButton_documentation.clicked.connect(self.applySettings)

    def updateUI(self):
        if self.settings["shakeEffect"] == "Enable" :
            self.checkBox_shake_effect.setChecked(True)
        else :
            self.checkBox_shake_effect.setChecked(False)

        if self.settings["zoomEffect"] == "Enable" :
            self.checkBox_zoom_effect.setChecked(True)
        else :
            self.checkBox_zoom_effect.setChecked(False)

        self.lineEdit_shortcut.setText(self.settings["shortcut"])

    def applySettings(self):
        if self.checkBox_shake_effect.isChecked():
            self.settings["shakeEffect"] = "Enable"
        else:
            self.settings["shakeEffect"] = "Disable"

        if self.checkBox_zoom_effect.isChecked():
            self.settings["zoomEffect"] = "Enable"
        else:
            self.settings["zoomEffect"] = "Disable"

        self.settings["shortcut"] = self.lineEdit_shortcut.text()
        model.Settings().Save(self.settings)
        menu = nuke.menu("Nuke")
        Km_NGJ = menu.addMenu("KmTools")
        Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraph_Easy_Navigate.start()",self.settings["shortcut"])
        self.close()


def showSettings():
    global settingsWindowInstance
    settingsWindowInstance = SettingsWindow()
    settingsWindowInstance.show()

def start():
    """Start up function for MainWindow"""
    global mainWindowInstance  # pylint: disable=global-statement
    mainWindowInstance = MainWindow()
    mainWindowInstance.show()