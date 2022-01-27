import math
import os
def letterChecker(string):
    vowelCounter = 0
    consonantCounter = 0
    vowels = "AaEeIiOoUu"
    for x in string:
        if x in vowels:
            vowelCounter=vowelCounter+1
        else:
            consonantCounter=consonantCounter+1
    if vowelCounter > consonantCounter:
        return "True"
    if vowelCounter < consonantCounter:
        return "False"
    if vowelCounter == consonantCounter:
        return "None"
def cylinderVolume(h,r):
    volume=math.pi*h*r*r
    return volume
def stringListCombiner(stringList):
    stringListCombined=",".join(stringList)
    return stringListCombined
#def nestedListToCSV():

#def CSVtoNestedList():

def divisionWithWarning(m,n):
    try:
        o=m/n
        return o
    except ZeroDivisionError:
        return "Error"
def duplicateRemover(integerList):
    integerSet=set(integerList)
    return integerSet
def createFolder():
    if not os.path.exists("/mnt/c/Windows/system32/hw3/hw3-folder"):
        os.mkdir("/mnt/c/Windows/system32/hw3/hw3-folder")
        return "hw-3 has been created"
    else:
        return "hw-3 already exists"
print(letterChecker("Ukulele"))
print(letterChecker("Banjo"))
print(cylinderVolume(2,3))
print(divisionWithWarning(2,1))
print(divisionWithWarning(2,0))
print(duplicateRemover([1,1,2,3,4,5,5]))
print(createFolder())