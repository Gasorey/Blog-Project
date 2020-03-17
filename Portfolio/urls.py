from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.ProjectListView.as_view(),name='project_list'),
    path('resume/',views.ResumeView.as_view(),name='resume'),
    path('project/<int:pk>',views.ProjectDetailView.as_view(),name='project_detail'),
    path('project/new',views.ProjectCreateView.as_view(),name='project_create'),
    path('project/<int:pk>/update',views.ProjectUpdateView.as_view(),name='project_update'),
    path('project/<int:pk>/delete',views.ProjectDeleteView.as_view(),name='project_delete'),
    path('project/<int:pk>/publish', views.project_publish,name='project_publish'),
    path('drafts/',views.DraftListView.as_view(),name='draft_list'),
    path('project/<int:pk>/comment',views.add_comment_to_project,name='comment_add'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
]
