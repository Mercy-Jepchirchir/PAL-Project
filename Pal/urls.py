from django.urls import path
from .  import views

urlpatterns = [

    path("transaction/",views.register_transaction,name="transaction"),
    
]