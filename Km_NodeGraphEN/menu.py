import nuke
import Km_NodeGraph_Easy_Navigate
import model

settings = model.Settings().Load()
menu = nuke.menu("Nuke")
Km_NGJ = menu.addMenu("KmTools")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","Km_NodeGraph_Easy_Navigate.ShowMainWindow()",settings["shortcut"],shortcutContext=2)
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Settings | Help","Km_NodeGraph_Easy_Navigate.ShowSettings()","")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Edit Bookmarks","Km_NodeGraph_Easy_Navigate.ShowEditBookmarksWindow()","")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Templates","Km_NodeGraph_Easy_Navigate.ShowTemplatesWindow()","")