from django.db import models
from django.db.models.signals import post_init

from sigfig import round

# Create your models here.

class Number(models.Model):
    d_MetricScale  =   {
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

    s_Input     = models.CharField(max_length=15)

    def setNumber(self):
        # The input will always be a string
        # First, try to convert to float
        try:
            # If we succeed, our number is set
            self.f_Value    = float(self.s_Input)
        except Exception as e:
            b_PrefixMatched = False
            for s_Prefix in self.d_MetricScale:
                if self.s_Input[-1] == s_Prefix:
                    b_PrefixMatched = True
            if b_PrefixMatched == False:
                raise ValueError(f"Prefix {self.s_Input[-1]} not a valid metric prefix")
            else:
                f_Value     = float(self.s_Input[:-1])
                i_Exponent  = int(self.d_MetricScale[self.s_Input[-1]])
                self.i_SigFigs  = len(self.s_Input[:-1])
                self.f_Value    = round(f_Value*(10**i_Exponent), sigfigs=self.i_SigFigs)

def NumberConstructor(**kwargs):
    o_Number    = kwargs.get('instance')
    o_Number.setNumber()


post_init.connect(NumberConstructor, Number)