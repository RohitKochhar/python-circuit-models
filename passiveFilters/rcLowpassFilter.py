from .metricScale import MetricScale
from math import pi
from sigfig import round

class RCLowpassFilter():
    def __init__(self, o_Resistance=-1, o_Capacitance=-1):
        self.setResistance(o_Resistance)
        self.setCapacitance(o_Capacitance)
        self.setTimeConstant()

        self.i_SigFigs  = 3 # ToDo: Make this dynamic

        self.setCutoffFrequency()

    def setResistance(self, o_Input):
        self.f_Resistance   =   MetricScale(o_Input).f_Value

    def setCapacitance(self, o_Input):
        self.f_Capacitance  =   MetricScale(o_Input).f_Value

    def setTimeConstant(self):
        self.f_Tau  = self.f_Resistance*self.f_Capacitance

    def setCutoffFrequency(self):
        f_Pi    = MetricScale(pi).f_Value
        f_R     = self.f_Resistance
        f_C     = self.f_Capacitance

        f_Denominator   =   2*f_Pi*f_R*f_C

        self.f_CutoffFrequency  =   round((1/f_Denominator), sigfigs=self.i_SigFigs)

    def setDampingCoefficient(self):
        self.f_DampingCoefficient   = round(1/self.f_Tau, sigfigs=self.i_SigFigs)

    def setResonantFrequency(self):
        self.f_ResonantFrequency    = round(1/self.f_Tau, sigfigs=self.i_SigFigs)

o_RCLowpassFilter = RCLowpassFilter(o_Resistance="10k", o_Capacitance="318n")

