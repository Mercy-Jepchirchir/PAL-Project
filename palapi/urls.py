from django.urls import path, include
from rest_framework import routers
from .views import AccountDepositView, AccountTransferView, NetworkViewSets,NetworkResponseViewSets,PalTransactionViewSets

router = routers.DefaultRouter()
router.register(r"Network",NetworkViewSets)
router.register(r"NetworkResponse",NetworkResponseViewSets)
router.register(r"transaction",PalTransactionViewSets)

urlpatterns = [
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("deposit/<int:id>",AccountDepositView.as_view(),name='deposit-view'), 
    path("transfer/<int:pk>/",AccountTransferView.as_view(), name="transfer-view"),
    
]
