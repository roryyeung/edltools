# -*- coding: utf-8 -*-

def importEdlTitle(filepath):
    # Extracts the title from an File129 formatted EDL and returns a string
    with open(filepath) as file:
        for line in file.readlines():
            if line.startswith("TITLE") == True:
                return line[6:].strip()

def importEdlFcm(filepath):
    # Extracts the title from an File129 formatted EDL and returns a string
    with open(filepath) as file:
        for line in file.readlines():
            if line.startswith("FCM") == True:
                return line[6:].strip()

def importEdlBody(filepath):
    # Extracts the body from an File129 formatted EDL and returns a list of dicts
    body = []
    with open(filepath) as file:
        for line in file.readlines():
            counter = 0
            # This section of logic eliminates non-body lines
            if line.startswith("TITLE") == True:
                continue
            if line.startswith("FCM") == True:
                continue
            if line.startswith("* =") == True:
                #This logic detects the end of section marker and breaks the read loop
                break
            # This section changes between clip and effect lines on the EDL
            if line.startswith("*") != True:
                # This section addes clip lines to the EDL body
                counter += 1
                clip = line.split()
                body.append({"clip":clip})
            else:
                # This section adds effect lines to the EDL body
                line = line.strip("*")
                if len(line) > 2:
                    key, value = line.split(":")
                else:
                    continue
                value = value.strip()
                body[counter][key] = value
