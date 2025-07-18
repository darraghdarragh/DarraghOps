from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title',)
    ordering = ('-created_at',)

# Customize admin branding
admin.site.site_header = "DarraghOps Admin"
admin.site.site_title = "DarraghOps Admin Portal"
admin.site.index_title = "Welcome to the DarraghOps Dashboard"
