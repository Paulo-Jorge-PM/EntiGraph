#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re, os, time

from ontology import tools

def generate(savePath, skeleton, mainClass):
    
    savePath = savePath
    skeleton = skeleton
    mainClass = mainClass

    finalFile = ""
    person = ""
    priority = ""
    article = ""
    entities = ""

    skeleton = upateSkeleton(mainClass, skeleton)#add new mainClass if not have
    finalFile += skeleton
    
    path = savePath.joinpath("data", "individuals")

    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r', encoding="utf-8") as f: # open in readonly mode
            fileName = os.path.basename(f.name)
            data = f.read()
            if fileName == "article.txt":
                article += data
            elif fileName == "person.txt":
                person += data
            elif fileName == "priority.txt":
                priority += data
            else:
                entities += data

    finalFile += entities
    finalFile += person
    finalFile += priority
    finalFile += article

    saveFinal(finalFile, savePath)
    saveSkeleton(skeleton, savePath)
    
    print("\n>>> Done! Individuals assembled with the ontology skeleton.\nCheck the saves folder for the result.\nPress enter to exit")

def upateSkeleton(nameClass, skeleton):
    rdf2Insert = newClass(nameClass)
    insertAfter = r"""#################################################################
#    Object Properties
#################################################################"""
    search = re.search(r'' + rdf2Insert, skeleton)
    if not search:
        #needle = skeleton.find(insertAfter)
        needle = re.search(insertAfter, skeleton).span()[1]#span()[1] = end needle; span()[0] = start needle
        skeleton = skeleton[:needle] + rdf2Insert + skeleton[needle:]
    return skeleton
    
def newClass(nameClass):
    rdf = '''

###  http://sparql.entigraph.di.pt/corpus#'''+tools.normalizeNonAlfanumerical(nameClass)+'''
:'''+tools.normalizeNonAlfanumerical(nameClass)+''' rdf:type owl:Class .
'''
    return rdf
    
"""def getSkeleton():
    path = os.path.join(os.getcwd(), "ontology_skeleton.ttl")
    with open(path, 'r', encoding="utf-8") as f:
        data = f.read()
    return data"""

def saveFinal(data, savePath):
    try:#if 1st time it will not find file to replace
        doBackup(savePath)
    except:
        pass
    #timestap = time.time()
    #fileName = "ontology_"+str(countFilesAdnDirsInDir(savePath))+"_"+str(timestap)+".ttl"
    fileName = "ontology.ttl"
    path = savePath.joinpath(fileName)
    with open(path, 'w', encoding="utf-8") as f:
        f.write(data)

# Backup old ontology.ttl before replacing
def doBackup(savePath):
    timestap = time.time()
    backupDir = savePath.joinpath("backups")
    os.makedirs(backupDir, exist_ok=True)#make dir if not exist
    currentFile = savePath.joinpath("ontology.ttl")
    newName = "ontology_"+str(countFilesAdnDirsInDir(backupDir)+1)+"_"+str(timestap)+".ttl"
    # Move / Rename / Replace
    target = currentFile.replace(currentFile.parent / "backups" / newName)
    print("\n > Backup made: old ontology.tllf saved at backups folder")

def saveSkeleton(skeleton, saveFolder):
    savePath = saveFolder.joinpath("data", "ontology_skeleton.ttl")
    with open(savePath, "w+", encoding="utf-8") as file:
        file.write(skeleton)

#Used to number the ontology save name. Note: it starts zero, so increment + 1
def countFilesAdnDirsInDir(path):
    try:
        No_of_files = len(os.listdir(path))
        return No_of_files
    except:
        return 0
    
if __name__ == '__main__':
    main = generate()
