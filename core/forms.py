from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class ServidoresFilterForm(forms.Form):
    nome = forms.CharField(max_length=50)
    siape = forms.CharField(max_length=7)
