"""import compatible pyside lib for each version of nuke"""

# Import Nuke Libraries
import nuke  

# Pyside Library Import (pyside and pyside 2)  : pyside for nuke10.5 and older , pyside2 for nuke 11.0 and newer
try:

    if int(nuke.env ["NukeVersionMajor"]) < 11:
        from PySide.QtCore import *
        from PySide.QtGui import *
    else:
        from PySide2.QtCore import *
        from PySide2.QtGui import *
        from PySide2.QtWidgets import *
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
    pass