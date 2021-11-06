


#
#
# Km NodeGraph Easy Navigate v1.1
#
# Developed By Hossein Karamian
# 
# www.kmworks.ir
#
#    _  __  __  __ 
#   | |/ / |  \/  |
#   | ' /  | \  / |
#   |  <   | |\/| |
#   |_|\_\ |_|  |_|
#

"""
Change Log :
v1.0 | first version | December 4 , 2020 
v1.1 | nuke 13 compatible | November 1 , 2021
"""


import math
import nuke  
import os
import threading
import time
import datetime
import json

# Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer

try:
    import nuke
    import nukescripts
    if int(nuke.env ["NukeVersionMajor"]) < 11:
        from PySide.QtCore import *
        from PySide.QtGui import *
        #print "Km Backup And Recovery ToolKit : www.kmworks.ir"
    else:
        from PySide2.QtCore import *
        from PySide2.QtGui import *
        from PySide2.QtWidgets import *
        #print "Km Backup And Recovery ToolKit : www.kmworks.ir"
except ImportError:
    print ("not in nuke") # pycharm
    try:
        from PySide.QtCore import *
        from PySide.QtGui import *
        #print "using pyside"
    except ImportError:
        from PyQt4.QtCore import *
        from PyQt4.QtGui import *
        Signal = pyqtSignal
        #print "using pyqt4"
    pass

Km_Panel = None

COLORS = {'regular': "background-color:#282828; font: 13px",
          'orange': "background-color:#C26828; font: 13px",
          'green': "background-color: #1EB028; font: 13px"}

# To create the new introduced Shuffle2 nodes in Nuke 12, set SHUFFLE_TYPE value to 1.
# SHUFFLE_TYPE = 0  old shuffle node
# SHUFFLE_TYPE = 1 new shuffle node

SHUFFLE_TYPE = 1


class LayerButton(QPushButton):
    """Custom QPushButton to change colors when hovering above."""

    def __init__(self, name, button_width, parent=None):
        super(LayerButton, self).__init__(parent)
        self.setMouseTracking(True)
        self.setText(name)
        self.setMinimumWidth(button_width / 2)
        self.setMaximumHeight(30)
        self.setSizePolicy(QSizePolicy.Preferred,
                           QSizePolicy.Expanding)
        self.setStyleSheet(COLORS['regular'])

    def enterEvent(self, event):  # pylint: disable=invalid-name,unused-argument
        """Change color to orange when mouse enters button."""
        if not self.styleSheet() == COLORS['green']:
            self.setStyleSheet(COLORS['orange'])

    def leaveEvent(self, event):  # pylint: disable=invalid-name,unused-argument
        """Change color to grey when mouse leaves button."""
        if not self.styleSheet() == COLORS['green']:
            self.setStyleSheet(COLORS['regular'])


