import string
import requests
import urllib

class TrieNode:
    def __init__(self,_character,_list,isLeaf):
        self._character=_character
        self._list=_list
        self.isLeaf=isLeaf

class RootNode:
    def __init__(self,rootMap):
        self.rootMap=rootMap

rootNode=RootNode({})
Zlist=[]
def setupWords(rootNode,wordList):
  for _word in wordList:
    currentNode=None
    nextNode=None
    wordLength=len(_word)
    if wordLength==1:    
      rootNode.rootMap[_word[0]].isLeaf=True
    else:
      for i in range(wordLength):
        if i==0:
          currentNode=rootNode.rootMap.get(_word[0])
          if currentNode is None:
            currentNode=TrieNode(_word[i],{},False)        
          rootNode.rootMap[_word[i]]=currentNode
          currentNode=rootNode.rootMap[_word[i]]        
        elif i==wordLength-1:        
          newNode=currentNode._list.get(_word[i])
          if newNode is None:
            temp=TrieNode(_word[i],{},True)
            currentNode._list[_word[i]]=temp
          else:
            newNode.isLeaf=True
            currentNode._list[_word[i]]=newNode                
          currentNode=currentNode._list[_word[i]]
        else:
          newNode=currentNode._list.get(_word[i])
          if newNode is None:
            temp=TrieNode(_word[i],{},False)
            currentNode._list[_word[i]]=temp
            currentNode=currentNode._list[_word[i]]          
          else:
            currentNode=currentNode._list[_word[i]]

def wordExists(word,rootNode):
  wordLength=len(word)
  currentNode=None
  #print(wordLength)
  if wordLength==1:
    nextNode=rootNode.rootMap.get(word[0])
    if nextNode is None:
      return False
    else:      
      currentNode=rootNode.rootMap[word[0]]
    return currentNode.isLeaf  
  else:
    for i in range(wordLength):      
      if i==0:
        newNode=rootNode.rootMap.get(word[i])
        if newNode is None:
          return False
        else:
          currentNode=newNode
      else:
        newNode=currentNode._list.get(word[i])
        if newNode is None:
          return False
        else:
          currentNode=newNode

      if i==wordLength-1:
        return currentNode.isLeaf


def AddData(_rootNode):
	content=urllib.request.urlopen('https://github.com/Ad1tyaV/pyTestFiles/blob/master/scrabbleWords.txt?raw=true')
	#print(content)
	wordList=[]
	for line in content:
	  text=line.decode('utf-8')
	  text=text.rstrip()
	  wordList.append(text.lower())
	#print(wordList)  
	#print(len(wordList))
	#print(wordList[:10])
	setupWords(_rootNode,wordList)

def getFirstNode(startChar,rootNode):
  Zlist.clear()
  currentNode=rootNode.rootMap.get(startChar)
  return currentNode

def getWordsStartWith(currentNode,res=""):    
  if currentNode.isLeaf:        
    res+=currentNode._character
    Zlist.append(res)
    #print(res)
    for _key in currentNode._list:
      getWordsStartWith(currentNode._list.get(_key),res)
  else:
    res+=currentNode._character
    for _key in currentNode._list:
      getWordsStartWith(currentNode._list.get(_key),res)


def getWordList():
  return Zlist
	
def testData(_rootNode):
	for x in _rootNode.rootMap:
	  testNode=_rootNode.rootMap.get(x)
	#print(testNode._character)  
	for p in testNode._list:
	  pass #print(testNode._list.get(p)._character)