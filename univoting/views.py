from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from univoting.forms import UniversityForm
from univoting.models.degree import Degree
from univoting.models.subject import Subject
from univoting.models.course import Course
from univoting.models.degree import University
from univoting.models.subject_review import SubjectReview
from univoting.models.subject_comment import SubjectComment


def home(request):
    context = {
        'title': 'Home',
        'subtitle': 'Welcome to UniApp',
        'description': 'Where you can find your perfect university',
    }
    return render(request, 'univoting/home.html', context)


class UniversityListView(ListView):
    model = University
    context_object_name = 'universities'
    template_name = 'univoting/universities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Universities'
        return context


class UniversityCreateView(LoginRequiredMixin, CreateView):
    model = University
    fields = ['name', 'address', 'city', 'country', 'zipcode', 'lat', 'long', 'description', 'picture']
    template_name = 'univoting/university-register.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        # afegir aqui el obtenir la localitzacio
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['title'] = 'University Create View'


class UniversityEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = University
    fields = ['name', 'description']
    template_name = 'univoting/university-register.html'

    def test_func(self):
        university = self.get_object()
        if self.request.user == university.author:
            return True
        return False
'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'University Update View'
'''


class UniversityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = University

    def test_func(self):
        university = self.get_object()
        if self.request.user == university.author:
            return True
        return False

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'University Delete View'
'''


class UniversityDetailView(DetailView):
    model = University
    context_object_name = 'university'
    template_name = 'univoting/university.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['university'].name

        # Obtain list of university degrees
        degrees = Degree.objects.filter(university=context['university'])
        context['degrees'] = degrees
        return context


class DegreeCreateView(LoginRequiredMixin, CreateView):
    model = Degree
    fields = ('title', 'ects', 'description')
    template_name = 'univoting/university-register.html'

    def form_valid(self, form):
        form.instance.university = get_object_or_404(University, self.kwargs['pk'])
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Degree Create View'
'''


class DegreeEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Degree
    fields = ('title', 'ects', 'description')
    template_name = 'univoting/university-register.html'

    def test_func(self):
        university = self.get_object()
        if self.request.user == university.author:
            return True
        return False

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Degree Edit View'
'''


class DegreeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Degree

    def test_func(self):
        university = self.get_object()
        if self.request.user == university.author:
            return True
        return False

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Degree Delete View'
'''


class DegreeDetailView(DetailView):
    model = Degree
    context_object_name = 'degree'
    template_name = 'univoting/degree.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['degree'].title

        # Obtain list of subjects with their course for the Degree
        subjects = Course.objects.filter(degree_id=context['degree'])
        context['subjects'] = subjects

        # Obtain list of best and worst subjects
        subjects_qualified = []
        for subject in subjects.all():
            if subject.subject_id.review:
                subjects_qualified.append(subject)

        context['worst_subjects'], context['best_subjects'] = \
            get_top_for_degrees(3, subjects_qualified)

        return context


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('name', 'ects', 'description')
    template_name = 'univoting/university-register.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class SubjectEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Subject
    fields = ('name', 'ects', 'description')
    template_name = 'univoting/university-register.html'

    def test_func(self):
        university = self.get_object()
        if self.request.user == university.author:
            return True
        return False


class SubjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject

    def test_func(self):
        university = self.get_object()
        if self.request.user == university.author:
            return True
        return False


'''
class SubjectReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectReview

    def form_valid(self, form):
        # cridar update subject?



def update_subject(new_values, old_values):
    SubjectReview.recalculate_score_on_insert()
    return NotImplementedError
'''


class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'univoting/subject.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['subject'].name
        context['comments'] = SubjectComment.objects.filter(subject=context['subject'])
        context['course'] = get_object_or_404(Course, subject_id=context['subject'])
        return context


def get_top_for_degrees(maximum, listed):
    worst_qualifies = sorted(listed, key=lambda item: item.subject_id.review.mark)
    best_qualifies = list(reversed(sorted(listed, key=lambda item: item.subject_id.review.mark)))
    # Check for maximum qualified items
    if listed:
        length = len(listed)
        if length >= maximum:
            best_qualifies = best_qualifies[:maximum]
            worst_qualifies = worst_qualifies[:maximum]

    return worst_qualifies, best_qualifies

#
#########################################################################################
#                           MOCK UPs


def universities_mock(request):
    context = {
        'title': 'Universities',
        'universities':
            {
                ('Harvard', 'noimage.png', 'This is the Harvard university description.'),
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


def degree_mock(request):
    context = {
        'name': 'Degree Example',
        'description': 'This is a description.',
        'curses': {'First', 'Second', 'Third', 'Fourth'},
        'subjects': {
                'Subject Example1',
                'Subject Example2',
                'Subject Example3',
                'Subject Example4',
                'Subject Example5',
                'Subject Example6',
                'Subject Example7',
                'Subject Example8',
            }
        }

    return render(request, 'univoting/degree.html', context)


def subject_mock(request):
    context = {
        'name': 'Subject Example',
        'description': 'This is a description.',
        'comments': {
            'First comment',
            'Second comment',
            'Third comment',
            'Forth comment'
        },
        'mark': 7.5,
        'difficulty': 6.2,
    }

    return render(request, 'univoting/subject.html', context)

#####################################################################################################
#
