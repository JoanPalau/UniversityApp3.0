from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from univoting.models.degree import Degree


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