class ActionLabel(QLabel):
    def __init__(self, id,pr,index):
        super(ActionLabel, self).__init__()

        self.my_parrent = pr
        self.Index = index

        self.id = id
        self.mainPosX = 0
        self.mainPosY = 0
        self.NodeName = "node name"
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking(True)
        self.setFixedWidth(70)
        self.setFixedHeight(70)
        self.setStyleSheet("""background:gray;
                            color:white ; border:2px red ; font-size:14px;""")
        self.setText("Final Render")


        self.setWordWrap(True)

        #self.set_action()






    def setNodeName(self,NN):
        self.NodeName = NN

    def enterEvent(self, event): 
        self.setStyleSheet("""background:orange;
                            color:white ;font-size:18px;""")


        self.mainPosX = self.x()
        self.mainPosY = self.y()
        self.anim3 = QPropertyAnimation(self, "geometry")
        self.anim3.setDuration(100)
        w = 70
        h = 70
        self.anim3.setStartValue(QRect(self.mainPosX, self.mainPosY, w, h))
        self.anim3.setEndValue(QRect(self.mainPosX-((110-w)/2), self.mainPosY-((110-h)/2), 110, 110))



        self.anim = QPropertyAnimation(self, "minimumHeight")
        self.anim.setDuration(100)
        self.anim.setStartValue(70)
        self.anim.setEndValue(110)    

        self.anim2 = QPropertyAnimation(self, "minimumWidth")
        self.anim2.setDuration(100)
        self.anim2.setStartValue(70)
        self.anim2.setEndValue(110)

        self.anim3.start()
        self.anim.start()
        self.anim2.start()
        #print "done"
        #self.anim2.start()

    def scaleUpEffect(self):
        scale = 70
        for i in xrange( 0, 100 ):
            time.sleep( 0.0015 )
            #print(datetime.datetime.now())
            scale = scale + 0.5
            self.setFixedWidth(scale)
            self.setFixedHeight(scale)

    def leaveEvent(self, event):  
        self.setStyleSheet("""background:gray;
                            color:white;font-size:14px;""")
        #if not self.styleSheet() == COLORS['green']:
        #    self.setStyleSheet(COLORS['regular'])

        
        self.anim = QPropertyAnimation(self, "minimumHeight")
        self.anim.setDuration(100)
        self.anim.setStartValue(110)
        self.anim.setEndValue(70)    

        self.anim2 = QPropertyAnimation(self, "minimumWidth")
        self.anim2.setDuration(100)
        self.anim2.setStartValue(110)
        self.anim2.setEndValue(70)

        w = 70
        h = 70
        self.anim3.setStartValue(QRect(self.mainPosX, self.mainPosY, w, h))
        self.anim3.setEndValue(QRect(self.mainPosX+((110-w)/2), self.mainPosY+((110-h)/2), 70, 70))

        self.anim3.start()
        self.anim.start()
        self.anim2.start()
        
 
    def JumpAndShakeEffect(self,SN):

        xC = SN.xpos() + SN.screenWidth()/2
        yC = SN.ypos() + SN.screenHeight()/2
        nuke.zoom( 1, [ xC, yC ])

        move_value = 5  
        for i in xrange( 0, 8 ):
            move_value = move_value * -1
            SN.setXpos(int(SN["xpos"].getValue())+ move_value)
            time.sleep( 0.05 )
            #print move_value
            #print(datetime.datetime.now())

    def ZoomInEffect(self,SN):
        zoom = 0.1  
        for i in xrange( 0, 200 ):
            time.sleep( 0.0015 )
            #print(datetime.datetime.now())
            node = SN
            xC = node.xpos() + node.screenWidth()/2
            yC = node.ypos() + node.screenHeight()/2
            zoom = zoom + 0.01
            if zoom > 1:
                break
            nuke.zoom( zoom, [ xC, yC ])

    def SimpleJump(self,SN):
        node = SN
        xC = node.xpos() + node.screenWidth()/2
        yC = node.ypos() + node.screenHeight()/2
        nuke.zoom( 1, [ xC, yC ])


    def mousePressEvent(self, event):

        NavigationEffect = "JumpAndShake"
        NavigationEffect = "ZoomIn"

        if event.buttons() == Qt.LeftButton:
            if self.id == "icon" :
                global Km_EasyNavigate_Settings_Instance
                Km_EasyNavigate_Settings_Instance = Km_EasyNavigate_Settings()
                Km_EasyNavigate_Settings_Instance.show()
            if self.id == "empty" :
                if nuke.selectedNodes() == [] :
                    nuke.message("First select a node to define new Shortcut")
                else:                    
                    #print self.id
                    selected_node = nuke.selectedNode() 
                    if not nuke.root().knob("KM_NGJ_NN_"+selected_node['name'].getValue()):
                        p = NewBokMarkPanel("empty","add",self.Index)
                        p.setMinimumSize(300, 50)
                        if p.showModalDialog() :
                            if not nuke.root().knob("KM_NGJ_NN_"+p.NodeName.getValue()):
                                #print p.Title.getValue()
                                #print p.NodeName.getValue()
                                #print p.Index.getValue()
                                nuke.root().addKnob(nuke.EvalString_Knob("KM_NGJ_NN_"+p.NodeName.getValue(), "Title"))
                                nuke.root().knob("KM_NGJ_NN_"+p.NodeName.getValue()).setValue(p.Title.getValue())
                                nuke.root().knob("KM_NGJ_NN_"+p.NodeName.getValue()).setVisible(False)
                                nuke.root().addKnob(nuke.Int_Knob("KM_NGJ_Index_"+p.NodeName.getValue(), "Title"))
                                nuke.root().knob("KM_NGJ_Index_"+p.NodeName.getValue()).setValue(int(p.Index.getValue()))
                                nuke.root().knob("KM_NGJ_Index_"+p.NodeName.getValue()).setVisible(False)
                    else :
                        nuke.message("Selected node exists in the list, you can delete or edite that")

        if event.buttons() == Qt.LeftButton:
            if self.id != "empty" and self.id != "icon":
                node = nuke.toNode(self.id.replace('KM_NGJ_NN_', ''))

                nuke.root().knob("KM_NGJ_NN_"+node['name'].getValue())
                if self.my_parrent.settings["zoomEffect"] == "Enable":
                    threading.Thread( target=self.ZoomInEffect, args=(node,)).start()
                else:
                    self.SimpleJump(node)

                if self.my_parrent.settings["shakeEffect"] == "Enable":
                    threading.Thread( target=self.JumpAndShakeEffect, args=(node,)).start()
             



        if event.buttons() == Qt.RightButton:

            if self.id != "empty" and self.id != "icon":
                #print "RightButton"
                ## Remove BookMark
                nodeName = self.id.replace('KM_NGJ_NN_', '')
                knobName1 = "KM_NGJ_NN_"+nodeName
                knobName2 = "KM_NGJ_Index_"+nodeName
                if nuke.ask("Remove "+nuke.root().knob("KM_NGJ_NN_"+self.id).getValue()+" Bookmark ?"):
                    nuke.root().removeKnob(nuke.root().knobs()[knobName1])
                    nuke.root().removeKnob(nuke.root().knobs()[knobName2])
                else :
                    pass


            #ex = Example()
            #ex.show()

        if event.buttons() == Qt.MiddleButton:
            #print "MiddleButton"
            # Edit Bookmark

            if self.id != "empty" and self.id != "icon":
                nodeName = self.id.replace('KM_NGJ_NN_', '')
                p = NewBokMarkPanel(nodeName,"edit",0)
                p.setMinimumSize(300, 50)
                if p.showModalDialog() :
                    #print p.Title.getValue()
                    #print p.NodeName.getValue()
                    #print p.Index.getValue()
                    nuke.root().knob("KM_NGJ_NN_"+p.NodeName.getValue()).setValue(p.Title.getValue())
                    nuke.root().knob("KM_NGJ_NN_"+p.NodeName.getValue()).setVisible(False)
                    nuke.root().knob("KM_NGJ_Index_"+p.NodeName.getValue()).setValue(int(p.Index.getValue()))
                    nuke.root().knob("KM_NGJ_Index_"+p.NodeName.getValue()).setVisible(False)

        self.my_parrent.close()

        


