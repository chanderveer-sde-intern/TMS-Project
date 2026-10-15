from rest_framework import serializers
from .models import Task, Submission, Profile


class TaskSerializer(serializers.ModelSerializer):

    intern_username = serializers.ReadOnlyField(
        source = 'intern.username'
    )

    class Meta:
        model = Task
        fields = "__all__" 

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
