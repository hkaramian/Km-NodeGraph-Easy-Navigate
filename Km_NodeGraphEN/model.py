""" data managment"""

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
        """save new bookmark data as a new knob\n"""
        bookmarkDataString = '{' +'"nodeName": "{}", "title": "{}", "index": "{}", "shortcut" : "{}" '.format(bookmarkNodeName,bookmarkTitle,bookmarkIndex,bookmarkShortcut) + '}'
        # bookmark data string sample : '{"nodeName": "NodeName","title": "", "index": "", "shortcut" : ""}'
        knobName = BOOKMARK_KNOB_PREFIX + bookmarkNodeName
        nuke.root().addKnob(nuke.EvalString_Knob(knobName, "Km Nodegraph Bookmark Data"))
        #nuke.root().knob(knobName).setValue(bookmarkDataString)
        nuke.root().knob(knobName).setTooltip(bookmarkDataString) # for store data in nuke knob: instead of setValue function we use setTooltip function, so we can see and edit data string in nuke knob edit window
        nuke.root().knob(knobName).setVisible(False)

    @staticmethod
    def UpdateBookmarkData(bookmarkData) :
        bookmarkDataString = '{' +'"nodeName": "{}", "title": "{}", "index": "{}", "shortcut" : "{}" '.format(bookmarkData["nodeName"],bookmarkData["title"],bookmarkData["index"],bookmarkData["shortcut"]) + '}'
        knobName = BOOKMARK_KNOB_PREFIX + bookmarkData["nodeName"]
        nuke.root().knob(knobName).setTooltip(bookmarkDataString)

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

    @staticmethod
    def ResetBookmarks():
        """remove all bookmarks in current project"""
        settingKnobs = nuke.root().knobs()
        for x in settingKnobs :
            if BOOKMARK_KNOB_PREFIX in x:
                nuke.root().removeKnob(nuke.root().knobs()[x])

    @staticmethod
    def getTotalBookmarksCount():
        settings = Settings.Load()
        numberOfBookmarks = int(settings["bookmarksGridColumns"]) * int(settings["bookmarksGridRows"])
        return numberOfBookmarks
        


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