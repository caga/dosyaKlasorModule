import glob
import os
import re
from pathlib import Path

silmessage=False
silinenObje=Path()
yaratmessage=False

class Dosya:
    def __init__(self,pathNFileName):
        self.pathNFileName=Path(pathNFileName)
        self.fileName=str(pathNFileName).split("/")[-1]
        self.fileStrings=self.fileName.split(".")
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
    def isimDegistir(self,fileName):
        s=str(self.pathNFileName.parent)+"/"+fileName
        # self.pathNFileName.rename(s)
        self.__init__(s)
        print(self.fileName)
        # self.fileName=fileName
        # self.fileStrings=fileName.split(".")
        # self.SecondNameFlag=False
        # self.fileExtension=False
        # if len(self.fileStrings)==3:
        #     self.SecondNameFlag=True
        #     self.fileExtension=True
        #     self.fileFirstName=self.fileStrings[0]
        #     self.fileSecondName=self.fileStrings[1]
        #     self.fileExtension=self.fileStrings[2]
        # if len(self.fileStrings)==2:
        #     self.fileExtension=True
        #     self.fileFirstName=self.fileStrings[0]
        #     self.fileExtension=self.fileStrings[1]
        # if len(self.fileStrings)==1:
        #     self.fileFirstName=self.fileStrings[0]
    def sil(self):
        global silmessage
        global silinenObje
        # silmessage=self.pathNFileName
        silmessage=True
        silinenObje=self.pathNFileName
        self.pathNFileName.unlink()
        returnString="silinen dosya: "+str(silinenObje)
        return returnString
    def yaz(self,String):
        self.pathNFileName.write_text(String)
    def oku(self):
        return self.pathNFileName.read_text()
        

    def __str__(self):
        s=self.fileName
        return s
    def __repr__(self):
        return "Dosya Nesnesi: {}".format(self.fileName)
class Klasor:
    def __init__(self,path):
        self.path=Path(path)
        self.__dosyaListesi=self.dosyalar(initial=True) 
        self.__klasorListesi=self.klasorler(initial=True)
    def dosyalar(self,initial=None):
        global silmessage
        global silinenObje
        global yaratmessage
        dosyaListesi=[Dosya(dosya) for dosya in self.path.iterdir() if dosya.is_file()]
        if initial or silmessage or yaratmessage :
            self.__dosyaListesi=[Dosya(dosya) for dosya in self.path.iterdir() if dosya.is_file()]
            silmessage=False
            yaratmessage=False
        return self.__dosyaListesi
    def klasorler(self,initial=None):
        global silmessage
        global yaratmessage
        if initial or silmessage or yaratmessage:
            self.__klasorListesi=[Klasor(str(altKlasor)) for altKlasor in self.path.iterdir() if altKlasor.is_dir()]
            silmessage=False
            yaratmessage=False
        return self.__klasorListesi
    def dosyaSil(self,fileName):
        path2File=Path()
        path2File=self.path / fileName
        p = [dosya for dosya in self.__dosyaListesi if path2File==dosya.pathNFileName][0]
        p.sil()
    def dosyaYarat(self,fileName):
        global yaratmessage
        path2File=Path()
        path2File=self.path / fileName
        path2File.touch()
        yaratmessage=True
        
        # print(path2File)
        # print(path2File.exists())
        
    def __str__(self):
        global silmessage
        if silmessage:
            self.__init__()
            silmessage=False
        s="Klasor: {}\n dosyaListesi: {}\n klasorListesi: {}".format(self.path,self.__dosyaListesi,self.__klasorListesi)
        return s
    def __repr__(self):
        global silmessage
        if silmessage:
            self.__init__()
            silmessage=False
        return "Klasor Nesnesi: {}".format(self.path)
