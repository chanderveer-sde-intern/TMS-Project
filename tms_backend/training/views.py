from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Task, Submission
from .serializers import TaskSerializer, SubmissionSerializer




class TaskListView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()

        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by("due_date")

class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskSubmissionsView(ListAPIView):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        task_id = self.kwargs['pk']
        return Submission.objects.filter(task_id=task_id)
