from typing import Dict, List, Tuple
from collections import deque
import random
from memory_profiler import profile
def readTextFile(fName:str)->str:
    with open(fName, 'r') as f:
        lines = f.readlines()
    return " ".join(lines).replace('\n', "")

def makeDict(indexSize:int, baseText:str)->Dict[Tuple, List[str]]:
    wordList = baseText.split(" ")
    markovDict = {}
    key = wordList[:indexSize]
    for i in range(indexSize, len(wordList)):
        key = tuple(key)
        if key not in markovDict:
            markovDict[key] = []
        word = wordList[i]
        markovDict[key].append(word)
        key = deque(key)
        key.popleft()
        key.append(word)
    return markovDict

def generateText(maxNbWords:int, markovDict:Dict[Tuple, List[str]])->Tuple[str ,int]:
    result = []
    key = random.choice([k for k in markovDict.keys()])
    while len(result) < maxNbWords and key in markovDict:
        word = random.choice(markovDict[key])
        key = deque(key)
        key.append(word)
        key.popleft()
        key = tuple(key)
        result.append(word)
    return "".join(result), len(result)
        
def realText(maxMbWords:int, indexSize:int) -> str:
    txt = ""
    baseText = readTextFile("dataset.txt")
    markovDict = makeDict(indexSize, baseText)
    lenText = 0
    while lenText < maxMbWords:
        txt, lenText = generateText(maxMbWords, markovDict)
    return txt
    
if __name__== "__main__":
    print("2階")
    text = realText(100, 2)
    print(text)
    print("5階")
    text = realText(100, 5)
    print(text)