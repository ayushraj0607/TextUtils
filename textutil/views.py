from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')

    #check checkbox value
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')

    #check with checkbox is on
    if removepunc=='on':
        punctuations='''!()[]{}<>;:"',.~!@#$%^&*_-?/'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    
    if capitalize=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to UPPERCASE','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    
    if (newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if (char!="\n" and char!="\r"):
                analyzed=analyzed+char.upper()
        params={'purpose':'Removed New Line','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    
    if (spaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Removed Extra Space','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    
    if (charcount=='on'):
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1
        params={'purpose':'Counted character','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if(removepunc!='on' and capitalize!='on'and newlineremover!='on' and spaceremover!='on' and charcount!='on'):
        return HttpResponse("Error")
    

    return render(request,'analyze.html',params)