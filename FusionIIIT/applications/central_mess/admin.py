from django.contrib import admin

from .models import Mess, Menu, Monthly_bill, Payments, Rebate, Special_request, Vacation_food, Nonveg_data, Nonveg_menu, Mess_meeting, Menu_change_request, Feedback
# Register your models here.

class MessAdmin(admin.ModelAdmin):
    model = Mess
    
    fieldsets = [
        ('mess_option',{'fields': ['department']}),
        ('student', {'fields': ['sanction_cl_rh'], 'classes': ['collapse']}),
        ('nonveg_total_bill', {'fields': ['nonveg_total_bill'], 'classes': ['collapse']}),
        ('rebate_count', {'fields': ['rebate_count'], 'classes': ['collapse']}),
        ('count', {'fields': ['count'], 'classes': ['collapse']}),
        ('current_bill', {'fields': ['current_bill'], 'classes': ['collapse']})

    ]
    list_display = ('student', 'mess_option','nonveg_total_bill','rebate_count','count','current_bill')



class MenuAdmin(admin.ModelAdmin):
    model = Menu
    
    fieldsets = [
        ('mess_option',{'fields': ['mess_option']}),
        ('meal_time', {'fields': ['meal_time'], 'classes': ['collapse']}),
        ('dish', {'fields': ['dish'], 'classes': ['collapse']}),
        
    ]
    list_display = ('mess_option', 'meal_time','dish')


class Monthly_billAdmin(admin.ModelAdmin):
    model = Monthly_bill
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('month', {'fields': ['month'], 'classes': ['collapse']}),
        ('amount', {'fields': ['amount'], 'classes': ['collapse']}),
        
    ]
    list_display = ('student_id','month','amount')

class PaymentsAdmin(admin.ModelAdmin):
    model = Payments
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('sem', {'fields': ['sem'], 'classes': ['collapse']}),
        ('amount_paid', {'fields': ['amount_paid'], 'classes': ['collapse']}),
        
    ]
    list_display = ('student_id','sem','amount_paid')

class RebateAdmin(admin.ModelAdmin):
    model = Rebate
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('start_date', {'fields': ['start_date'], 'classes': ['collapse']}),
        ('end_date', {'fields': ['end_date'], 'classes': ['collapse']}),
        ('purpose', {'fields': ['purpose'], 'classes': ['collapse']}),
        ('status', {'fields': ['status'], 'classes': ['collapse']}),
        
    ]
    list_display = ('student_id','start_date','end_date','purpose','status')

class Vacation_foodAdmin(admin.ModelAdmin):
    model = Vacation_food
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('start_date', {'fields': ['start_date'], 'classes': ['collapse']}),
        ('end_date', {'fields': ['end_date'], 'classes': ['collapse']}),
        ('purpose', {'fields': ['purpose'], 'classes': ['collapse']}),
        ('status', {'fields': ['status'], 'classes': ['collapse']}),
        
    ]
    list_display = ('student_id','start_date','end_date','purpose','status')

class Nonveg_menuAdmin(admin.ModelAdmin):
    model = Nonveg_menu
    fieldsets = [
        ('dish',{'fields': ['dish']}),
        ('price', {'fields': ['price'], 'classes': ['collapse']})
        
    ]
    list_display = ('dish','price')

class Nonveg_dataAdmin(admin.ModelAdmin):
    model = Nonveg_data
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('order_date', {'fields': ['order_date'], 'classes': ['collapse']}),
        ('order_interval', {'fields': ['order_interval'], 'classes': ['collapse']}),
        ('dish', {'fields': ['dish'], 'classes': ['collapse']})
        
    ]
    list_display = ('student_id','order_date','order_interval','dish')

class Special_requestAdmin(admin.ModelAdmin):
    model = Special_request
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('start_date', {'fields': ['start_date'], 'classes': ['collapse']}),
        ('end_date', {'fields': ['end_date'], 'classes': ['collapse']}),
        ('request', {'fields': ['request'], 'classes': ['collapse']}),
        ('status', {'fields': ['status'], 'classes': ['collapse']}),
        
    ]
    list_display = ('student_id','start_date','end_date','request','status')

class Menu_change_requestAdmin(admin.ModelAdmin):
    model = Menu_change_request
    fieldsets = [
        ('dish',{'fields': ['dish']}),
        ('request', {'fields': ['request'], 'classes': ['collapse']}),
        ('status', {'fields': ['status'], 'classes': ['collapse']}),
        
    ]
    list_display = ('dish','request','status')

class Mess_meetingAdmin(admin.ModelAdmin):
    model = Mess_meeting
    fieldsets = [
        ('meeting_date',{'fields': ['meeting_date']}),
        ('agenda', {'fields': ['agenda'], 'classes': ['collapse']}),
        ('venue', {'fields': ['venue'], 'classes': ['collapse']}),
        ('meeting_time', {'fields': ['meeting_time'], 'classes': ['collapse']}),
        ('mess_minutes', {'fields': ['mess_minutes'], 'classes': ['collapse']}),
        
    ]
    list_display = ('meeting_date','agenda','venue','meeting_time','mess_minutes')   

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    fieldsets = [
        ('student_id',{'fields': ['student_id']}),
        ('fdate', {'fields': ['fdate'], 'classes': ['collapse']}),
        ('description', {'fields': ['description'], 'classes': ['collapse']}),
        ('feedback_type', {'fields': ['feedback_type'], 'classes': ['collapse']})
        
    ]
    list_display = ('student_id','fdate','description','feedback_type')


admin.site.register(Mess, MessAdmin),
admin.site.register(Menu, MenuAdmin),
admin.site.register(Monthly_bill, Monthly_billAdmin ),
admin.site.register(Payments, PaymentsAdmin),
admin.site.register(Rebate, RebateAdmin),
admin.site.register(Vacation_food, Vacation_foodAdmin),
admin.site.register(Special_request, Special_requestAdmin),
admin.site.register(Nonveg_menu, Nonveg_menuAdmin),
admin.site.register(Nonveg_data, Nonveg_dataAdmin),
admin.site.register(Mess_meeting, Mess_meetingAdmin),
admin.site.register(Feedback, FeedbackAdmin),
admin.site.register(Menu_change_request, Menu_change_requestAdmin)
