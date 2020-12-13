from django import forms

class RCLowPassForm(forms.Form):
    s_ResistorValue     = forms.CharField(label='Resistor Value', max_length=15)
    s_CapacitorValue    = forms.CharField(label='Capacitor Value', max_length=15)
    