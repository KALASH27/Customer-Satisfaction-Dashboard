from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cus_Res


@admin.register(Cus_Res)
class CusAdmin(ImportExportModelAdmin):
    list_display = ('Cus_id', 'Cus_name', 'Checkin', 'Checkout', 'Easeofonlinebooking', 'wifi_Service', 'FoodDrinks', 'DepartureArrivalConvinience', 'Checkinoutservice', 'Cleanliness', 'OtherServices', 'Satisfication')