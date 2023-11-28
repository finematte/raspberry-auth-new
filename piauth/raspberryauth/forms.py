from django import forms


class CodeForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label="")
