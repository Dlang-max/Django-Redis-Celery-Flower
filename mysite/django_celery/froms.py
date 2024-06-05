from django import forms

class TestForm(forms.Form):
    field = forms.CharField(label="field", max_length=100)