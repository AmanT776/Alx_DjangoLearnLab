from django import forms

class ExampleForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100, required=False)
