from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdmin(UserAdmin):

    ordering = ('email',)
    list_display = ('email', 'fname', 'lname', 'date_joined', 'last_login',)
    search_fields = ('fname', 'lname', 'email')
    readonly_fields = ('id', 'date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    
    fieldsets = (
        ('Credentials',{'fields': ('email', 'password')}),
        ('Details',{'fields': ('fname', 'lname', 'dob', 'gender', 'classstandings', 'major')}),
        ('Logs',{'fields': ('date_joined', 'last_login')}),
        ('Permissions',{'fields': ('is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        ('Credentials',{'fields': ('email', 'password')}),
        ('Details',{'fields': ('fname', 'lname', 'dob', 'gender', 'classstandings', 'major')}),
    )
    # inlines = (UserDepartmentInline, UserVendorInline)
admin.site.register(Account, AccountAdmin)