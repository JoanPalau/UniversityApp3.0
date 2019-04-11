from django.urls import path
from .views import DegreeListView, home, universities_mock, university_mock, degree_mock


urlpatterns = [
    path('', home, name='home'),
    path('universities/', universities_mock, name='universities'),
    path('university/', university_mock, name='university'),
    path('degree/', degree_mock, name='degree_mock'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
]
