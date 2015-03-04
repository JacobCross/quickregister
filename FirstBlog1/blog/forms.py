from django import forms

class dataform(forms.Form):
    fname = forms.CharField(label='fname', max_length=100)
    lname = forms.CharField(label='lname', max_length=30)
    school = forms.CharField(label='school', max_length=100)