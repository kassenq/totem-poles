'''
Created on Sep 20, 2018

@author: kassen
'''

def isVowel(ch):
    if ch =='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        return True;
    else:
        return False
#OR
def isVowel2(ch):
    lst = ['a', 'e', 'i', 'o', 'u']
    if ch in lst:
        return True
    return False
def isVowel3(ch):
    return ch in 'aeiouAEIOU'

def ranking(desserts, searching):
    currRank = 1
    for i in range(len(desserts)):
        

if __name__ == '__main__':
    print (isVowel3('y'));
    
    
    # set variable before loop
    # change variable within loop 