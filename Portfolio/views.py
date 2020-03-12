from django.shortcuts import render, get_object_or_404,redirect
from .models import Project, Comment
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required                                  
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm, CommentForm
from django.urls import reverse, reverse_lazy
# Create your views here.


########## Resume ##################
 
class ResumeView(TemplateView):                      
    template_name = 'Resume.html'


############### Project Views #####################

class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__lte=timezone.now()).order_by('-pubished_date')

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/Project_Detail.html'
    form_class = ProjectForm
    model = Project

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/Project_Detail.html'
    form_class = ProjectForm
    model = Project

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project

    success_url = reverse_lazy('Project_List')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/Project_list.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__isnull=True).order_by('created_date')


################## Comments Views ####################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Project,pk=pk),
    post.publish
    return redirect('Project_Detail',pk=pk),






@login_required
def add_comment_to_project(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Project
            comment.save()
            return redirect('Project_Detail',pk=project.pk)

    else:
        form = CommentForm()
    return render(request,'Portfolio/Comment_Form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk),
    comment.approve()
    return redirect('Project_Detail',pk=comment.Project.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk),
    post.pk = comment.post.pk
    comment.delete
    return redirect('Project_detail',pk=Project.pk)