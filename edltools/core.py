# -*- coding: utf-8 -*-
from . import helpers

class Edl:
    def __init__(self,path):
        self.title = helpers.importEdlTitle(path)
        self.body = helpers.importEdlBody(path)
        self.fcm = helpers.importEdlFcm(path)
    
    def export_json(self,path):
        pass

    def export_excel(self,path,effects=False):
        if effects == False:
            body = helpers.dumpEffects(self.body)
        else:
            body = self.body
        pass