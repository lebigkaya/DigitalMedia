from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import MusicFile, VideoFile

def home(request):
    last_video = VideoFile.objects.latest('uploaded_at') if VideoFile.objects.exists() else None
    last_audio = MusicFile.objects.latest('uploaded_at') if MusicFile.objects.exists() else None
    return render(request, 'frontend/index.html', {'last_video': last_video, 'last_audio': last_audio})

def upload_music(request):
    if request.method == 'POST' and request.FILES['music']:
        music = request.FILES['music']
        fs = FileSystemStorage()
        filename = fs.save(music.name, music)
        MusicFile.objects.create(file=filename)
        return redirect('home')
    return render(request, 'frontend/upload_music.html')

def upload_video(request):
    if request.method == 'POST' and request.FILES['video']:
        video = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)
        VideoFile.objects.create(file=filename)
        return redirect('home')
    return render(request, 'frontend/upload_video.html')
