from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html' )
    #return HttpResponse('''<h1>hello broo</h1> <a href="https://www.youtube.com/watch?v=HZVMNMuXDtI&list=RDHZVMNMuXDtI&start_radio=1"> Dum dee dee Dum </a>''')

def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    #check which checkboxis on
    if removepunc == "on":
        analysed = ""
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''

        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Remove Punctuations', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if(fullcaps == "on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Change to Upper Case', 'analysed_text': analysed}
        djtext = analysed
       # return render(request, 'analyse.html',params)
    if (newlineremover == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analysed = analysed + char.upper()
        params = {'purpose': 'remove new line', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on"):
        return HttpResponse("Error")

    return render(request,'analyse.html',params)
