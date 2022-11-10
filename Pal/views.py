from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def register_transaction(request):
    if request.method == "POST":
        form = forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.TransactionRegistrationForm()     
    return render(request,'palapp/register_transactionn.html',
                  {"form":form})
    
def list_transaction(request):
    transaction = models.PalTransaction.objects.all()
    return render (request, 'palapp/transaction_list.html',
                   {"transactions":transaction})