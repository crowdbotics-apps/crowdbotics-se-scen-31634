from django.contrib import admin
from home.models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", )