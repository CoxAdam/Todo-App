from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("task-lists", TaskListViewSet, basename="task_list")
router.register("tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls))
]