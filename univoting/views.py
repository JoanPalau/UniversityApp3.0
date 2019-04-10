from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from univoting.models.degree import Degree
from univoting.models.subject import Subject
from univoting.models.course import Course
from univoting.models.degree import University


def home(request):
    context = {
        'title': 'Home',
        'description': 'TEMP DESCRIPTION',
    }
    return render(request, 'univoting/home.html', context)


class DegreeListView(ListView):
    model = Degree
    template_name = 'univoting/degree_list.html'

    '''
    slug_field = "university"
    slug_url_kwarg = "university"

    def get_queryset(self):
        self.university = get_object_or_404(Degree, room=self.kwargs['university'])
        return Degree.objects.filter(univesity=self.university)
    '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Degrees'
        return context


def universities_mock(request):
    context = {
        'title': 'Universities',
        'universities':
            {
                ('Harvard', 'image1.jpg', 'This is the Harvard university description.'),
                ('MIT', 'image2.jpg', 'This is the MIT university description.'),
                ('Stanford', 'image3.jpg', 'This is the Stanford university description.'),
                ('Universitat de Lleida', 'udl.jpg', 'This is the Universitat de Lleida description.'),
                ('Oxford', 'oxford.png', 'This is the Oxford university description.'),
            },
        'description': 'This is the universities page description.',
    }
    return render(request, 'univoting/universities.html', context)


def university_mock(request):
    context = {
        'title': 'Universitat de Lleida',
        'name': 'Universitat de Lleida',
        'description': 'This is the universities page description.',
        'picture': 'image1.jpg',
        'degrees': {
            'Anthropology',
            'Architecture, Landscape Architecture, and Urban Planning',
            'Astronomy',
            'Biophysics',
            'Business Administration',
            'Business Economics',
            'Celtic Languages and Literatures',
            'The Classics',
            'Computer science',
            'Data Science ',
            'Economics',
            'Education',
            'Engineering and Applied Sciences',
            'English',
            'Germanic Languages and Literatures',
            'Inner Asian and Altaic Studies',
            'Materials Science and Mechanical Engineering',
            'Mathematics',
            'Near Eastern Languages and Civilizations',
            'Philosophy',
            'Physics',
            'Political Economy and Government',
            'Population Health Sciences',
            'Regional Studies–Russia, Eastern Europe, and Central Asia',
            'Speech and Hearing Bioscience and Technology ',
            'Virology ',
            }
    }
    return render(request, 'univoting/university.html', context)


class DegreeDetailView(DetailView):
    model = Degree
    context_object_name = 'degree'
    # template_name = '' No template yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model.title

        # Obtain list of subjects with their course for the Degree
        subjects = Course.objects.filter(degree_id=self.model.pk)
        context['subjects'] = subjects
        return context


class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'subject'
    # template_name = '' No template yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model.name
        return context


class UniversityListView(ListView):
    model = University
    context_object_name = 'universities'
    # template_name = '' No template yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Universities'
        return context
