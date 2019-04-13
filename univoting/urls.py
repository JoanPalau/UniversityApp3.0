from django.urls import path
from .views import universities_mock, university_mock, degree_mock, subject_mock
from .views import home, DegreeListView, UniversityListView, UniversityDetailView, DegreeDetailView


urlpatterns = [
    path('', home, name='home'),
    path('universities/', UniversityListView.as_view(), name='universities'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university'),
    path('degree/<int:pk>/', DegreeDetailView.as_view(), name='degree'),

    path('subject/', subject_mock, name='subject'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
    # path('universities/', universities_mock, name='universities'),
    # path('university/', university_mock, name='university'),
    # path('degree/', degree_mock, name='degree'),
]
