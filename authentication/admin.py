from django.contrib import admin
from .models import *
from . import models
# Register your models here.
admin.site.site_header='TCE.WEB Admin'
admin.site.index_title='Admin'

class deptAdmin(admin.ModelAdmin):
    list_display=['dept_name']
    search_fields = ['dept_name']
admin.site.register(dept,deptAdmin)

class dept_eventsAdmin(admin.ModelAdmin):
    list_display=['title','dashboard','venue','conducted_by','date','time','image','hover_description','rules','description','rewards','participants','participation_type','contact_details','link']
    search_fields =['title','dashboard','venue','conducted_by','date']
admin.site.register(dept_events,dept_eventsAdmin)

class clubsAdmin(admin.ModelAdmin):
    list_display=['club_name','gs','gt','js','jt','gsn','gtn','jsn','jtn','desc','image']
    search_fields=['club_name','gs']
admin.site.register(clubs,clubsAdmin)

class club_eventsAdmin(admin.ModelAdmin):
    list_display=['title','venue','time','date','image','description','contact_details','clubs']
    search_fields=['title','venue','date','clubs']
admin.site.register(club_events,club_eventsAdmin)

class achieversAdmin(admin.ModelAdmin):
    list_display=['dep_event_name','first','second','third','first_dept','second_dept','third_dept','dept']
    search_fields=['dep_event_name','dept']
admin.site.register(achievers,achieversAdmin)

