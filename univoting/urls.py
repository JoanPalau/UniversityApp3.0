from django.urls import path
from .views import DegreeListView, home, universities_mock


urlpatterns = [
    path('', home, name='home'),
    path('universities/', universities_mock, name='universities'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
]
