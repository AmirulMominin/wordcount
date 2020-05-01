from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,"home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    x = len(fulltext)
    words = fulltext.split(" ")
    y = len(words)
    x = len(fulltext)

    wordslist = {}

    for word in words:
        if word in wordslist:
            wordslist[word] += 1
        else:
            wordslist[word] = 1

    final = sorted(wordslist.items(),key=operator.itemgetter(1), reverse = True)
    return render(request,"count.html",{"fulltext":fulltext,"length":y,"word":y,"wordslist":final})

def about(request):
    return render(request,"about.html/")
