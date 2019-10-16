#!/usr/bin/python
import glob
import os
import re
from pathlib import Path

class Dosya(Path):
    def __init__(self,fileName):
        self.fileName=fileName
        self.fileStrings=fileName.split(".")
        self.SecondNameFlag=False
        self.fileExtension=False

        if len(self.fileStrings)==3:
            self.SecondNameFlag=True
            self.fileExtension=True
            self.fileFirstName=self.fileStrings[0]
            self.fileSecondName=self.fileStrings[1]
            self.fileExtension=self.fileStrings[2]
        if len(self.fileStrings)==2:
            self.fileExtension=True
            self.fileFirstName=self.fileStrings[0]
            self.fileExtension=self.fileStrings[1]
        if len(self.fileStrings)==1:
            self.fileFirstName=self.fileStrings[0]
        print (self.fileStrings)
        print (len(self.fileStrings))
    def uzantiDegistir(self,extension):
        self.fileExtension=extension
    def isimDegistir(self,fileName):
        self.fileName=fileName
        self.fileStrings=fileName.split(".")
        self.SecondNameFlag=False
        self.fileExtension=False
        if len(self.fileStrings)==3:
            self.SecondNameFlag=True
            self.fileExtension=True
            self.fileFirstName=self.fileStrings[0]
            self.fileSecondName=self.fileStrings[1]
            self.fileExtension=self.fileStrings[2]
        if len(self.fileStrings)==2:
            self.fileExtension=True
            self.fileFirstName=self.fileStrings[0]
            self.fileExtension=self.fileStrings[1]
        if len(self.fileStrings)==1:
            self.fileFirstName=self.fileStrings[0]

    def __str__(self):
        s=self.fileName
        return s
    def __repr__(self):
        return "Dosya Nesnesi: {}".format(self.fileName)
class Klasor:
    def __init__(self,path):
        self.path=Path(path)
        self.dosyaListesi=self.dosyaListesi() 
        self.klasorListesi=self.altKlasor()
    def dosyaListesi(self):
        # dosyaListesi=[]
        dosyaListesi=[Dosya(str(dosya).split("/")[-1]) for dosya in self.path.iterdir() if dosya.is_file()]
        # for file in self.path.glob('*'): 
            # dosyaListesi.append(Dosya(str(file)))
        return dosyaListesi
    def altKlasor(self):
        klasorListesi=[altKlasor for altKlasor in self.path.iterdir() if altKlasor.is_dir()] 
        return klasorListesi
        
        
        


