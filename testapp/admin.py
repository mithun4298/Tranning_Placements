from django.contrib import admin
from testapp.models import student, info
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['s_username','s_name','s_branch', 's_semester','s_proglang']
class infoAdmin(admin.ModelAdmin):
    list_display = ['i_username','i_companyname','i_jobtype','i_joblocation','i_jobsalary']


admin.site.register(student,studentAdmin)
admin.site.register(info, infoAdmin)
admin.site.site_header = "Training and placement"
admin.site.site_title = "Training and placement placement"