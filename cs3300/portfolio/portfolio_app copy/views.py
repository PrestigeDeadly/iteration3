from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
"""from .forms import ProjectForm, PortfolioForm"""
from django.contrib import messages
from .forms import ProjectForm
from .forms import PortfolioForm

def index(request):

    return render( request, 'portfolio_app/index.html')

def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.portfolios.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def deleteProject(request, portfolio_id, project_id): 

    obj = get_object_or_404(Project, id=project_id)
    context ={
        "portfolio_id":portfolio_id,
        "project_id":project_id
    }
 
    if request.method =="POST":
        obj.delete()
        return redirect('portfolio-detail', portfolio_id)

    return render(request, "portfolio_app/delete_view.html", context)

def updateProject(request, portfolio_id, project_id):
    form = ProjectForm()
    portfolio = Portfolio.portfolios.get(pk=portfolio_id)

    context ={
        "portfolio_id":portfolio_id,
        "project_id":project_id
    }
    obj = get_object_or_404(Project, id=project_id)
    form = ProjectForm(request.POST, instance=obj)

    if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def updatePortfolio(request, portfolio_id):
    form = PortfolioForm()
    portfolio = Portfolio.portfolios.get(pk=portfolio_id)

    context ={
        "portfolio_id":portfolio_id,
    }
    obj = get_object_or_404(Portfolio, id=portfolio_id)
    form = PortfolioForm(request.POST, instance=obj)

    if form.is_valid():
            # Save the form without committing to the database
            portfolio = form.save(commit=False)
            portfolio.save()

            return redirect('students')
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student
class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)

        context['project_list'] = Project.projects.filter(portfolio__pk=self.object.pk)

        return context

class PortfolioListView(generic.ListView):
    model = Portfolio
class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project