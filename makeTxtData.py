from typing import List
import re
import MeCab
def readTxt(fName: str)->List[str]:
    with open(fName, 'r', encoding='cp932') as f:
        lines = f.readlines()
    return lines

def cutUselessWords(lines:List[str])->List[str]:
    #ヘッダーとフッター削除
    lines = lines[17:-14]
    # 記号を削除
    outputList = []
    for line in lines:
        line = line.replace('\u3000', '').replace('|', '')
        line = re.sub(r'《.+?》|［＃.+?］', "", line)
        outputList.append(line)
    return outputList

def wakatiTxt(txtList:List[str])->List[str]:
    outputList = []
    # MeCabで分かち書きする
    wakati = MeCab.Tagger("-Owakati")
    for txt in txtList: outputList.append(wakati.parse(txt))
    return outputList
        
def outputFile(txtList:List[str]):
    with open("dataset.txt", 'w', encoding='utf-8') as f:
        f.writelines(txtList)
def makeTxtData(fName:str):
    lines = readTxt(fName)
    outputList = cutUselessWords(lines)
    outputList = wakatiTxt(outputList)
    outputFile(outputList)

if __name__ == "__main__":
    txtFile = "gingatetsudono_yoru.txt"
    makeTxtData(txtFile)
