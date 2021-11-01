import nuke
import Km_NodeGraphJump

menu = nuke.menu("Nuke")
Km_NGJ = menu.addMenu("KmTools")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraphJump.start()","shift+e")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Settings | Help","Km_NodeGraphJump.showSettings()","")
