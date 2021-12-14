#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib, json

from ontology import ontology

import generate

"""
Module Docstring
"""

__author__ = "Paulo PM"
__email__ = "paulo.jorge.pm@gmail.com"
__version__ = "0.1.0"
__license__ = "MIT"

class Iterate:

    def __init__(self, fileName="", allFolder=False, workFolder="ontology1", mainClass="", skeleton="", sentiment=False):
		
        self.fileName = fileName
        self.allFolder = allFolder
        self.workFolder = workFolder#save folder - it will create it or update it adding new individuas if exist
        self.mainClass = mainClass#Main class name for this entry (it will add it to the ontology skeleton if not exist)
        self.sentiment = sentiment
        
        self.saveFolder = pathlib.Path.cwd().joinpath('saves', self.workFolder)
        if skeleton != "":
            self.skeleton = skeleton
        else:
            self.skeleton = self.openSkeleton()
        
        self.count = 1
        
        if allFolder != True:
            self.startExtraction(self.fileName, self.mainClass, self.workFolder, self.skeleton)
        else:
            for filePath in pathlib.Path.cwd().joinpath("raw", self.fileName):
                print(str(filePath))
        
        #SAVE AND ASSEMBLE in the folder ./saves/"workFolder"/
        self.generateOntology()
        
        
    def startExtraction(self, fileName, mainClass, workFolder, skeleton):
        data = self.openFile(fileName)
        js = self.loadJson(data)
        sourceUrl = js["header"]["url"]
        for i in js['commentThread']:
            print("#"+str(self.count), end=": ")
            self.count+=1
            comment = i["commentText"]
            timestamp = i["timestamp"]
            user = i["user"]
            id = i["id"]
            ontology.Ontology(text=comment, mainClass=mainClass, properties={"id":id, "sourceUrl":sourceUrl, "timestamp":timestamp, "user":user, "text":comment, "type":"comment", "source":"Sol64"}, configs={"skeleton":skeleton, "workFolder":workFolder, "sentimentAnalyze":self.sentiment})
            


    def loadJson(self, file):
        js = json.loads(file)
        return js

    def openFile(self, fileName):
        filePath = pathlib.Path.cwd().joinpath("raw", fileName)
        with open(filePath, "r", encoding="utf-8") as file:
            data = file.read()
        return data

    def openSkeleton(self):
        ### If folder already exist with skeleton use it instead (could have new class's or different template from the base one)
        targetSkeleton = self.saveFolder.joinpath("data", "ontology_skeleton.ttl")
        if targetSkeleton.is_file():
            with open(targetSkeleton, "r", encoding="utf-8") as file:
                skeleton = file.read()
            return skeleton
        else:
            sourceTemplate = pathlib.Path.cwd().joinpath("ontology_skeleton.ttl")
            with open(sourceTemplate, "r", encoding="utf-8") as file:
                skeleton = file.read()
            return skeleton

    def generateOntology(self):
        generate.generate(savePath=self.saveFolder, skeleton=self.skeleton, mainClass=self.mainClass)




    

    
if __name__ == '__main__':
	main = Iterate()
