from django.contrib import admin
from .models import Department,Complaint,Payment,Student,Notice

# admin.site.register(Department)
admin.site.register(Notice)

# @admin.register(Student)    
# class StudentAdmin(admin.ModelAdmin):
#     list_display=("name","current_semester","address","phone_number")
#     list_filter=("current_semester","branch")

# @admin.register(Complaint)    
# class ComplaintAdmin(admin.ModelAdmin):
#     list_display=("text","date_of_complaint","student")
#     list_filter=("date_of_complaint","student__name")

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display=("student","amount","date_of_payment","remarks")
#     list_filter=("student","date_of_payment")