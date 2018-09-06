from django.shortcuts import render
from django.http import HttpResponse
from subprocess import Popen,PIPE
# Create your views here.

def index(request):
    return render(request,'pyrunner/home.html')
def pyrunner(request):
    if request.method == 'POST':
        info = request.POST['info_name']
        output = runscript(info)
        print(info)
    else:
        info = "failed"
        output = "failed"
    return render(request,"pyrunner/home.html",{
        'info': info,
        'output': output,
      })

def runscript(filepath):
    #output = subprocess.call(['python' ,filepath],shell=True)
    process = Popen(['python',filepath],stdout=PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
    return stdout