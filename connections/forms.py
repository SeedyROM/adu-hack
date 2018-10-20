from django import forms


class JobForm(forms.Form):
    address = forms.CharField(label='Address', max_length=512, required=True)
    description = forms.CharField(label='Description', max_length=100, required=True)
