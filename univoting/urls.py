from django.urls import path
from .views import universities_mock, university_mock, degree_mock, subject_mock
from .views import home, DegreeListView, UniversityListView


urlpatterns = [
    path('', home, name='home'),
    path('universities/', UniversityListView.as_view(), name='universities'),
    path('university/', university_mock, name='university'),
    path('degree/', degree_mock, name='degree'),
    path('subject/', subject_mock, name='subject'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
    # path('universities/', universities_mock, name='universities'),
]
