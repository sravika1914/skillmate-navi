from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('skill-input/', views.skill_input_view, name='skill-input'),
    path('career-plan/', views.career_plan_view, name='career-plan'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('add-skill/', views.add_skill_view, name='add_skill'),
    path('roadmap/<str:skill_name>/', views.skill_roadmap_view, name='skill-roadmap'),
    path('skills/', views.skills_list_view, name='skills-list'),
    path('goals/', views.goals_list, name='goals-list'),
    path('courses/', views.courses_completed, name='courses-completed'),
    path('set-goal/', views.set_goal, name='set-goal'),
    path('goals/<int:goal_id>/complete/', views.mark_goal_complete, name='mark-goal-complete'),
    path('progress/', views.progress_tracker, name='progress-tracker'),
]
