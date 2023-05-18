# -*- coding: utf-8 -*-
from . import helpers

class Edl:
    # This class stores the data about our EDL in a list of dicts format (self.body).
    # Other data is stored as other properties.
    def __init__(self,path):
        self.title = helpers.importEdlTitle(path)
        self.body = helpers.importEdlBody(path)
        self.fcm = helpers.importEdlFcm(path)
    
    def exportJson(self,path):
        # Todo
        pass

    def exportExcel(self,path,effects=False):
        # Todo
        if effects == False:
            body = helpers.dumpEffects(self.body)
        else:
            body = self.body
        pass

    def listFiles(self):
        # Todo
        fileList = []
        for line in self.body:
            source = line.get('SOURCE FILE')
            fileList.append(source)
        # This checks if the list is empty and raises an error if so.
        if not fileList:
            raise ValueError('No source file names found - check these are selected on editing software.')
        return fileList

def elfFileSearchCopy(list,searchpath,destination):
    # Todo
    # This function loops across "list" and searches "searchpath" for each file.
    # If it finds the file, it copies it to "destination"
    # This logic identifys any common spanned files, and copies the folder instead
    pass 