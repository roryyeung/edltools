# -*- coding: utf-8 -*-
import timecode
import re

def importEdlTitle(filepath):
    """Helper function - extracts the title from an File129 formatted EDL and returns a string"""
    with open(filepath) as file:
        for line in file.readlines():
            if line.startswith("TITLE") == True:
                return line[6:].strip()

def importEdlFcm(filepath):
    """Helper function - extracts the title from an File129 formatted EDL and returns a string"""
    with open(filepath) as file:
        for line in file.readlines():
            if line.startswith("FCM") == True:
                return line[5:].strip()

def importEdlBody(filepath,frameRate=25):
    """Helper function - extracts the body from an File129 formatted EDL and returns a list of dicts"""
    body = []
    with open(filepath) as file:
        counter = -1
        for line in file.readlines():
            
            # This section of logic eliminates non-body lines
            if line.strip() == "":
                continue
            if line.startswith("TITLE") == True:
                continue
            if line.startswith("FCM") == True:
                continue
            if line.startswith("* =") == True:
                #This logic detects the end of section marker and breaks the read loop
                return body
            # This section changes between clip and effect lines on the EDL
            if line.startswith("*") == False:
                # This section addes clip lines to the EDL body
                counter = counter + 1
                clip = line.split()
                # This section converts timecode to timecode objects
                i = 0
                while i < len(clip):
                    if re.search("[0-9]:[0-9]:[0-9]:[0-9]",clip[i]):
                        clip[i] = Timecode(frameRate,clip[i])
                    i +=1
                body.append({"clip":clip})
            else:
                # This section adds effect lines to the EDL body
                line = line.strip("*")
                if ":" in line:
                    key, value = line.split(":")
                    value = value.strip()
                    body[counter][key] = value
                else:
                    continue
    return body

def dumpEffects():
    """Helper function - removes all effects (non-clip) lines from the EDL."""
    # Todo
    pass