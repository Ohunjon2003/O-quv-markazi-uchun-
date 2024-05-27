from django.urls import path,include
from .views import *
urlpatterns = [
    path('projects/',projects,name='projects'),
    path('project_add/',project_add,name='project_add'),
    path('project_edit/<uuid:id>/',project_edit,name='project_edit'),
    path('project_delete/<uuid:id>/',project_delete,name='project_delete'),
    path('project/<uuid:id>/',project,name='project'),
]
