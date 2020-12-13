from .metricScale import MetricScale

class RCLowpassFilter():
    def __init__(self, o_Resistance=-1, o_Capacitance=-1):
        self.setResistance(o_Resistance)
        self.setCapacitance(o_Capacitance)

    def setResistance(self, o_Input):
        self.o_Resistance   =   MetricScale(o_Input)

    def setCapacitance(self, o_Input):
        self.o_Capacitance  =   MetricScale(o_Input)

o_RCLowpassFilter = RCLowpassFilter(o_Resistance="10k", o_Capacitance="318n")

