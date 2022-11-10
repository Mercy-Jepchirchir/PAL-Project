from django import forms
from . import models


class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.PalTransaction
        fields = "__all__"