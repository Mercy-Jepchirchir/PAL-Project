from Pal import models
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import NetworkSerializer,NetworkResponseSerializer,PalTransactionSerializer

# Create your views here.
class NetworkViewSets(viewsets.ModelViewSet):
    queryset = models.Network.objects.all()
    serializer_class =NetworkSerializer
    
class NetworkResponseViewSets(viewsets.ModelViewSet):
    queryset = models.NetworkResponse.objects.all()
    serializer_class =NetworkResponseSerializer
    
class PalTransactionViewSets(viewsets.ModelViewSet):
    queryset = models.PalTransaction.objects.all()
    serializer_class =PalTransactionSerializer
    
    
class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = models.PalTransaction.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)
   
class AccountTransferView(views.APIView):
    def post(self,request,pk,format=None):
        account_1=models.PalTransaction.objects.get(pk=pk)
        account_id=request.data["destination"]   
        amount=request.data["amount"]  
        

        try:
            account=models.PalTransaction.objects.get(id=account_id)   
        except ObjectDoesNotExist:  
            return Response("Account Not Found", status=404)
        message, status = account_1.transfer(account,amount)    
        return Response (message,status=status)   

    




