from django.urls import path
from .views import DegreeListView


urlpatterns = [
    # TEMP: This is not the home page
    # *******************************
    path('', DegreeListView.as_view(template_name='univoting/degree_list.html'), name=''),
    # path('degrees/', DegreeListView.as_view(), name='degrees'),
]
