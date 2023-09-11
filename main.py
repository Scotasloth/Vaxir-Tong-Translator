import sys
import os
from tkinter import *
from PIL import ImageTk,Image
import pyodbc 

def main(data):

    
    root = Tk(className="Vaxir Tong Translator") 

    program_directory=sys.path[0]

    word = getWord()

    translation = translate(word)



def get_database():
    dataDict = {}
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pc\OneDrive\Documents\Programs\Python\Vaxir Tong Translator\Vaxir Tong.accdb;')
    cursor = conn.cursor()
    cursor.execute('SELECT English FROM main')

    keys = []
    val = []

    for row in cursor:
        new = str(row)

        keys.append(new)

    cursor.execute('SELECT Elder FROM main')

    for row in cursor:
        new = str(row)

        val.append(new)

    dataDict = {k: v for k, v in zip(keys, val)}
    #print(str(dataDict))
   
    return(dataDict)


def getWord():

    word = "('Hello',)"
    return word

def translate(word):

    elder = dict[word]
    print (elder)
    return elder



if __name__ == '__main__':
    dict = get_database()
    main(dict)