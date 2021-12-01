import nuke
import Km_NodeGraph_Easy_Navigate

menu = nuke.menu("Nuke")
Km_NGJ = menu.addMenu("KmTools")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraph_Easy_Navigate.start()","shift+e")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Settings | Help","Km_NodeGraph_Easy_Navigate.showSettings()","")
