from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('employee', views.EmployeeViewSet)
router.register('service', views.ServiceViewSet)

urlpatterns = router.urls
