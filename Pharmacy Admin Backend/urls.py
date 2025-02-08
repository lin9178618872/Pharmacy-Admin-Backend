from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medication import views

router = DefaultRouter()
router.register(r'medications', views.MedicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
