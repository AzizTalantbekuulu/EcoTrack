from django.urls import path
from .views import (
    RegisterView, UserListCreateView, UserDetailView,
    SensorListCreateView, SensorDetailView,
    DataListCreateView, DataDetailView,
    AlertListCreateView, AlertDetailView, LoginView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('sensor/', SensorListCreateView.as_view(), name='sensor-list'),
    path('sensor/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensor/<int:sensor_id>/data/', DataListCreateView.as_view(), name='data-list'),
    path('sensor/<int:sensor_id>/data/<int:pk>/', DataDetailView.as_view(), name='data-detail'),
    path('sensor/<int:sensor_id>/alerts/', AlertListCreateView.as_view(), name='alert-list'),
    path('sensor/<int:sensor_id>/alerts/<int:pk>/', AlertDetailView.as_view(), name='alert-detail'),
]
