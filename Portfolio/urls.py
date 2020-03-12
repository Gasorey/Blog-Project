from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ProjectListView.as_view(),name='ProjectListView'),
    path('Resume/',views.ResumeView.as_view(),name='Resume'),
    path('Detail/<int:pk>',views.ProjectDetailView.as_view(),name='ProjectDetailView'),
    path('Project/new',views.CreateProjectView.as_view(),name='CreateProjectView')



]
