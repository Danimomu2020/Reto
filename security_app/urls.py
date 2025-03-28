from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from security_app import views

router = routers.DefaultRouter()
router.register(r'vulnerabilities', views.VulnerabilityViewSet, basename='vulnerability')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Las URLs para las acciones personalizadas se generan automáticamente por el router
]