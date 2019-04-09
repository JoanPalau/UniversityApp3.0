from django.urls import path
from .views import DegreeListView, home, universities_mock, university_mock


urlpatterns = [
    path('', home, name='home'),
    path('universities/', universities_mock, name='universities'),
    path('university/', university_mock, name='university'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
]
