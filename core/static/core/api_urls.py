from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, TaskViewSet, IssueViewSet

router = DefaultRouter()

router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('issues', IssueViewSet)

urlpatterns = router.urls