from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account han been created {username}! You are now able to lod in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form': form, 'title': 'Register'})


@login_required
def profile(request):
    context = {
        'title': 'Landing Home',
    }
    return render(request, 'users/profile.html', context)

