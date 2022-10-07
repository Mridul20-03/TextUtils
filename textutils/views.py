
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    var = {'name':'Mridul','place':'India'}
    return render(request,'index.html',var)

def analyze(request):
    djtext=request.POST.get('text','default')

    #checkboxes values check
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')

    
    if removepunc=="on":
        punctuations='''!"#$%&'()*+-./:;<=>?@[\]^_`{|},~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removal of Punctuations','analyzed_text':analyzed}
        
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if fullcaps=="on":
            analyzed=djtext.upper()
            params={'purpose':'Conversion to Upper Case','analyzed_text':analyzed}
            djtext=analyzed
            #return render(request,'analyze.html',params)    

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed+char

        params={'purpose':'Removal of New Lines','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params={'purpose':'Removal of Extra Spaces from text','analyzed_text':analyzed}
        djtext=analyzed
       # return render(request,'analyze.html',params)

    if charactercounter=="on":
        analyzed+=("  No of characters in the text are: "+str(len(djtext)))
        print(analyzed)
        params={'purpose':' No of Character in text','analyzed_text':analyzed}
        #analyse the text
        #return render(request,'analyze.html',params)


    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charactercounter!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)