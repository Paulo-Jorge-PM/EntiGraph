#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import iterate

#The name of the JSON file inside the "raw" folder (from the root dir of the app) to be iterated.
fileName = "Sol_extraction_portuguese_64.json"

#False is default, will only use the fileName. True to iterate all JSON files in the raw folder (from the root dir of the app). Note: leave the fileName empty, True will ignore it
allFolder = False

#Name of the folder where it will be saved inside the "saves" folder in the root dir. If the folder existis it will not delete it, but update with the new class or individuals
workFolder = "ontology8"

#the main Class of this extraction, e.g. Youtube, Newspaper-Guardian, Comment, etc. - Note: take notice of OWL/Turtle rules, don't use quotes for instance, avoid spaces and special symbols
mainClass = "Sol"

#Leave empty as it is to use the default ontology template (the one at root dir if it is a new ontology, or the skeleton inside the saves/workFolder/data folder if it is an update to an existing one), otherwise it will assume your skeleton template instead and ignore the default ones.
skeleton = ""

if __name__ == '__main__':
    iterate.Iterate(fileName=fileName, allFolder=allFolder, workFolder=workFolder, mainClass=mainClass, skeleton=skeleton, sentiment=False)
