from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100, required=False)
