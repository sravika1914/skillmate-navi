from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import SkillRoadmap
from .models import Skill, UserProfile
from .models import Goal
from .forms import GoalForm
from datetime import date

# ---------------- Signup View ----------------
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'career/signup.html')

# ---------------- Login View ----------------
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            # ✅ Ensure user has a UserProfile
            try:
                profile = user.userprofile
            except UserProfile.DoesNotExist:
                profile = UserProfile.objects.create(user=user)

            # ✅ Redirect based on skill submission
            if not profile.has_submitted_skills:
                return redirect('skill-input')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'career/login.html')
    else:
        return render(request, 'career/login.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Skill, Goal, Course

@login_required
def dashboard_view(request):
    user = request.user

    # Get skills added by the current user
    user_skills = Skill.objects.filter(user=user)

    # Get goals set by the current user
    goals = Goal.objects.filter(user=user)

    # Get completed courses by the user
    completed_courses = Course.objects.filter(user=user)

    context = {
        'skills': user_skills,
        'goals': goals,
        'courses': completed_courses,
    }
    return render(request, 'career/dashboard.html', context)




# ---------------- Skill Input ----------------
@login_required
def skill_input_view(request):
    if request.method == 'POST':
        skill_name = request.POST.get('skillName')
        category = request.POST.get('skillCategory')
        proficiency = request.POST.get('proficiency')
        experience = request.POST.get('experience')
        description = request.POST.get('description')
        certifications = request.POST.get('certifications')
        currently_learning = 'currentlyLearning' in request.POST

        # Save to DB
        Skill.objects.create(
            user=request.user,
            skill_name=skill_name,
            category=category,
            proficiency=proficiency,
            experience=experience,
            description=description,
            certifications=certifications,
            currently_learning=currently_learning,
        )

        # ✅ Update user profile flag
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=request.user)
        profile.has_submitted_skills = True
        profile.save()

        messages.success(request, 'Skill added successfully!')
        return redirect('dashboard')

    return render(request, 'career/skill-input.html', {
        "quick_skills": ['Python', 'Java', 'Communication'],
        "proficiency_levels": [
            ('beginner', 'Beginner', 'Learning basics'),
            ('intermediate', 'Intermediate', 'Some projects done'),
            ('advanced', 'Advanced', 'Worked professionally'),
        ]
    })

# ---------------- Other Views ----------------
def home(request):
    return render(request, 'career/index.html')

def career_plan_view(request):
    return render(request, 'career/career-plan.html')

def add_skill_view(request):
    return render(request, 'career/add-skill.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

@login_required
def skill_roadmap_view(request, skill_name):
    roadmaps = SkillRoadmap.objects.filter(skill_name__iexact=skill_name).order_by('stage')
    
    if not roadmaps:
        messages.warning(request, f"No roadmap found for skill: {skill_name}")
    
    return render(request, 'career/skill-roadmap.html', {
        'skill_name': skill_name.capitalize(),
        'roadmaps': roadmaps
    })

@login_required
def skills_list_view(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'career/skills_list.html', {'skills': skills})

@login_required
def goals_list(request):
    goals = Goal.objects.filter(user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals-list')
    else:
        form = GoalForm()
    return render(request, 'career/goals.html', {'form': form, 'goals': goals})

from .models import Course
from .forms import CourseForm

@login_required
def courses_completed(request):
    courses = Course.objects.filter(user=request.user).order_by('-completed_date')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('courses-completed')
    else:
        form = CourseForm()
    return render(request, 'career/courses.html', {'form': form, 'courses': courses})

def set_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')  # or a goals list page
    else:
        form = GoalForm()
    return render(request, 'career/goal_form.html', {'form': form})

from django.shortcuts import get_object_or_404

def mark_goal_complete(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        goal.completed = True
        goal.save()
    return redirect('dashboard')

from django.shortcuts import render

def progress_tracker(request):
    return render(request, 'career/progress.html')
