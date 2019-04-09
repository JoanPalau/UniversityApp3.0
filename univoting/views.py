from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from univoting.models.degree import Degree
from univoting.models.subject import Subject
from univoting.models.course import Course
from univoting.models.degree import University


def home(request):
    context = {
        'title': 'UniApp',
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
