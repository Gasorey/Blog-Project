from django.shortcuts import render
from .models import Project, Comment
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required                                  
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm, CommentForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class ResumeView(TemplateView):
    template_name = 'Resume.html'

class PortfolioListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__lte=timezone.now()).order_by('-pubished_date')

class ProjectDetailView(DetailView):
    model = Project

class CreateProjectView(LoginRequiredMixin,CreateView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/Project_Detail.html'
    form_class = ProjectForm
    model = Project

class UpdateProjectView(LoginRequiredMixin,UpdateView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/Project_Detail.html'
    form_class = ProjectForm
    model = Project

class DeleteProjectView(LoginRequiredMixin,DeleteView):
    model = Project

    success_url = reverse_lazy('Project_List')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/Project_list.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__isnull=True).order_by('created_date')
