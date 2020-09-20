from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from . import trieInit
import re
import json

# Create your views here.

firstRun=True
rootNode=None

def initializeTrie(request):    
    global firstRun
    global rootNode
    if firstRun:
        rootNode=trieInit.RootNode({})
        trieInit.AddData(rootNode)
        firstRun=False
    availableURLs={"Instructions":{"Check for a word's existence":request.get_host()+"/checkWord/<word>","Check letters starting with":request.get_host()+"/startLetter/<letter>"}}
    return JsonResponse(availableURLs)

def checkForWord(request,word):
    global rootNode
    global firstRun
    word=word.lower()
    wordLength=len(word)
    if wordLength>15 or wordLength==0:
        return JsonResponse({"Error":"Invalid Word"})
    else:
        pattern=re.compile("^([a-z]+)$")
        if pattern.match(word):
            if firstRun:
                initializeTrie(request)
            return JsonResponse({word:trieInit.wordExists(word,rootNode)})
        else:
            return JsonResponse({"Error":"Invalid Word"})                
    #return HttpResponse(trieInit.wordExists('testing',rootNode))

def wordStartsWithLetter(request,letter):
    pattern=re.compile("[a-z]")
    letter=letter.lower()
    global rootNode
    global firstRun
    if len(letter)>1 or len(letter)==0:
        return JsonResponse({"Error":"Enter exactly one letter"})
    if not pattern.match(letter):
        return JsonResponse({"Error":"Enter valid start letter!"})
    else:        
        if firstRun:
            initializeTrie(request)
        currentNode=trieInit.getFirstNode(letter,rootNode)
        trieInit.getWordsStartWith(currentNode,"")
        return JsonResponse({letter:(trieInit.getWordList())})


def handler404(request,exception):
    return JsonResponse({"Instructions":{"Check for a word's existence":request.get_host()+"/checkWord/<word>","Check letters starting with":request.get_host()+"/startLetter/<letter>"}})
