from django.urls import path
from .views import DegreeListView, home


urlpatterns = [
    path('', home, name='home'),
    path('degrees/', DegreeListView.as_view(), name='degrees'),
]
