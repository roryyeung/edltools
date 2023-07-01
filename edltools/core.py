# -*- coding: utf-8 -*-
from . import helpers

class Edl:
    # This class stores the data about our EDL in a list of dicts format (self.body).
    # Other data is stored as other properties.
    def __init__(self,path,frameRate=25):
        '''Accepts a file path, differentiates between AAF and FILE_129 EDL formats and populates the EDL object using the file.'''
        # The following logic switches between AAC or FILE_129 options based on file extension.
        if path.lower().endswith('edl'):
            # Todo - some kind of edl checking for conformity helper function?
            self.title = helpers.importEdlTitle(path)
            self.body = helpers.importEdlBody(path,frameRate)
            self.fcm = helpers.importEdlFcm(path)
            self.length = len(self.body)
        elif path.lower().endswith('aaf'):
            # Todo
            pass
        else:
            raise ValueError('File provided not of accepted format. Please use FILE_129 EDLs or Avid AAFs.')
    
    def __str__(self):
        '''Returns string of the object'''
        return f'EDL object - Title: {self.title}, Length: {self.length} lines.'

    def __repr__(self):
        '''Returns representation of the object'''
        return f'EDL(title={self.title},length={self.length})'

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

def edlFileSearchCopy(list,searchpath,destination):
    # Todo
    # This function loops across "list" and searches "searchpath" for each file.
    # If it finds the file, it copies it to "destination"
    # This logic identifys any common spanned files, and copies the folder instea
    conventionalFiles = [] # Todo - fill in
    spannedFiles = [] # Todo - fill in
    i = 0
    while i < len(list):
        if True: # Todo - implament logic to decide if spanned or regular clip
            pass
        print(f'Searching file {i + 1} of {len(list) + 1}.')
        filePath = helpers.fileSearch(list[i],searchpath) # Todo - implement helper function
        if True: # Todo - implement sucess or failure report - cant find, unsupported file, no file name - continue on failutre - start log file! - helper function - implament checksum?
            pass 
        helpers.fileCopy(filePath,destination) # Todo - Implement copy function
    # Todo - return copy report

def edlDupeDetection(var):
    # Todo
    # Takes an arbitary number of EDLs, and lists any files used more than once.
    # Could also run in clip name mode as a secondary function?
    # Works by creating two lists. Every time it sees a file, it adds it to the first list. If it sees it a second time, adds it to the second list.
    # Use set to avoid using more than once?
    # Create some kind of comparison object - that also stores where the dupes are used?
    pass