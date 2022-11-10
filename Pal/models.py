from django.db import models

import uuid

# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length=225)
    code = models.CharField(max_length=255)
    
    def _str_(self):
        return self.name
    
class NetworkResponse(models.Model):
    message = models.TextField()
    ref = models.UUIDField(uuid.uuid4())
    date_time = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.ref
    
class PalTransaction(models.Model):
    sender = models.CharField(max_length=225)
    receiver= models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    network = models.ForeignKey(Network,on_delete=models.PROTECT)
    response = models.ForeignKey(NetworkResponse,on_delete=models.PROTECT)
    processed_by = models.CharField(max_length= 225)
    
    
    def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.amount += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.amount}"
           status = 200
       return message, status
   
    def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.amount:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.amount -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount},  from{self.sender} to {destination}your new balance is {self.amount}"
           status = 200
       return message, status




    

    
    
