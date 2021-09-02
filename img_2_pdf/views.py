from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from img_2_pdf.forms import pdfImageUpload
import os
from .models import pdfImage
from fpdf import FPDF
# Create your views here.
def index(request):
    form = pdfImageUpload(request.POST or None)
    if request.method == 'POST':
        form = pdfImageUpload(request.POST ,request.FILES)
        files=request.FILES.getlist('imag')
        if form.is_valid():
             for f in files:
                 file_instance = pdfImage(imag=f)
                 file_instance.save()


        path="C:/yadav/Ultra/media/pdfs/"
        imageList=os.listdir(path)
        imageList.sort()
        pdf = FPDF("P","mm","A4")
        x=0
        y=0
        w=310
        h=297

        for image in imageList:
            exclude=[".tif","Ink"]
            if image in exclude:
                continue
            
            else:
                pdf.add_page()
                pdf.image(path+image,20,120,170)
                print('pdf page created....')
        # pdf.(50,50,"Powered By DjangoApps.com")
        



        pdf.output("C:/yadav/Ultra/media/output.pdf",'F')
        yes=1
        return render(request,'pdf2.html',{'yes' : yes})

    folder = 'C:/yadav/Ultra/media/pdfs/'
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

       
        
    return render(request,'pdf.html',{'form':form})

    # return HttpResponse('<h2>Success</h2>')