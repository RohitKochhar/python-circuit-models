from django import forms

class RCLowPassForm(forms.Form):
    s_ResistorValue     = forms.CharField(
                label='Resistor Value', 
                max_length=15,
                widget=forms.TextInput(attrs={
                    "class": "form-control",
                    "placeholder": "10.4k"
                })
    )
    s_CapacitorValue    = forms.CharField(
                label='Capacitor Value', 
                max_length=15,
                widget=forms.TextInput(attrs={
                    "class": "form-control",
                    "placeholder": "312.4p"
                })
    )
    