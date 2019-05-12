from django.urls import path
from .views import home, UniversityListView, UniversityDetailView, DegreeDetailView, SubjectDetailView, \
    UniversityCreateView, UniversityEditView, UniversityDeleteView, \
    DegreeCreateView, DegreeEditView, DegreeDeleteView, \
    SubjectCreateView, SubjectEditView, SubjectDeleteView, SubjectCommentCreate
from .views import universities_mock, university_mock, degree_mock, subject_mock


urlpatterns = [
    path('', home, name='home'),
    path('universities/', UniversityListView.as_view(), name='universities'),
    path('universities/<int:pk>/', UniversityDetailView.as_view(), name='university'),
    path('degree/<int:pk>/', DegreeDetailView.as_view(), name='degree'),
    path('degree/<int:pkd>/subject/<int:pk>/', SubjectDetailView.as_view(), name='subject'),
    # Editar universities
    path('universities/new/', UniversityCreateView.as_view(), name='new-university'),
    path('universities/<int:pk>/update/', UniversityEditView.as_view(), name='update-university'),
    path('universities/<int:pk>/delete/', UniversityDeleteView.as_view(), name='delete-university'),
    # Editar degree
    path('universities/<int:pk>/new/', DegreeCreateView.as_view(), name='new-degree'),
    path('degree/<int:pk>/update/', DegreeEditView.as_view(), name='update-degree'),
    path('degree/<int:pk>/delete/', DegreeDeleteView.as_view(), name='delete-degree'),
    # Editar subject
    path('degree/<int:pk>/new/', SubjectCreateView.as_view(), name='new-subject'),
    path('degree/<int:pkd>/subject/<int:pk>/update/', SubjectEditView.as_view(), name='update-subject'),
    path('degree/<int:pkd>/subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='delete-subject'),
    # Editar reviews
    path('subject/<int:pk>/comment/new', SubjectCommentCreate.as_view(), name='add-comment'),
    path('degree/<int:pkd>/subject/<int:pk>/new/', SubjectEditView.as_view(), name='update-review'),

    # Editar comment
    # path('subject/<int:pks>/comment<int:pk>/update/', SubjectCommentEdit.as_view(), name='update-comment'),
    # path('subject/<int:pks>/comment/<int:pk>/delete/', SubjectCommentDelete.as_view(), name='delete-comment'),
    # path('universities/', universities_mock, name='universities'),
    # path('university/', university_mock, name='university'),
    # path('degree/', degree_mock, name='degree'),
    # path('subject/', subject_mock, name='subject'),
]
