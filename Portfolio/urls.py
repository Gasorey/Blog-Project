from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ProjectListView.as_view(),name='Project_List'),
    path('Resume/',views.ResumeView.as_view(),name='Resume'),
    path('Detail/<int:pk>',views.ProjectDetailView.as_view(),name='Project_Detail'),
    path('Project/new',views.ProjectCreateView.as_view(),name='Project_Create'),
    path('Project/<int:pk>/Update'.views.ProjectUpdateView.as_view(),name='Project_Update'),
    path('Project/<int:pk>/Delete',views.ProjectDeleteView.as_view(),name='Project_Delete'),
    path('Drafts/',views.DraftListView.as_view(),name='Draft_List'),



]
