from django.shortcuts import render

from filterdesigner.models import RCLowPass

from filterdesigner.forms import RCLowPassForm

# Create your views here.
def index(request):
    a_Filters   = [[RCLowPass.s_ImgUrl, RCLowPass.s_UrlString]]
    print(a_Filters)
    ctx = {
        "a_Filters": a_Filters
    }
    return render(request, 'filterdesigner/index.html', ctx)

def RCLowPassDetail(request):
    return render(request, 'filterdesigner/filterDetail.html')

def createRCLowPassFilter(request):
    if request.method == 'POST':
        o_Form  = RCLowPassForm(request.POST)
        if o_Form.is_valid():
            return HttpResponseRedirect('/thanks/')
        
    else:
        o_Form = RCLowPassForm()

    ctx ={
        "o_Form": o_Form
    }

    return render(request, 'filterdesigner/filterDetail.html', ctx)