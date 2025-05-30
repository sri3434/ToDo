from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the add task view
    path('addTask/', views.addTask, name='addTask'),

    # URL pattern for the mark as done view
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # URL pattern for the mark as undone view
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    # URL pattern for editing a task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # URL pattern for the delete task view
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]