from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee3.models import Caption,Documents
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

ini =0

# Create your views here.

def index(request):
    return render(request,"fossee3/index.html")


@csrf_exempt
def uploadDocument(request):
    if request.method=="POST":
        ini =0
        if ini == 0:
                caption = Caption(
                title = request.POST.get('title'),
                description = request.POST.get('description')
                )
                caption.save()
                ini =1
        Document = Documents(
            document = request.FILES.get('Document')

        )
        Document.save()
        print(Document.is_valid())
    return render(request,"fossee3/uploadDocument.html")

def viewDocument(request):
    print("viewDocument")
    caption = Caption.objects.all()[0]
    Document = Documents.objects.all()
    return render(request,"fossee3/viewDocuments.html",{"caption":caption,"Document":Document})