class NewBokMarkPanel(nukescripts.PythonPanel):
    def __init__(self,nodeName,type,index):
        nukescripts.PythonPanel.__init__(self, 'Define New Item - Node Graph Jump')

        if type == "add":
            ### find selected node
            selected_node = nuke.selectedNode() 
            for node in nuke.selectedNodes() : 
                selected_node = node
            ##print selected_node['name'].getValue() 
            self.Title = nuke.EvalString_Knob("node_name2", "BookMark Name")
            title = ""
            if nuke.toNode(selected_node['name'].getValue())["label"].getValue() != "":
                title = nuke.toNode(selected_node['name'].getValue())["label"].getValue()
            else:
                title = selected_node['name'].getValue()
            self.Title.setValue(title)
            self.NodeName = nuke.EvalString_Knob("node_name2", "Node Name")
            self.NodeName.setValue(selected_node['name'].getValue())
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



class Km_Panel(QWidget):
    

    settings = {
      "shakeEffect": "Enable",
      "zoomEffect": "Enable",
      "shortcut": "shift+e", 
    }

    def __init__(self):
        super(Km_Panel, self).__init__()

        self.load_settings()


        self.shuffle_list = []

        width, height = 500, 400
        self.setFixedSize(width, height)
        offset = QPoint(width * 0.5, height * 0.5)
        self.move(QCursor.pos() - offset)

        grid = QGridLayout()
        grid.setContentsMargins(50,50,50,50)
        self.setLayout(grid)

        column_counter, row_counter = 0, 0
        button_width = 100

        """
        for layer in xrange(1,12):
            #button = LayerButton("test", 100)
            km_lable_instance = ActionLabel(1)
            #button.clicked.connect(self.clicked)
            #grid.addWidget(button, row_counter, column_counter)
            grid.addWidget(km_lable_instance, row_counter, column_counter)
            print "row : " + str(row_counter)
            print "column : "+str(column_counter)
            if column_counter > 2:
                row_counter += 1
                column_counter = 0

            else:
                column_counter += 1
                print "cond"
        """

        settingKnobs = nuke.root().knobs()
        for n in range(0, 9):
            #button = LayerButton("test", 100)

            if column_counter == 1 and row_counter == 1:
                column_counter += 1
                continue

            isEmpty = True
            for x in settingKnobs :
                if "KM_NGJ_NN_" in x:
                    #print "hast"
                    #button = LayerButton("test", 100)
                    nodeName = x.replace('KM_NGJ_NN_', '')
                    #print nodeName
                    if int(nuke.root().knob("KM_NGJ_Index_"+nodeName).getValue()) == n:
                        isEmpty = False
                        km_lable_instance = ActionLabel(nodeName,self,n)
                        km_lable_instance.setNodeName(x)
                        km_lable_instance.setText(nuke.root().knob(x).getValue())
                    #button.clicked.connect(self.clicked)
                    #grid.addWidget(button, row_counter, column_counter)
                        grid.addWidget(km_lable_instance, row_counter, column_counter)

            if isEmpty:
                km_lable_instance = ActionLabel("empty",self,n)
                km_lable_instance.setNodeName("empty")
                km_lable_instance.setText("")
                #button.clicked.connect(self.clicked)
                #grid.addWidget(button, row_counter, column_counter)
                grid.addWidget(km_lable_instance, row_counter, column_counter)

            #print "row : " + str(row_counter)
            #print "column : "+str(column_counter)
            if column_counter > 1:
                row_counter += 1
                column_counter = 0

            else:
                column_counter += 1
                #print "cond"


        """
        for x in nuke.root().knobs():
            if "KM_NGJ_NN_" in x:
                #button = LayerButton("test", 100)
                km_lable_instance = ActionLabel(x,self)
                km_lable_instance.setNodeName(x)
                km_lable_instance.setText(nuke.root().knob(x).getValue())
                #button.clicked.connect(self.clicked)
                #grid.addWidget(button, row_counter, column_counter)
                if column_counter == 1 and row_counter == 1:
                    #column_counter += 1
                    continue
                grid.addWidget(km_lable_instance, row_counter, column_counter)
                print "row : " + str(row_counter)
                print "column : "+str(column_counter)
                if column_counter > 1:
                    row_counter += 1
                    column_counter = 0

                else:
                    column_counter += 1
                    print "cond"
        """

        label_icon = ActionLabel("icon",self,4)
        label_icon.setText("")
        label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/icon.jpg"))
        label_icon.setObjectName("label_icon")
        grid.addWidget(label_icon, 1, 1)

        #label_add_new = ActionLabel("add_new",self)
        #label_add_new.setText("Add New")
        #grid.addWidget(label_add_new, row_counter, 2)

        #self.input = LineEdit(self, layers)
        #grid.addWidget(self.input, row_counter, column_counter)
        #self.input.returnPressed.connect(self.line_enter)

        self.set_window_properties()
        #op=QGraphicsOpacityEffect(self)
        #op.setOpacity(0.2) #0 to 1 will cause the fade effect to kick in
        #self.setGraphicsEffect(op)
        #self.setAutoFillBackground(True)



        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(0)
        self.setGraphicsEffect(self.effect)
        self.fade = QPropertyAnimation(self.effect, 'opacity'.encode())  # encode is utf-8 by default      
        self.fade.setDuration(500)
        self.fade.setStartValue(0)
        self.fade.setEndValue(1)
        self.fade.start()


    def load_settings(self):
        plugin_path = os.path.dirname(__file__)
        with open(plugin_path+'/settings.json') as json_file:
            self.settings = json.load(json_file)

    def save_settings(self):
        plugin_path = os.path.dirname(__file__)
        with open(plugin_path+'/settings.json', 'w') as outfile:
            json.dump(self.settings, outfile)

    def set_window_properties(self):
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




    def line_enter(self):
        """Change Viewer to completed text."""
        self.active_viewer['channels'].setValue(self.input.text())
        self.close()

    def eventFilter(self, object, event):
        if event.type() in [QEvent.WindowDeactivate, QEvent.FocusOut]:
            self.close()
            return True
        return False





