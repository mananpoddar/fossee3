from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee3.models import Caption,Documents
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import subprocess
import shutil
import ntpath
import os
ntpath.basename("/media/document/")
wdFormatPDF = 17


# argument: request 
# what it does:renders the front page 
# returns: returns the front page
def index(request):
    return render(request,"fossee3/index.html")


# argument: request 
# what it does:get's the file from user one by one through ajax requests,
#              saves it in the database
# returns: returns the page where user can upload the slides
@csrf_exempt
def uploadDocument(request):
    
    if request.method=="POST":
        fileUrl = request.FILES.get('Document') 
        
    
        caption = Caption(
        title = request.POST.get('title'),
        description = request.POST.get('description')
        )
        caption.save()
        # conversiontopdf(fileUrl)

        Document = Documents(
            document = request.FILES.get('Document')

        )
        Document.save()
        fileUrl = Document.document.url
        conversiontopdf(fileUrl)
  
    return render(request,"fossee3/uploadDocument.html")


# argument: request 
# what it does:gets all the documents from the database
# returns: returns the page rendering all these documents with viewer link to it
def viewDocument(request):
    print("viewDocument")
    caption = Caption.objects.all()[0]
    Document = Documents.objects.all()
    
    #saving pdf path to every object in document to render the pdf's
    for obj in Document:
        head, tail = ntpath.split('./'+str(obj.document) )
        tail = tail.split('.')[0] + '.pdf'
        obj.document = 'document/'+tail
        obj.save()
    return render(request,"fossee3/viewDocuments.html",{"caption":caption,"Document":Document})


# argument:path of the file
# what it does: since I was not able to find viewer for extensions other than pdf, 
#               I converted the files to pdf first and saved it in the database along 
#               with the original files, so that I can render all the files through the viewers
#               so,basically this function converts all the files to pdf and keep a copy of that as well in database     
# returns: doesn't return anything
def conversiontopdf(fileUrl):
    fileUrl = '.'+fileUrl
    head, tail = ntpath.split(fileUrl)
    tail = tail.split('.')[0] + '.pdf'
    src = tail
    dest = './media/document'
    output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf' ,fileUrl])
    try:
        shutil.move(src,dest)
    except:
        os.remove(src)
    

   

