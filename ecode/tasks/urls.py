from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_view, name='tasks'),
    path('<int:pk>/show', views.task_detailview.as_view(), name='task-show'),
    path('<int:pk>/update',views.task_update_view.as_view(), name='task_update'),
    path('create', views.task_create_view, name='task-create'),
    path('<int:pk>/delete', views.task_delete_view, name='task-delete')
] 