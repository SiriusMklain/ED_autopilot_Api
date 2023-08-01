from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin


class DescriptionAdmin(ModelAdmin):
    list_display = ['id',
                    'status_update',
                    'version_app',
                    'short_text',
                    'text_app',
                    ]


class GlobalActiveAdmin(ModelAdmin):
    list_display = ['id',
                    'global_active'
                    ]


class CmndrAdmin(ModelAdmin):
    list_display = ['id',
                    'name_cmdr',
                    'active',
                    'screen_size',
                    ]


admin.site.register(Description, DescriptionAdmin)
admin.site.register(GlobalActive, GlobalActiveAdmin)
admin.site.register(Cmndr, CmndrAdmin)