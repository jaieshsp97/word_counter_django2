from django.http import HttpResponse
from django.shortcuts import render
import operator

def Home(request):
    return render(request,'homepage.html')

def Count(request):
    fulltext = request.GET['textinput']
    answer=len(fulltext.split())

    dict={}

    for word in fulltext.split():
        if word in dict:
            dict[word]=dict[word]+1
        else:
            dict[word]=1

    return render(request,'count.html',{'answer':answer,'dict':sorted(dict.items(),key=operator.itemgetter(1),reverse=True)})

def About(request):
    return render(request,'about.html')
