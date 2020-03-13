from django.urls import path, include
from . import views

urlpatterns = [
    path('Project_List',views.ProjectListView.as_view(),name='Project_List'),
    path('',views.ResumeView.as_view(),name='Resume'),
    path('Detail/<int:pk>',views.ProjectDetailView.as_view(),name='Project_Detail'),
    path('Project/new',views.ProjectCreateView.as_view(),name='Project_Create'),
    path('Project/<int:pk>/Update',views.ProjectUpdateView.as_view(),name='Project_Update'),
    path('Project/<int:pk>/Delete',views.ProjectDeleteView.as_view(),name='Project_Delete'),
    path('Drafts/',views.DraftListView.as_view(),name='Draft_List'),
    path('Project/<int:pk>/Comment',views.add_comment_to_project,name='Comment_Add'),
    path('Comment/<int:pk>/Approve/',views.comment_approve,name='Comment_Approve'),
    path('Comment/<int:pk>/Remove/',views.comment_remove,name='Comment_Remove'),
    path('Project/<int:pk>/Publish', views.project_publish,name='project_publish'),
    
]
