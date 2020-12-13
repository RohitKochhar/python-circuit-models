from sigfig import round

class MetricScale():
    def __init__(self, o_Input=-1):
        self.d_MetricScale  =   {
            "T":    12,
            "G":    9,
            "M":    6,
            "k":    3,
            "h":    2,

            "d":    -1,
            "c":    -2,
            "m":    -3,
            "u":    -6,
            "n":    -9,
            "p":    -12   
        }

        if o_Input == -1:
            raise ValueError("You must provide either an integer or string to the MetricScale() class upon call")
            return

        self.setNumber(o_Input)


    def setNumber(self, o_Input):
        if type(o_Input) == str:
            s_Input = o_Input
            b_PrefixMatched = False
            for s_Prefix in self.d_MetricScale:
                if s_Input[-1] == s_Prefix:
                    b_PrefixMatched = True
            if b_PrefixMatched == False:
                raise ValueError(f"Prefix {s_Input[-1]} not a valid metric prefix")
            else:
                f_Value     = float(s_Input[:-1])
                i_Exponent  = int(self.d_MetricScale[s_Input[-1]])
                self.i_SigFigs  = len(s_Input[:-1])
                self.f_Value    = round(f_Value*(10**i_Exponent), sigfigs=self.i_SigFigs)
        elif type(o_Input) == int or type(o_Input) == float:
            f_Input = float(o_Input)
            self.f_Value    =   f_Input

    def __str__(self):
        return f_Input