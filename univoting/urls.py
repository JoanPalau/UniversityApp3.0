from django.urls import path
from .views import DegreeListView, home, universities_mock, university_mock, degree_mock, subject_mock


urlpatterns = [
    path('', home, name='home'),
    path('universities/', universities_mock, name='universities'),
    path('university/', university_mock, name='university'),
    path('degree/', degree_mock, name='degree'),
    path('subject/', subject_mock, name='subject'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
]
