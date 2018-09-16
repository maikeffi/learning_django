import os
import fpdf
from io import StringIO
from django.shortcuts import render
from django.http import HttpResponse
from subprocess import Popen,PIPE
from reportlab.pdfgen import canvas
# Create your views here.

def index(request):
    return render(request,'pyrunner/home.html')
def pyrunner(request):
    if request.method == 'POST':
        info = request.POST['info_name']
        output = runscript(info)
        '''response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename = "pythonoutput.pdf"'
        p = canvas.Canvas(response)
        p.drawString(100, 200, output)
        p.showPage()
        p.save()
        return response'''
    else:
        info = "failed"
        output = "failed"
    return render(request,"pyrunner/home.html",{
        'info': info,
        'output': output,
      })


def runscript(filepath):
    #output = subprocess.call(['python' ,filepath],shell=True)
    #process = Popen(['python',filepath],stdout=PIPE)
    #stdout, stderr = process.communicate()
    #print(stdout)
    pdf = fpdf.FPDF(format='letter')
    savepath = str(filepath).replace(".py",".pdf")
    pdf.add_page()
    pdf.set_font("Arial", size=8)
    with Popen(['python3',filepath], stdout=PIPE, bufsize=1,universal_newlines=True) as p, StringIO() as buf:
        for line in p.stdout:
            print(line, end='')
            buf.write(line)
            pdf.write(5,line)
        output = buf.getvalue()
    pdf.output(savepath)
    return savepath

