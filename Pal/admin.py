from django.contrib import admin
from .models import Network,NetworkResponse,PalTransaction

# Register your models here.

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name','code')
    search_fields = ('name','code')
admin. site.register(Network,NetworkAdmin)

class NetworkResponseAdmin(admin.ModelAdmin):
    list_display = ('message','ref','date_time')
    search_fields = ('message','ref','date_time')
admin. site.register(NetworkResponse,NetworkResponseAdmin)

class PalTransactionAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','amount','network','response','processed_by')
    search_fields = ('sender','receiver','amount','network','response','processed_by')
admin. site.register(PalTransaction,PalTransactionAdmin)