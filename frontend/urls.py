from django.urls import path
from .views import home, upload_music, upload_video

urlpatterns = [
    path('', home, name='home'),
    path('upload/music/', upload_music, name='upload_music'),
    path('upload/video/', upload_video, name='upload_video'),
]
