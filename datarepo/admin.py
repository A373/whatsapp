from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, chats, status, groups


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


class chatsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'message', 'created']
    list_filter = ['user_name', 'message']
    search_fields = ['user_name', 'message']


class statusAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'created']
    list_filter = ['user']
    search_fields = ['user']


class groupsAdmin(admin.ModelAdmin):
    fields = ['username', 'message', 'created']
    list_display = ['message', 'created']
    list_filter = ['username']
    search_fields = ['username']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(chats, chatsAdmin)
admin.site.register(status, statusAdmin)
admin.site.register(groups, groupsAdmin)
