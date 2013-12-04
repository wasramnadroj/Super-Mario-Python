import pygame,os,sys,data,save
from pygame.locals import *

class Savefile(object):

    def __init__(self,filename='saves.txt'):
        self.filename = filename

    def readscore(self):
        with open(self.filename, "r") as f:
            for line in f:
                line = line.replace("\n","") # remove the trailing newline
                return line

    def writescore(self,score):
        open(self.filename,'w').write(str(score))

    def read(self): #CODE TAKEN FROM LECTURE NOTES
        saves = []
        temp = []
        with open(self.filename, "r") as f:
            for line in f:
                line = line.replace("\n","") # remove the trailing newline
                word = ''
                for char in xrange(len(line)):
                    if line[char] != '[' and line[char] != ']' and line[char] != ',' and line[char] != ' ':
                        word += line[char]
                    if line[char] == ',' or char+2 == len(line):
                        if word != '':
                            temp.append(word)
                        word = ''
                saves.append(temp)
                temp = []
        return saves

    def write(self,toon,level,lives,position,empty=False):
        if position == 1 and empty:
            lvl = '%s-%s' % ((level-1)/4+1,(level-1)%4+1)
            save = '['+toon+','+lvl+','+str(lives)+']\n[]\n[]'
            open(self.filename,'w').write(save)
        if position == 2 and empty:
            lvl = '%s-%s' % ((level-1)/4+1,(level-1)%4+1)
            save = '[]\n['+toon+','+lvl+','+str(lives)+']\n[]'
            open(self.filename,'w').write(save)
        if position == 3 and empty:
            lvl = '%s-%s' % ((level-1)/4+1,(level-1)%4+1)
            save = '[]\n[]\n['+toon+','+lvl+','+str(lives)+']'
            open(self.filename,'w').write(save)
        if position == 3 and not empty:
            saves = Savefile().read()
            lvl = '%s-%s' % ((level-1)/4+1,(level-1)%4+1)
            save1,save2 = '[]','[]'
            if saves[0] != []:
                save1 = '['+saves[0][0]+','+saves[0][1]+','+saves[0][2]+']'
            if saves[1] != []:
                save2 = '['+saves[1][0]+','+saves[1][1]+','+saves[1][2]+']'
            save = save1+'\n'+save2+'\n['+toon+','+lvl+','+str(lives)+']'
            open(self.filename,'w').write(save)
        if position == 2 and not empty:
            saves = Savefile().read()
            lvl = '%s-%s' % ((level-1)/4+1,(level-1)%4+1)
            save1,save2 = '[]','[]'
            if saves[0] != []:
                save1 = '['+saves[0][0]+','+saves[0][1]+','+saves[0][2]+']'
            if saves[2] != []:
                save2 = '['+saves[2][0]+','+saves[2][1]+','+saves[2][2]+']'
            save = save1+'\n['+toon+','+lvl+','+str(lives)+']'+'\n'+save2
            open(self.filename,'w').write(save)
        if position == 1 and not empty:
            saves = Savefile().read()
            lvl = '%s-%s' % ((level-1)/4+1,(level-1)%4+1)
            save1,save2 = '[]','[]'
            if saves[2] != []:
                save2 = '['+saves[2][0]+','+saves[2][1]+','+saves[2][2]+']'
            if saves[1] != []:
                save1 = '['+saves[1][0]+','+saves[1][1]+','+saves[1][2]+']'
            save = '['+toon+','+lvl+','+str(lives)+']'+'\n'+save1+'\n'+save2
            open(self.filename,'w').write(save)




#placeholder