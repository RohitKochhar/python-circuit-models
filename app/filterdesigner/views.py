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

def RCLowPassFilterDetail(request):
    o_Form      = RCLowPassForm()
    a_Results   = -1
    if request.method == 'POST':
        o_Form = RCLowPassForm(request.POST)
        if o_Form.is_valid():
            o_RCLowPassFilter   = RCLowPass(
               s_Resistance=o_Form["s_ResistorValue"].value(),
               s_Capacitance=o_Form["s_CapacitorValue"].value()    
            )
            a_Results   = [o_RCLowPassFilter.f_Resistance, o_RCLowPassFilter.f_Capacitance, o_RCLowPassFilter.f_CutoffFrequency, o_RCLowPassFilter.f_TimeConstant, o_RCLowPassFilter.f_DampingCoefficient, o_RCLowPassFilter.f_ResonantFrequency, o_RCLowPassFilter.s_TransferFunction]

    ctx = {
        "o_Form":       o_Form,
        "a_Results":    a_Results
    }

    return render(request, "filterdesigner/RCLowPassFilterDetail.html", ctx)
            