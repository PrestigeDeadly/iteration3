from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('videos/', views.VideoListView.as_view(), name= 'videos'),
path('videos/<int:pk>', views.VideoDetailView.as_view(), name='video-detail'),
path('videos/createvideo', views.createVideo, name='create_video'),
path('videos/<int:video_id>/update_video/', views.updateVideo, name='update_video'),
path('videos/<int:video_id>/delete_video/', views.deleteVideo, name='delete_video'),
path('signup/', views.SignUpView.as_view(), name='signup'),
]