from django.shortcuts import render, redirect
from .models import Score
from .forms import ScoreForm
from django.contrib.auth.decorators import login_required

def home(request):
    scores = Score.objects.all()
    return render(request, 'scoretracker/home.html', {'scores': scores})

@login_required
def add_score(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.user = request.user
            score.save()
            return redirect('home')
    else:
        form = ScoreForm()
    return render(request, 'scoretracker/add_score.html', {'form': form})
