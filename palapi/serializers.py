from Pal import  models
from rest_framework import serializers

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Network
        fields = ('name','code')
        
class NetworkResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NetworkResponse
        fields = ('message','ref','date_time')
        

class PalTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PalTransaction
        fields = ('sender','receiver','amount','network','response','processed_by')