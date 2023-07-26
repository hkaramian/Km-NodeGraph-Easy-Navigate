""" data managment """

# Import Nuke Libraries
import nuke  
import nukescripts

# Import built-in Libraries
import json
import os
import re

# Import local libs
from constants import BOOKMARK_KNOB_PREFIX


class Settings():
    """use file system to store settings data"""

    @staticmethod
    def Load():
        pluginPath = os.path.dirname(__file__)
        with open(pluginPath+'/settings.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def Save(settingsData):
        pluginPath = os.path.dirname(__file__)
        with open(pluginPath+'/settings.json', 'w') as outfile:
            json.dump(settingsData, outfile)



class Bookmarks():
    """using nuke settings knobs to store bookmarks data"""

    @staticmethod
    def Load():
        """Load all bookmarks from nuke knobs"""
        settingKnobs = nuke.root().knobs()
        allBookmarksData = list()
        for x in settingKnobs :
            if BOOKMARK_KNOB_PREFIX in x: 
                nodeName = x.replace(BOOKMARK_KNOB_PREFIX, '')
                bookmarkDataString = nuke.root().knob(x).tooltip()
                bookmarkData = json.loads(bookmarkDataString, strict=False) # convert data string to dictinary
                allBookmarksData.append(bookmarkData)
                # check if exist any bookmark for this postition
        return allBookmarksData

    @staticmethod
    def Save():
        """save & update all bookmarks\n
        (remove all bookmarks knobs and save updated bookmarks as new knobs)"""

    @staticmethod
    def AddNewBookmark(bookmarkNodeName,bookmarkTitle,bookmarkIndex,bookmarkShortcut=""):
        # replace double quotes by singe quotes in title
        bookmarkTitle = bookmarkTitle.replace('"', "'")
        # remove double quotes and single quotes in shortcut
        bookmarkShortcut = bookmarkShortcut.replace('"', "")
        bookmarkShortcut = bookmarkShortcut.replace("'", "")
        """save new bookmark data as a new knob\n"""
        bookmarkDataString = '{' +'"nodeName": "{}", "title": "{}", "index": "{}", "shortcut" : "{}" '.format(bookmarkNodeName,bookmarkTitle,bookmarkIndex,bookmarkShortcut) + '}'
        # bookmark data string sample : '{"nodeName": "NodeName","title": "", "index": "", "shortcut" : ""}'
        knobName = BOOKMARK_KNOB_PREFIX + bookmarkNodeName
        nuke.root().addKnob(nuke.EvalString_Knob(knobName, "Km Nodegraph Bookmark Data"))
        #nuke.root().knob(knobName).setValue(bookmarkDataString)
        nuke.root().knob(knobName).setTooltip(bookmarkDataString) # for store data in nuke knob: instead of setValue function we use setTooltip function, so we can see and edit data string in nuke knob edit window
        nuke.root().knob(knobName).setVisible(False)
        Bookmarks.SetToggleIfExist()

    @staticmethod
    def UpdateBookmarkData(bookmarkData) :
        # replace double quotes by singe quotes in title
        bookmarkData["title"] = bookmarkData["title"].replace('"', "'")
        # remove double quotes and single quotes in shortcut
        bookmarkData["shortcut"] = bookmarkData["shortcut"].replace('"', "")
        bookmarkData["shortcut"] = bookmarkData["shortcut"].replace("'", "")
        bookmarkDataString = '{' +'"nodeName": "{}", "title": "{}", "index": "{}", "shortcut" : "{}" '.format(bookmarkData["nodeName"],bookmarkData["title"],bookmarkData["index"],bookmarkData["shortcut"]) + '}'
        knobName = BOOKMARK_KNOB_PREFIX + bookmarkData["nodeName"]
        nuke.root().knob(knobName).setTooltip(bookmarkDataString)
        Bookmarks.SetToggleIfExist()

    @staticmethod
    def getBookmarkData(nodeName):
        """return bookmark data dict"""
        knobName = BOOKMARK_KNOB_PREFIX + nodeName
        bookmarkDataString = nuke.root().knob(knobName).tooltip()
        bookmarkData = json.loads(bookmarkDataString, strict=False) # convert data string to dictinary
        return bookmarkData
    
    @staticmethod
    def removeABookmark(nodeName):
        knobNameToRemove = BOOKMARK_KNOB_PREFIX + nodeName
        nuke.root().removeKnob(nuke.root().knobs()[knobNameToRemove])
        Bookmarks.SetToggleIfExist()

    @staticmethod
    def ResetBookmarks():
        """remove all bookmarks in current project"""
        settingKnobs = nuke.root().knobs()
        for x in settingKnobs :
            if BOOKMARK_KNOB_PREFIX in x:
                nuke.root().removeKnob(nuke.root().knobs()[x])
        Bookmarks.SetToggleIfExist()

    @staticmethod
    def getTotalBookmarksCount():
        settings = Settings.Load()
        numberOfBookmarks = int(settings["bookmarksGridColumns"]) * int(settings["bookmarksGridRows"])
        return numberOfBookmarks

    @staticmethod
    def GetToggles():
        """return toggle data"""
        toggleKnobsPrefix = "KmEN" # do not use the same as bookmarks knob prefix, it cause bug
        toggle1 = toggleKnobsPrefix + "toggle1"
        toggle2 = toggleKnobsPrefix + "toggle2"
        lastToggle = toggleKnobsPrefix + "lastToggle"
        toggleShortcut = toggleKnobsPrefix + "toggleShortcut"
        toggle1_Nodename = ""
        toggle2_Nodename = ""
        lastToggle_Nodename = ""
        toggleShortcut_value = ""
        if nuke.root().knob(toggle1):
            toggle1_Nodename = nuke.root().knob(toggle1).tooltip()
        if nuke.root().knob(toggle2):
            toggle2_Nodename = nuke.root().knob(toggle2).tooltip()
        if nuke.root().knob(lastToggle):
            lastToggle_Nodename = nuke.root().knob(lastToggle).tooltip()
        if nuke.root().knob(toggleShortcut):
            toggleShortcut_value = nuke.root().knob(toggleShortcut).tooltip()
        return toggle1_Nodename,toggle2_Nodename,lastToggle_Nodename,toggleShortcut_value

    @staticmethod
    def UpdateToggles(toggle1_Nodename,toggle2_Nodename,lastToggle_Nodename,toggleShortcut_value):
        """update toggle data"""

        toggleKnobsPrefix = "KmEN" # do not use the same as bookmarks knob prefix, it cause bug
        # knobs names
        toggle1 = toggleKnobsPrefix + "toggle1"
        toggle2 = toggleKnobsPrefix + "toggle2"
        lastToggle = toggleKnobsPrefix + "lastToggle"
        toggleShortcut = toggleKnobsPrefix + "toggleShortcut"
        
        # remove old knobs
        if nuke.root().knob(toggle1):
            nuke.root().removeKnob(nuke.root().knobs()[toggle1])
        if nuke.root().knob(toggle2):
            nuke.root().removeKnob(nuke.root().knobs()[toggle2])
        if nuke.root().knob(lastToggle):
            nuke.root().removeKnob(nuke.root().knobs()[lastToggle])
        if nuke.root().knob(toggleShortcut):
            nuke.root().removeKnob(nuke.root().knobs()[toggleShortcut])

        # create new knobs    
        nuke.root().addKnob(nuke.EvalString_Knob(toggleKnobsPrefix + "toggle1", "Km Nodegraph toggle1"))
        nuke.root().addKnob(nuke.EvalString_Knob(toggleKnobsPrefix + "toggle2", "Km Nodegraph toggle2"))
        nuke.root().addKnob(nuke.EvalString_Knob(toggleKnobsPrefix + "lastToggle", "Km Nodegraph lastToggle"))
        nuke.root().addKnob(nuke.EvalString_Knob(toggleKnobsPrefix + "toggleShortcut", "Km Nodegraph toggleShortcut"))
        # Hide knobs 
        nuke.root().knob(toggleKnobsPrefix + "toggle1").setVisible(False)
        nuke.root().knob(toggleKnobsPrefix + "toggle2").setVisible(False)
        nuke.root().knob(toggleKnobsPrefix + "lastToggle").setVisible(False) 
        nuke.root().knob(toggleKnobsPrefix + "toggleShortcut").setVisible(False)
        # set knobs values
        nuke.root().knob(toggleKnobsPrefix + "toggle1").setTooltip(toggle1_Nodename)
        nuke.root().knob(toggleKnobsPrefix + "toggle2").setTooltip(toggle2_Nodename)
        nuke.root().knob(toggleKnobsPrefix + "lastToggle").setTooltip(lastToggle_Nodename)    
        nuke.root().knob(toggleKnobsPrefix + "toggleShortcut").setTooltip(toggleShortcut_value)  
    
    @staticmethod
    def SetToggleIfExist():
        """go through the bookmarks and set toogle if exist"""
        Bookmarks.UpdateToggles("", "", "", "")
        bookmarksData = Bookmarks.Load()
        for i in range(len(bookmarksData)):
            for j in range(i+1, len(bookmarksData)):
                if bookmarksData[i]["shortcut"] == bookmarksData[j]["shortcut"]:
                    toggle1NodeName = bookmarksData[i]["nodeName"]
                    toggle2NodeName = bookmarksData[j]["nodeName"]
                    Bookmarks.UpdateToggles(toggle1NodeName, toggle2NodeName, toggle1NodeName, bookmarksData[i]["shortcut"])



class BookmarkTemplates : 
    """store bookmarks templates data in files"""

    @staticmethod
    def Load():
        templatesPath = os.path.dirname(__file__)+"/templates/"
        templatesFiles = os.listdir(templatesPath)
        templatesList = list()
        for templateFile in templatesFiles :
            if (templateFile.endswith(".json")) :
                with open(templatesPath+templateFile) as json_file:
                    templatesList.append(json.load(json_file))
        
        return templatesList

    @staticmethod
    def AddNew(templateName):
        templateData = { 
            "templateName" : templateName ,
            "fileName" : BookmarkTemplates.get_valid_filename(templateName) + '.json' ,
            "bookmarks" : { 
                            1 : {"nodeName": "", "title": "", "index": "", "shortcut": ""} 
                        } 
                        }
        bookmarksData = Bookmarks.Load()
        if (len(bookmarksData) == 0) : return False # return if there is no bookmark
        counter = 1
        for item in bookmarksData :
            templateData['bookmarks'][counter] =  {"nodeName": item["nodeName"], "title": item["title"], "index": item["index"], "shortcut": item["shortcut"]}
            counter += 1

        templatesPath = os.path.dirname(__file__)+"/templates/"
        with open(templatesPath + templateData["fileName"], 'w') as outfile:
            json.dump(templateData, outfile)

    @staticmethod
    def DeleteTemplateFile(templateFileName):
        templateFilePath = os.path.dirname(__file__)+"/templates/" + templateFileName
        os.remove(templateFilePath)

    @staticmethod
    def GetATemplateData(templateFileName):
        templatesFilePath = os.path.dirname(__file__)+"/templates/"+templateFileName
        if os.path.exists(templatesFilePath) : 
            with open(templatesFilePath) as json_file:
                return json.load(json_file)


    @staticmethod
    def get_valid_filename(s):
        """
        Return the given string converted to a string that can be used for a clean
        filename. Remove leading and trailing spaces; convert other spaces to
        underscores; and remove anything that is not an alphanumeric, dash,
        underscore, or dot.
        >>> get_valid_filename("john's portrait in 2004.jpg")
        'johns_portrait_in_2004.jpg'
        """
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s) 