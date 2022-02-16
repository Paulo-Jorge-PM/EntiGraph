#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, pathlib, json

from ontology import ontology

import generate

"""
Module Docstring
"""

__author__ = "Paulo PM"
__email__ = "paulo.jorge.pm@gmail.com"
__version__ = "0.1.0"
__license__ = "MIT"

SCRIPT_DIR = pathlib.Path(__file__).resolve(strict=True).parent

class Iterate:

    def __init__(self, filePath=None, allFolder=False, workFolder="ontology1", mainClass="", skeleton=None, sourceLang="en", sentiment=False, json=None, fieldColumns=None):
		
        self.filePath = filePath
        self.allFolder = allFolder
        self.workFolder = workFolder#save folder - it will create it or update it adding new individuas if exist
        self.mainClass = mainClass#Main class name for this entry (it will add it to the ontology skeleton if not exist)
        self.sentiment = sentiment
        self.sourceLang = sourceLang
        
        self.fieldColumns = fieldColumns
        
        self.saveFolder = SCRIPT_DIR.joinpath('saves', self.workFolder)
        
        self.skeleton = self.openSkeleton(newSkeleton=skeleton)
        
        self.json = json
        
        self.count = 1
        
        if allFolder != True:
            self.startExtraction(self.filePath, self.mainClass, self.workFolder, self.skeleton, self.json)
        else:
            print("Multiple file iterator not yet implemented. Run only one at a time.")
            #for filePath in SCRIPT_DIR.joinpath("raw", self.filePath):
            #    print(str(filePath))
        
        #SAVE AND ASSEMBLE in the folder ./saves/"workFolder"/
        self.generateOntology()
        
        
    def startExtraction(self, filePath, mainClass, workFolder, skeleton, js):
        if js:#JS can be used only in CLI. In GUI it asks for a file always
            data = js
        else:
            data = self.openFile(filePath)
        js = self.loadJson(data)
        #sourceUrl = js["header"]["url"]
        #Iterate over JS according to schema in fieldColumns. Empty fields will be written, and non existent fields will continue the same
        for item in js:
            fieldColumns = json.loads(self.fieldColumns)
            print("\n> Extraction #"+str(self.count)+"/"+str(len(js)))
            print('> Content: """' + str(item) +'"""')
            self.count+=1
            for key in fieldColumns:
                if key in item:
                   fieldColumns[key] = str(item[key])
            ontology.Ontology(text=fieldColumns["text"], mainClass=mainClass, properties=fieldColumns, configs={"skeleton":skeleton, "workFolder":workFolder, "sourceLang": self.sourceLang, "sentimentAnalyze":self.sentiment})

        """for i in js['commentThread']:
            fieldColumns = self.fieldColumns
            print("\n> Extraction #"+str(self.count)+"/"+str(len(js['commentThread'])))
            print('- Text: """' + i["commentText"] +'"""')
            self.count+=1
            comment = i["commentText"]
            timestamp = i["timestamp"]
            user = i["user"]
            id = i["id"]
            ontology.Ontology(text=comment, mainClass=mainClass, properties={"id":id, "sourceUrl":sourceUrl, "timestamp":timestamp, "user":user, "text":comment, "type":"post", "source":"hiperfolio"}, configs={"skeleton":skeleton, "workFolder":workFolder, "sourceLang": self.sourceLang, "sentimentAnalyze":self.sentiment})"""
            


    def loadJson(self, file):
        js = json.loads(file)
        return js

    def openFile(self, filePath):
        #filePath = SCRIPT_DIR.joinpath("raw", filePath)
        with open(filePath, "r", encoding="utf-8") as file:
            data = file.read()
        return data

    def openSkeleton(self, newSkeleton=None):
        ### If folder already exist with skeleton use it instead (could have new class's or different template from the base one)
        targetSkeleton = self.saveFolder.joinpath("data", "ontology_skeleton.ttl")
        if targetSkeleton.is_file():
            with open(targetSkeleton, "r", encoding="utf-8") as file:
                skeleton = file.read()
            return skeleton
        else:
            if newSkeleton:
                sourceTemplate = newSkeleton
            else:
                sourceTemplate = SCRIPT_DIR.joinpath("ontology_skeleton.ttl")
            with open(sourceTemplate, "r", encoding="utf-8") as file:
                skeleton = file.read()
            return skeleton

    def generateOntology(self):
        generate.generate(savePath=self.saveFolder, skeleton=self.skeleton, mainClass=self.mainClass)




    

    
if __name__ == '__main__':
	main = Iterate()
