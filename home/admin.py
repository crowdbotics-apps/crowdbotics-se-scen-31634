from django.contrib import admin
from home.models import Plan, App, Subscription

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "created_at", "updated_at")
    ordering = ("-updated_at", )


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "type", "framework", "user", "created_at", "updated_at")
    list_filter = ("type", "framework", "updated_at")
    ordering = ("-updated_at", )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("app", "plan", "active", "created_at", "updated_at")
    list_filter = ("plan", "updated_at", )
    ordering = ("-updated_at", )