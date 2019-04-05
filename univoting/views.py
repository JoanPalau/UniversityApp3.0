from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from univoting.models.degree import Degree


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
