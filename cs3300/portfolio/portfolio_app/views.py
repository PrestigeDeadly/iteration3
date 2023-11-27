from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
"""from .forms import ProjectForm, PortfolioForm"""
from django.contrib import messages
from .forms import VideoForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

def index(request):

    return render( request, 'portfolio_app/index.html')

@login_required
def createVideo(request):
    form = VideoForm()
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        video_data = request.POST.copy()
        
        form = VideoForm(video_data, request.FILES)
        if form.is_valid():
            # Save the form without committing to the database
            video = form.save(commit=False)
            # Set the portfolio relationship
            video.save()

            # Redirect back to the portfolio detail page
            return redirect('videos')

    context = {'form': form}
    return render(request, 'portfolio_app/video_form.html', context)

@login_required
def deleteVideo(request, video_id): 

    obj = get_object_or_404(Video, id=video_id)
    context ={
        "video_id":video_id
    }
 
    if request.method =="POST":
        obj.delete()
        return redirect('videos')

    return render(request, "portfolio_app/delete_view.html", context)

@login_required
def updateVideo(request, video_id):
    form = VideoForm()

    context ={
        "video_id":video_id
    }
    obj = get_object_or_404(Video, id=video_id)
    form = VideoForm(request.POST, request.FILES, instance=obj)

    if form.is_valid():
            # Save the form without committing to the database
            video = form.save(commit=False)
            video.save()

            # Redirect back to the portfolio detail page
            return redirect('videos')
    context = {'form': form}
    return render(request, 'portfolio_app/video_form.html', context)

class VideoListView(generic.ListView):
    model = Video
class VideoDetailView(generic.DetailView):
    model = Video
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
