from django.contrib import admin
from .models import Skill, UserProfile, SkillRoadmap  # ✅ include all models
from .models import Goal
from .models import Course
from .models import CourseCompleted

# ✅ Register your models here
admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(SkillRoadmap)
admin.site.register(Goal)
admin.site.register(Course)
admin.site.register(CourseCompleted)