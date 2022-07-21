from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=True)
    count = forms.IntegerField(required=True, min_value=0)
    cost = forms.DecimalField(required=True, min_value=0, decimal_places=2)