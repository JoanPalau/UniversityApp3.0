from django.urls import path
from .views import home, UniversityListView, UniversityDetailView, DegreeDetailView, SubjectDetailView
from .views import universities_mock, university_mock, degree_mock, subject_mock


urlpatterns = [
    path('', home, name='home'),
    path('universities/', UniversityListView.as_view(), name='universities'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university'),
    path('degree/<int:pk>/', DegreeDetailView.as_view(), name='degree'),
    path('subject/<int:pk>/', SubjectDetailView.as_view(), name='subject'),
    # path('universities/', universities_mock, name='universities'),
    # path('university/', university_mock, name='university'),
    # path('degree/', degree_mock, name='degree'),
    # path('subject/', subject_mock, name='subject'),
]
