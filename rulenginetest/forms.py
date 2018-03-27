from django import forms


class RulengineForm(forms.Form):
    email = forms.CharField(max_length=100, required=False)
    age = forms.IntegerField(required=False)
    country = forms.CharField(max_length=2, required=False)
    bank_account = forms.FloatField(required=False)
