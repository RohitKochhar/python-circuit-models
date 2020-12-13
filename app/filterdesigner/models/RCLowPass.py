from django.db import models
from django.db.models.signals import post_init
from filterdesigner.models import Number
from math import pi
from sigfig import round

class RCLowPass(models.Model):
    # Model Constants -----------------
    s_ImgUrl    = "https://github.com/RohitKochhar/spyce/blob/main/images/RCLowPass.png?raw=true"
    s_UrlString = "rc-low-pass"

    # Model Variables- ----------------
    s_Resistance    = models.CharField(max_length=15)
    s_Capacitance   = models.CharField(max_length=15)

    i_SigFigs       = 3

    def setResistance(self):
        self.f_Resistance   =   Number(s_Input=self.s_Resistance).f_Value

    def setCapacitance(self):
        self.f_Capacitance  =   Number(s_Input=self.s_Capacitance).f_Value 

    def setCutoffFrequency(self):
        f_Pi        = Number(s_Input=pi).f_Value
        f_R         = self.f_Resistance
        f_C         = self.f_Capacitance
        self.f_CutoffFrequency  = round(1/(2*f_Pi*f_R*f_C), sigfigs=self.i_SigFigs)

    def setTimeConstant(self):
        self.f_TimeConstant     = round(self.f_Resistance*self.f_Capacitance, sigfigs=self.i_SigFigs)

    def setDampingCoefficient(self):
        self.f_DampingCoefficient   = round(1/self.f_TimeConstant, sigfigs=self.i_SigFigs)

    def setResonantFrequency(self):
        self.f_ResonantFrequency    = round(1/self.f_TimeConstant, sigfigs=self.i_SigFigs)

    def setTransferFunction(self):
        self.s_Numerator     = f"{self.f_DampingCoefficient}"
        self.s_Denominator   = f"s+{self.f_ResonantFrequency}"
        self.s_TransferFunction =   f"{self.s_Numerator}/({self.s_Denominator})"
    
def RCLowPassConstructor(**kwargs):
    o_RCLowPass     = kwargs.get('instance')
    o_RCLowPass.setResistance()
    o_RCLowPass.setCapacitance()
    o_RCLowPass.setCutoffFrequency()
    o_RCLowPass.setTimeConstant()
    o_RCLowPass.setDampingCoefficient()
    o_RCLowPass.setResonantFrequency()
    o_RCLowPass.setTransferFunction()

post_init.connect(RCLowPassConstructor, RCLowPass)