#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, re, pathlib

from textblob import TextBlob
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer

#pip install googletrans
#Google Tradutor
#from googletrans import Translator

class SentimentAnalysis:

    def __init__(self, text='', model=False, lexFolder='SentiLex-PT02', lang="pt"):

        base_path = os.path.join(os.getcwd(), 'data', lexFolder)
        self.train = []
        self.wordsPT = []
        self.wordsPT_sentiments = []
        
        self.lang = lang
        self.model = model
        
        if model:
            self.cl = self.trainModel(base_path)
            #self.sentimentPT(text, self.model)
        #else:
        #    self.sentimentPtTranslator(text)
    
    def sentiment(self, txt):
        # Note: the pt Model=true is problematic, use the traanslation version instead with model=false
        if self.lang == "pt":
            if self.model == True:
                sa = self.sentimentPT(txt, self.cl)
            else:
                sa = self.sentimentPtTranslator(txt)
        elif self.lang == "en":
            sa = self.sentimentEn(txt)
        print("- Sentiment Analysis: " + str(sa))
        return str(sa)
        
    
    #Train Model
    def trainModel(self, base_path):
        c=0
        if base_path.split('/')[-1] == 'ReLi-Lex':

            files = [os.path.join(base_path, f) for f in os.listdir(base_path)]
            for file in files:
                t = 1 if '_Positivos' in file else -1
                with open(file, 'r', encoding='utf-8') as content_file:
                    content = content_file.read()
                    all = re.findall('\[.*?\]',content)
                    for w in all:
                        self.wordsPT.append((w[1:-1]))
                        self.wordsPT_sentiments.append(t)
                        self.train.append((w[1:-1], t))
                        c+=1
        elif base_path.split('/')[-1] == 'SentiLex-PT02':

            file = os.path.join(base_path, 'SentiLex-lem-PT02.txt')

            with open(file, 'r', encoding='utf-8') as content_file:
                for line in content_file.readlines():
                    word = re.match(r'.*\.', line).group().replace('.','')
                    polarity = re.sub(r'.*POL:N[0-9]=', '', line)
                    polarity = re.sub(r';.*', '', polarity).replace('\n','')
                    polarity = int(polarity)

                    self.wordsPT.append((word))
                    self.wordsPT_sentiments.append(polarity)
                    self.train.append((word, polarity))
                    c+=1

        cl = NaiveBayesClassifier(self.train)
        
        return cl

    #Sentiment Analysis with TextBlob
    def sentimentPT(self, text, cl):
        polarity = 0
        blob = TextBlob(text, classifier=cl)

        polarity = blob.classify()

        prob_dist = cl.prob_classify(text)
        #print((prob_dist.prob(1),prob_dist.prob(0),prob_dist.prob(-1)))

        return polarity

    #Sentiment Analysis with English Algorithm - Translation 1st - Not ideal, but english algorithm model is better
    def sentimentPtTranslator(self, text):
        sentence = TextBlob(text)
        
        try:
            en = sentence.translate(to='en', from_lang='pt')
            analyzer1 = TextBlob(str(en))
            polarity = analyzer1.sentiment.polarity
        except:
            print("SA failed")
            log='>>Translation failed for: ' + str(sentence)
            self.logError(log)
            polarity = '0'
        #googleTranslator = Translator()
        #enGoogle = googleTranslator.translate(text, dest='en', src='pt').text  
        #print(en)
        #print(enGoogle)
        return str(polarity)

        """analyzer2 = TextBlob(str(en), analyzer=NaiveBayesAnalyzer())
        classification = analyzer2.sentiment.classification
        print(classification)
        pos = analyzer2.sentiment.p_pos
        neg = analyzer2.sentiment.p_neg
        print(pos, neg)"""

    def sentimentEn(self, text):
        sentence = TextBlob(text)
        try:
            polarity = sentence.sentiment.polarity
        except:
            log='>>Translation failed for: ' + str(text)
            self.logError(log)
            polarity = '0'
        return str(polarity)

    def logError(self,log):
        print('Sentiment Analysis failed')
        logFile = pathlib.Path.cwd().joinpath('sentimentAnalysis','logs','translationFailed.txt')
        with open(logFile, "a+", encoding="utf-8") as file:
            file.write(log)
		
if __name__ == '__main__':
    textPT = "Odeio coisas verdes!"
    textEN = "I hate to eat green things!"
    sa = SentimentAnalysis(lang="pt")
    #main = SentimentAnalysis().sentiment(text)
    #main = SentimentAnalysis(text, model=True)
    result = sa.sentiment(textPT)
    print(result)
