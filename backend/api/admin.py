from django.contrib import admin
from .models import Project, Task, Comment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_by', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'assigned_to', 'due_date', 'created_at')
    list_filter = ('status', 'due_date')
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'task', 'created_by', 'created_at')
    search_fields = ('content',)
