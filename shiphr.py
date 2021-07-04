import random
def Mainmenu():
   inpt = ""
   print("  1 - Encrypt\n  2 - Decrypt\n  3 - Finish")
   inpt = input()
   if inpt == "1":
        modeone()
        Mainmenu()
   elif inpt == "2":
        modetwo()
        Mainmenu()
   elif inpt == "3":
        print("Finish")
   else:
        Mainmenu()  
def RANDOMKEY():
    alphabet = list("!,.)(/*-+=?:;/1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")# len 143
    out =''.join(random.sample(alphabet,3))    
    return out
def SEARCHKEY(word):
    out =[]
    for t in range(3):
        out.insert(t*-1, word[len(word)-t-1])
    return(out) 
def deshiphrovka(word,key):
    alphabet = list("!,.)(/*-+=?:;/1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    out = ""
    wi = []
    ki = []
    for j in range(len(word)-3):
        wi.insert(j, alphabet.index(word[j]) ) 
    for i in range(len(key)):
        ki.insert(i, alphabet.index(key[i]) ) 
    for q in range(len(wi)):
        out += alphabet[((wi[q]-ki[q%3])+286)%143]    
    print(out)
def shiphrovka(word, key):
    alphabet = list("!,.)(/*-+=?:;/1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    out = ""
    wi = []
    ki = []
    for j in range(len(word)):
        wi.insert(j, alphabet.index(word[j]) ) 
    for i in range(len(key)):
        ki.insert(i, alphabet.index(key[i]) )        
    for q in range(len(wi)):
        out += alphabet[(wi[q]+ki[q%3])%(143)]
    out += ''.join(key) 
    print(out)
def modeone():
    print("Enter text:")
    inpt = input()
    k = RANDOMKEY()
    shiphrovka(list(inpt),list(k))
def modetwo():
    print("Enter text:")
    inpt = input()
    k = SEARCHKEY(inpt)
    deshiphrovka(list(inpt),list(k))
Mainmenu()