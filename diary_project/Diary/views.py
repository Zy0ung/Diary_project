from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from Diary.models import Diary
from django.utils import timezone

# Create your views here.
def home(request):
    diaries = Diary.objects.all()
    return render(request, 'home.html', {'diaries':diaries})

def create(request):
    if request.method == 'POST':
            new_diary = Diary()
            new_diary.title = request.POST['title']
            new_diary.body = request.POST['body']
            new_diary.image = request.FILES['image']
            new_diary.pub_date = timezone.now()
            new_diary.weather = request.POST['weather']
            new_diary.save()
            return redirect('home')
    else:
        return render(request, 'new.html')
