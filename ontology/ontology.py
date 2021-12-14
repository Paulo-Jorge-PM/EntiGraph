 #!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")

import re, pathlib, importlib, time, os

from . import tools
from sentimentAnalysis import sentiment

class Ontology():

    """
    Generates an ontology with ramifications of identified entities.

    Parameters:
        Example: ontology.Ontology(text="", source="Text", uri="http://sparql.entigraph.di.pt/corpus", properties={"id":"", "sourceUrl":""}, configs={"sourceLang":"pt", "skeleton":"", "sentimentAnalyze":False, "workFolder":"teste"})
        Mandatory: text (string of text or textes to be parsed and extracted the entities from).
        Important (with default values): mainClass (the name of the parent class, which will be automatically created; e.g. "Newspaper-Sol", "Comment", "Youtube" etc. usefull for filetering); workFolder (folder where all will be saved; note: if the folder and extractions exist, the script will add to them, use this to create new ones or update existing ones); id and sourceUrl are important for identification and link to the source material; if skeleton is not specified it will use the one in the app root folder; sourLang determines the folder used inside the list folder with the entities datasets (it accepts pt or en, but the en folder is just a clone of the pt one right now).

    Properties:
        The properties dicitonarie only has one mandatory pair: id. Any other pair will be dinamically generated and added to the entry ontology as one of its properties (in string type), allowing for flexibility.
    
    Returns:
        Saves the entities individuals in the folder name specified as workFolder in the save root folder (it uses timestamp for not rewriting). Use Iterate or Generate to compile and generate the final ontology.
    """

    def __init__(self, text="", mainClass="Text", uri="http://sparql.entigraph.di.pt/corpus", properties={"id":"", "sourceUrl":"", "timestamp":""}, configs={"sourceLang":"pt", "skeleton":"", "sentimentAnalyze":False, "workFolder":"teste"}):

        ### DATA
        self.text = text
        self.mainClass = mainClass
        self.uri = uri
        
        #CONFIGS
        self.workFolder = configs["workFolder"]
        #CONFIRM IF FOLDER ALREADY EXISTS OR CREATE IT
        self.mainFolder = pathlib.Path.cwd().joinpath('saves',self.workFolder)
        self.dataFolder = pathlib.Path.cwd().joinpath('saves',self.workFolder,'data')
        self.individualsFolder = pathlib.Path.cwd().joinpath('saves',self.workFolder,'data','individuals')
        os.makedirs(self.individualsFolder, exist_ok=True)
        
        if "skeleton" in configs:
            if configs["skeleton"] != "":
                self.skeleton = configs["skeleton"]
            else:
                self.skeleton = self.openSkeleton()
        else:
            self.skeleton = self.openSkeleton()
        #In case they use our skeleton and change the uri, do a replace:
        self.skeleton.replace("http://sparql.entigraph.di.pt/corpus", self.uri)    
            
        if "sourceLang" in configs:
            self.sourceLang = configs["sourceLang"]
        else:
            self.sourceLang = "pt"
            
        if "sentimentAnalyze" in configs:
            self.sentimentAnalyze = configs["sentimentAnalyze"]
        else:
            self.sentimentAnalyze = False
   
        if "workFolder" in configs:
            self.workFolder = configs["workFolder"]
        else:
            self.workFolder = "misc_"+str(time.time())
        
        
        self.properties = properties#Class properties to add
        #SET mandatory properties if not present
        if "id" in properties:#used for unique ID of the entry in the ontology
            self.id = properties["id"]
        else:
            self.id = str(time.time())
        self.properties["id"] = self.id

        self.individuals = {#Placeholder for the entities found in the text
        "animal":[],
        "city":[],
        "continent":[],
        "country":[],
        "otherPlace":[],
        "entity":[],
        "ethnicity":[],
        "keyword":[],
        "politicalParty":[],
        "religion":[],
        "weekday":[],
        "month":[],
        "footballClub":[],
        "brand":[],
        "carBrand":[],
        "sport":[],
        "tvChannel":[],
        "person":[],
        
        #Optional: list of dictionaries for identification of themes/subjects (similar to project Major Minors: 8 minorities were the 8 subjects)
        "subject":[],
        "priority":[],
        }

        self.sa = sentiment.SentimentAnalysis()
        
        
        for individualType in self.individuals:
            self.searchIndividuals(individualType)
        
        self.generateArticle()
    
    def searchIndividuals(self, individualType):
        if individualType not in ["priority", "subject"]:
            listImport = importlib.import_module(".lists."+self.sourceLang+"."+individualType, package="ontology")
            searchList = getattr(listImport, "data")
            for item in searchList:
                    #\b limita procura a terminação ou começo de palavra. Assim procurando p.e. por "arreiros", "Barreiros" não daria resultado.
                    pattern = r'\b' + re.escape(item) + r'\b'
                    try:
                        #try because if the item or body_text is empty it gives error. a if x and y would also work
                        if individualType in ["brand","politicalParty","tvChannel"]:#for case sensitive e.g. ONU , GNR etc.
                            search = re.search(pattern, self.text)
                        else:#all else case insensitive
                            search = re.search(pattern, self.text, flags=re.IGNORECASE)
                    except:
                        search = False
                    if search:
                        if individualType == "person":
                            self.generateIndividual(individualType, item, extra=searchList[item])
                        else:
                            self.generateIndividual(individualType, item)
        elif individualType == "subject":
            if "subject" in self.properties:
                for x in self.properties["subject"]:
                    self.generateIndividual("subject", x)
        elif individualType == "priority":
            if "priority" in self.properties:
                for x in self.properties["priority"]:
                    self.generatePriority(x, str(self.properties["priority"][x]))

    def generateIndividual(self, individualType, name, extra=None):
        name_filtered = tools.normalizeNonAlfanumerical(name)
        if individualType == 'person':
            line = '''
###  ''' + self.uri + '''#person-'''+name_filtered+'''
:person-'''+name_filtered+''' rdf:type owl:NamedIndividual ,
                               :Person ;'''
            if extra["job"]:
                line += '''
                      :job "'''+extra["job"]+'''"^^xsd:string ;'''
            if extra["wikiPage"]:
                line += '''
                      :wikiPage "'''+extra["wikiPage"]+'''"^^xsd:anyURI ;'''
            line += '''          
                      :personName "'''+name.strip()+'''"^^xsd:string .

            '''
        else:
            line = '''
###  ''' + self.uri + '''#'''+individualType+'''-'''+name_filtered+'''
:'''+individualType+'''-'''+name_filtered+''' rdf:type owl:NamedIndividual ,
                 :'''+individualType[0].upper()+individualType[1:]+''' ;
        :'''+individualType+''' "'''+name.strip()+'''"^^xsd:string .

            '''
        self.saveIndividual(individualType, line, individualType+"-"+name_filtered)
        self.individuals[individualType].append(individualType+"-"+name_filtered)


    def generateArticle(self):
        articleId = self.properties["id"]
        line = '''
###  ''' + self.uri + '''#article-'''+articleId+'''
:article-'''+articleId+''' rdf:type owl:NamedIndividual ,
                   :Article ;
                   :articleFrom :'''+ tools.normalizeNonAlfanumerical(self.mainClass).capitalize() +''' ;'''

        line += self.articleReferes("referesEntity",["entity"])
        line += self.articleReferes("referesKeyword",["keyword"])
        line += self.articleReferes("referesAnimal",["animal"])
        line += self.articleReferes("referesEthnicity",["ethnicity"])
        line += self.articleReferes("referesReligion",["religion"])
        line += self.articleReferes("referesPoliticalParty",["politicalParty"])
        line += self.articleReferes("referesCity",["city"])
        line += self.articleReferes("referesCountry",["country"])
        line += self.articleReferes("referesOtherPlace",["otherPlace"])
        line += self.articleReferes("referesMonth",["month"])
        line += self.articleReferes("referesContinent",["continent"])
        line += self.articleReferes("referesWeekday",["weekday"])
        
        line += self.articleReferes("referesFootballClub",["footballClub"])
        line += self.articleReferes("referesBrand",["brand"])
        line += self.articleReferes("referesCarBrand",["carBrand"])
        line += self.articleReferes("referesSport",["sport"])
        line += self.articleReferes("referesTvChannel",["tvChannel"])
        
        line += self.articleReferes("referesPerson",["person"])

           
        #DINAMICALY ADDED PROPERTIES   
        for property in self.properties:
            line += '''
           :'''+ str(property) +''' """'''+str(self.properties[property]).strip().replace('"',r'\"')+'''"""^^xsd:string ;
            '''
           
        if self.sentimentAnalyze==True:
            line += '''
           :sentimentAnalysis """'''+self.sa.sentiment(self.text)+'''"""^^xsd:string .

'''
        else:
            line += '''
           :sentimentAnalysis """"""^^xsd:string .

'''
            
        filePath = self.dataFolder.joinpath('individuals','article.txt')
        with open(filePath, "a+", encoding="utf-8") as file:
            file.write(line)
            
        #self.saveSkeleton()
        #self.generateOntology()
        print(">Entities extracted from id "+articleId+" and saved at:\n"+str(self.mainFolder))

    def articleReferes(self, referesX, individuals):
        line = ''
        c=0
        for individual in individuals:
            if self.individuals[individual] != []:
                if c == 0:
                    line = '''
                   :'''+referesX+''' '''
                    c+=1
                for entity in self.individuals[individual]:
                    if c>0:
                        line += '''
                        :'''+entity+''' ,'''
                    else:
                        line += ':'+entity+' ,'
        if c!=0:
            line = line[:-1]+";"
        return line

    def saveIndividual(self, individualType, line, searchFor):
        #filePath = pathlib.Path.cwd().joinpath('saves',self.workFolder,'individuals',individualType+'.txt')
        filePath = self.individualsFolder.joinpath(individualType+'.txt')
        try:
            with open(filePath, "r", encoding="utf-8") as file:
                data = file.read()
                search = re.search(searchFor, data)
        except:
            search = None
        if search == None:
            with open(filePath, "a+", encoding="utf-8") as file:
                file.write(line)

    def openSkeleton(self):
        sourceTemplate = pathlib.Path.cwd().joinpath("ontology_skeleton.ttl")
        with open(sourceTemplate, "r", encoding="utf-8") as file:
            skeleton = file.read()
        return skeleton


#if __name__ == '__main__':
#    main = Ontology()
