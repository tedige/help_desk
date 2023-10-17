from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_problem, name='create_problem'),
    path('problems/', views.problem_list, name='problem_list'),
    path('problem/<int:problem_id>/', views.view_problem, name='view_problem'),
]
