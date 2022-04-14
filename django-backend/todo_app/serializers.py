from rest_framework import serializers
from .models import *

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ["id", "name", "description", "all_done", "tasks"]

    all_done = serializers.SerializerMethodField(read_only=True)

    def get_all_done(self, instance):
        return instance.get_completed_tasks()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "list", "due_date", "is_completed"]