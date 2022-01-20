from django.urls import path
from .views import TodoList
from .views import TaskDetail
from .views import TaskCreate, TaskUpdate, TaskDelete, TodoLogin, RegisterView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', TodoLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('', TodoList.as_view(), name='task_page'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='task'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    ]
