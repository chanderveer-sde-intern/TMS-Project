from django.contrib import admin
from .models import Profile, Task, Submission


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Columns displayed in the Profile table.
    list_display = (
        'id',
        'user',
        'role',
        'mentor',
    )

    # Filters displayed in the sidebar.
    list_filter = (
        'role',
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'intern',
        'title',
        'due_date',
        'status',
    )

    list_filter = (
        'status',
        )


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'task',
        'github_link',
        'submitted_at',
        'score',
    )

    list_filter = (
        'submitted_at',
        'score',
    )
