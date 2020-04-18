from django.contrib import admin

# Register your models here.
from questionLib.models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "url"]


class QuestionLibAdmin(admin.ModelAdmin):
    list_display = ["id", "question"]
    search_fields = ["question", "A", "B", "C", "D"]


class LogAdmin(admin.ModelAdmin):
    list_display = ["versation", "time", "description"]
    search_fields = ["versation", "time", "description"]


admin.site.register(Banner, BannerAdmin)
admin.site.register(QuestionLib, QuestionLibAdmin)
admin.site.register(Log, LogAdmin)
