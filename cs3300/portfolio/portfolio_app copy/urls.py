from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('students/', views.StudentListView.as_view(), name= 'students'),
path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
path('portfolio/', views.PortfolioListView.as_view(), name='portfolios'),
path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
path('projects/', views.ProjectListView.as_view(), name='projects'),
path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
path('portfolio/<int:portfolio_id>/<int:project_id>/delete_project/', views.deleteProject, name='delete_project'),
path('portfolio/<int:portfolio_id>/<int:project_id>/update_project/', views.updateProject, name='update_project'),
path('portfolio/update_portfolio/<int:portfolio_id>/', views.updatePortfolio, name='update_portfolio'),
]