class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(397, 421)
        icon = QIcon()
        icon.addPixmap(QPixmap(os.path.dirname(__file__)+"/icons/icon.png"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_7 = QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_settings4 = QGroupBox(Form)
        self.groupBox_settings4.setObjectName("groupBox_settings4")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_settings4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(30, -1, 20, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_shake_effect = QCheckBox(self.groupBox_settings4)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_shake_effect.setFont(font)
        self.checkBox_shake_effect.setChecked(False)
        self.checkBox_shake_effect.setObjectName("checkBox_shake_effect")
        self.verticalLayout_4.addWidget(self.checkBox_shake_effect)
        self.checkBox_zoom_effect = QCheckBox(self.groupBox_settings4)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_zoom_effect.setFont(font)
        self.checkBox_zoom_effect.setChecked(True)
        self.checkBox_zoom_effect.setObjectName("checkBox_zoom_effect")
        self.verticalLayout_4.addWidget(self.checkBox_zoom_effect)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_settings4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_shortcut = QLineEdit(self.groupBox_settings4)
        self.lineEdit_shortcut.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_shortcut.setObjectName("lineEdit_shortcut")
        self.horizontalLayout_4.addWidget(self.lineEdit_shortcut)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_icon = QLabel(self.groupBox_settings4)
        self.label_icon.setText("")
        self.label_icon.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/icon.png"))
        self.label_icon.setObjectName("label_icon")
        self.verticalLayout_3.addWidget(self.label_icon)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.pushButton_documentation = QPushButton(self.groupBox_settings4)
        self.pushButton_documentation.setObjectName("pushButton_documentation")
        self.verticalLayout_8.addWidget(self.pushButton_documentation)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_2.addWidget(self.groupBox_settings4)
        self.groupBox_status = QGroupBox(Form)
        self.groupBox_status.setObjectName("groupBox_status")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_status)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(20, -1, 15, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QLabel(self.groupBox_status)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_4 = QLabel(self.groupBox_status)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QLabel(self.groupBox_status)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_2 = QLabel(self.groupBox_status)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.line = QFrame(self.groupBox_status)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.label_6 = QLabel(self.groupBox_status)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.label_icon_2 = QLabel(self.groupBox_status)
        self.label_icon_2.setFrameShape(QFrame.NoFrame)
        self.label_icon_2.setText("")
        self.label_icon_2.setPixmap(QPixmap(os.path.dirname(__file__)+"/icons/mouse.png"))
        self.label_icon_2.setObjectName("label_icon_2")
        self.horizontalLayout.addWidget(self.label_icon_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_status)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_plugins_version = QLabel(Form)
        self.label_plugins_version.setObjectName("label_plugins_version")
        self.horizontalLayout_2.addWidget(self.label_plugins_version)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QLabel(Form)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Km NodeGraph Easy Navigate"))
        self.groupBox_settings4.setTitle(_translate("Form", "Settings"))
        self.checkBox_shake_effect.setText(_translate("Form", "Shake Effect"))
        self.checkBox_zoom_effect.setText(_translate("Form", "Zoom Effect"))
        self.label_3.setText(_translate("Form", "Shortcut :"))
        self.lineEdit_shortcut.setText(_translate("Form", "shift+e"))
        self.pushButton_documentation.setText(_translate("Form", "Apply"))
        self.groupBox_status.setTitle(_translate("Form", "Help"))
        self.label.setText(_translate("Form", "Left Button    :    Jump to Bookmark"))
        self.label_4.setText(_translate("Form", "                         Assign New Bookmark"))
        self.label_5.setText(_translate("Form", "Middle Button :   Edit"))
        self.label_2.setText(_translate("Form", "Right Button  :    Remove"))
        self.label_6.setText(_translate("Form", "Assign Bookmark : Select a node or backdrop, Then click on an empty bookmark to assign"))
        self.label_plugins_version.setText(_translate("Form", "Km NodeGraph Easy Navigate v1.1"))
        self.label_8.setText(_translate("Form", "By Hossein Karamian"))
        self.label_9.setText(_translate("Form", "www.kmworks.ir"))






class Km_EasyNavigate_Settings(QWidget,Ui_Form):

    settings = {
          "shakeEffect": "Enable",
          "zoomEffect": "Enable",
          "shortcut": "shift+e", 
        }

    def __init__(self):
        super(Km_EasyNavigate_Settings, self).__init__()
        self.setupUi(self)

        self.updateUI()

        self.label_9.setText('''<a href='http://www.kmworks.ir' style='color:#555273;text-decoration: none;'>www.kmworks.ir</a>''')
        self.label_9.setOpenExternalLinks(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.pushButton_documentation.clicked.connect(self.applySettings)

    def updateUI(self):

        self.load_settings()

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
        
        self.save_settings()
        menu = nuke.menu("Nuke")
        Km_NGJ = menu.addMenu("KmTools")
        Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraphJump.start()",self.settings["shortcut"])

        self.close()

    def load_settings(self):
        plugin_path = os.path.dirname(__file__)
        with open(plugin_path+'/settings.json') as json_file:
            self.settings = json.load(json_file)

    def save_settings(self):
        plugin_path = os.path.dirname(__file__)
        with open(plugin_path+'/settings.json', 'w') as outfile:
            json.dump(self.settings, outfile)



def showSettings():
    global Km_EasyNavigate_Settings_Instance
    Km_EasyNavigate_Settings_Instance = Km_EasyNavigate_Settings()
    Km_EasyNavigate_Settings_Instance.show()

def start():
    """Start up function for Km_Panel. Checks if Viewer available and active."""
    global Km_Panel_instance  # pylint: disable=global-statement
    Km_Panel_instance = Km_Panel()
    Km_Panel_instance.show()




