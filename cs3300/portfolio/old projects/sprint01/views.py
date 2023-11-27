from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
"""from .forms import ProjectForm, PortfolioForm"""
from django.contrib import messages
from .forms import VideoForm

def index(request):

    return render( request, 'sprint01/index.html')


def createVideo(request):
    form = VideoForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        video_data = request.POST.copy()
        
        form = VideoForm(video_data)
        if form.is_valid():
            # Save the form without committing to the database
            video = form.save(commit=False)
            # Set the portfolio relationship
            video.save()

            # Redirect back to the portfolio detail page
            return redirect('video-detail')

    context = {'form': form}
    return render(request, 'sprint01/video_form.html', context)

def deleteVideo(request, video_id): 

    obj = get_object_or_404(Video, id=video_id)
    context ={
        "video_id":video_id
    }
 
    if request.method =="POST":
        obj.delete()
        return redirect('video-detail', portfolio_id)

    return render(request, "sprint01/delete_view.html", context)

def updateVideo(request, video_id):
    form = VideoForm()
    portfolio = Video.videos.get(pk=video_id)

    context ={
        "video_id":video_id
    }
    obj = get_object_or_404(Video, id=video_id)
    form = VideoForm(request.POST, instance=obj)

    if form.is_valid():
            # Save the form without committing to the database
            video = form.save(commit=False)
            video.save()

            # Redirect back to the portfolio detail page
            return redirect('video-detail', video_id)
    context = {'form': form}
    return render(request, 'sprint01/video_form.html', context)



class VideoListView(generic.ListView):
    model = Video
class VideoDetailView(generic.DetailView):
    model = Video
