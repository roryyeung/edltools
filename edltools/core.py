# -*- coding: utf-8 -*-
from . import helpers
import os

class Edl:
    """
    This class stores the data about our EDL in a list of dicts format (self.body).
    Other data is stored as other properties.
    It also contains a number of methods allowing for manipulation of the object.
    """
    def __init__(self,path,frameRate=25):
        '''Accepts a file path, differentiates between AAF and FILE_129 EDL formats and populates the EDL object using the file.'''
        # The following logic switches between AAC or FILE_129 options based on file extension.
        if path.lower().endswith('.edl'):
            # Todo - some kind of edl checking for conformity helper function?
            self.title = helpers.importEdlTitle(path)
            self.frameRate = frameRate
            self.body = helpers.importEdlBody(path,frameRate)
            self.fcm = helpers.importEdlFcm(path)
            self.length = len(self.body)
        elif path.lower().endswith('.aaf'):
            # Todo
            pass
        else:
            raise ValueError('File provided not of accepted format. Please use FILE_129 EDLs or Avid AAFs.')
    
    def __str__(self):
        '''Returns string of the object'''
        return f'EDL object - Title: {self.title}, Frame Rate: {str(self.frameRate)}, Length: {self.length} lines.'

    def __repr__(self):
        '''Returns representation of the object'''
        return f'EDL(title={self.title},frameRate={self.frameRate},length={self.length})'

    def exportJson(self,path):
        # Todo
        pass

    def exportExcel(self,path,effects=False):
        # Todo
        if effects == False:
            body = helpers.dumpEffects(self.body)
            helpers.exportXls(body,path)
        else:
            body = self.body
            helpers.exportXls(body,path)
        pass

    def listClips(self):
        """
        This method iterates through the body object and generates a list of clip names.
        It ignores all effects and other non-clip items.
        It will raise a valueError should no clip names be found.
        """
        # Todo
        pass

    def listFiles(self):
        """
        This method iterates through the body object and generate a list of source files in the EDL.
        It raises a ValueError, should no source file names be found.
        """
        fileList = []
        for line in self.body:
            source = line.get('SOURCE FILE')
            fileList.append(source)
        # This checks if the list is empty and raises an error if so. It also removes "None" values.
        count = 0
        cleanedFileList = []
        for file in fileList:
            if file != None:
                cleanedFileList.append(file)
                count += 1
        if count == 0:
            raise ValueError('No source file names found - check these are selected on editing software.')
        return cleanedFileList
    
    def dumpEffects(self):
        self.body = helpers.dumpEffects(self.body)

class Ale:
    """
    This class stores the data associated with an ALE file, along with methods to manipulate the ALE object.
    """
    #
    def __init__(self,path,delim="tab"):
        """Accepts a path and optionally a delimiter, which defaults to tab."""
        if path.lower().endswith('.ale'):
            self.header = helpers.importAleHeader(path,delim)
            self.body = helpers.importAleBody(path,delim)
        else:
            raise ValueError('File provided not of accepted format. Please use Avid ALE.')
    
    def __str__(self):
        '''Returns string of the object'''
        return f'ALE object.'

    def __repr__(self):
        '''Returns representation of the object'''
        return f'ALE'

    def exportJson(self,path):
        # Todo
        pass

    def exportExcel(self,path):
        body = self.body
        helpers.exportXls(body,path)

    def listContentss(self):
        """
        This method iterates through the body object and generates a list of names of the contents (clips or clip-like objects,e.g. Timelines). It will raise a valueError should no clip names be found.
        """
        # Todo
        pass

    def listFiles(self):
        """
        This method iterates through the body object and generates a list of names of source file names of video clips. If this column is not present, raises an error.
        """
        # Todo
        if True: #Body contains column "Source File"
            pass
        else:
            pass

def edlFileSearchCopy(object,searchpath,destination,copy=False):
    """
    This function accepts an EDL or ALE object and searches the "searchpath" for each clip in the object.
    It can either output a list of file paths to the destination or copy each file in the list to the destination.
    It does not fail if it can't find a file, but instead creates a list of files it can't find.
    It generates a log for each copy, whilst providing progress updates on the console.
    Note: this will not follow symbolic links.
    """

    # TODO - UNTESTED BEYOND THIS POINT ===========================================================================

    # This logic checks the the input object is an ALE or EDL.
    if isinstance(object,Edl) == False and isinstance(object,Ale) == False:
        raise TypeError("Object is not an Edl or Ale")
    # We call the object's list of files
    fileList = object.listFiles()
    # Convenienly, the listFiles method will raise a value error if all contained within are of type None.
    
    # In this section, we will perform an OS.walk to go through the target drive.
    # Every time that a filename matches one on the list, it will add the location to our new list.
    dirList = []
    for dirpath, dirnames, filenames in os.walk(searchpath):
        # This case handles non-spanned files
        for filename in filenames:
            if filename in fileList or filename in os.path.splitext(filename)[0]: #Need to modify to consider extension - not in EDL nessassarily?
                address = os.path.join(dirpath, filename)
                dirList.append(address)
        # This case handles spanned files - UNSURE!!!!! ==================================================
        for dirname in dirnames:
            if dirname in fileList:
                address = os.path.join(dirpath, dirname)
                dirList.append(address)
    print(f"Search complete, {len(dirList)} files found.")
            

    ## TODO - implement copy function =======================================================================
    if copy == True:
        pass
        print(f"Copy complete - at path: {destination}.")

    ## TODO - return copy report ==========================================================================
    reportName = object.title
    reportPath = os.join(destination,reportName)
    with open(reportPath, 'w') as fp:
        for address in dirList:
            fp.write(address)
    print(f"Report complete - at path {destination}.")

def edlDupeDetection(var):
    # Todo
    # Takes an arbitary number of EDLs, and lists any files used more than once.
    # Could also run in clip name mode as a secondary function?
    # Works by creating two lists. Every time it sees a file, it adds it to the first list. If it sees it a second time, adds it to the second list.
    # Use set to avoid using more than once?
    # Create some kind of comparison object - that also stores where the dupes are used?
    pass