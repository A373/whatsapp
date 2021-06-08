from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, contacts, chats, status, groups


# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'otp', 'username', 'phone', 'created']
    search_fields = ['phone', 'username']
    list_filter = ['phone', 'username']

    UserAdmin.fieldsets += (
        (
            'Custom fields', {
                'fields': ('phone', 'otp', 'created')
            }
        ),
    )


class contactsAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'contact_number']
    list_filter = ['contact_name', 'contact_number']
    search_fields = ['contact_name', 'contact_number']


class chatsAdmin(admin.ModelAdmin):
    list_display = ['contact_number', 'message', 'created']
    list_filter = ['contact_number', 'message']
    search_fields = ['contact_number', 'message']


class statusAdmin(admin.ModelAdmin):
    list_display = ['contact_number', 'text', 'image', 'created']
    list_filter = ['contact_number']
    search_fields = ['contact_number']


class groupsAdmin(admin.ModelAdmin):
    fields = ['contact_number', 'group_name', 'group_image', 'description', 'message', 'created']
    list_display = ['group_name', 'group_image', 'description', 'message', 'created']
    list_filter = ['contact_number', 'group_name']
    search_fields = ['contact_number', 'group_name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(contacts, contactsAdmin)
admin.site.register(chats, chatsAdmin)
admin.site.register(status, statusAdmin)
admin.site.register(groups, groupsAdmin)
