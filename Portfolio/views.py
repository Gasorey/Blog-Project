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
    template_name = 'Portfolio/resume.html'


############### Project Views #####################

class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/project_detail.html'
    form_class = ProjectForm
    model = Project

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/project_detail.html'
    form_class = ProjectForm
    model = Project

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/Login/'
    redirect_field_name = 'Portfolio/project_list.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(published_date__isnull=True).order_by('create_date')


################## Comments Views ####################


@login_required
def project_publish(request, pk):
    post = get_object_or_404(Project, pk=pk)
    post.publish()
    return redirect('project_detail',pk=pk)

@login_required
def add_comment_to_project(request, pk):
    post = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('project_detail',pk=pk)
    else:
        form = CommentForm()
    return render(request, 'Portfolio/comment_form.html', {'form': form})




@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk),
    comment.approve()
    return redirect('project_detail',pk=pk)



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('project_detail', pk=post_pk)