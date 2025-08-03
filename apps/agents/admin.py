from django.contrib import admin
from .models import Agent, VerifiedSupplier

class VerifiedSupplierInline(admin.TabularInline):
    model = VerifiedSupplier
    extra = 0

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__name', 'user__phone')
    ordering = ('-created_at',)
    inlines = [VerifiedSupplierInline]

@admin.register(VerifiedSupplier)
class VerifiedSupplierAdmin(admin.ModelAdmin):
    list_display = ('agent', 'supplier_id', 'status', 'verification_date')
    list_filter = ('status', 'verification_date', 'created_at')
    search_fields = ('agent__user__name', 'supplier_id')
    ordering = ('-verification_date',)