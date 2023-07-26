import nuke
import controller
import model

settings = model.Settings().Load()
menu = nuke.menu("Nuke")
Km_NGJ = menu.addMenu("KmTools")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Show Panel","controller.ShowMainWindow()",settings["shortcut"],shortcutContext=2)
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Settings | Help","controller.ShowSettings()","")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Edit Bookmarks","controller.ShowEditBookmarksWindow()","")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Templates","controller.ShowTemplatesWindow()","")
Km_NGJ.addCommand("Km NodeGraph Easy Navigate/Survive (Reset Bookmarks)","controller.Survive()","")
