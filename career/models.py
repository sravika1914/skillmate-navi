from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ----------------------
# Skill Model
# ----------------------

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('databases', 'Databases'),
        ('cloud', 'Cloud & DevOps'),
        ('design', 'Design & UI/UX'),
        ('soft-skills', 'Soft Skills'),
        ('project-management', 'Project Management'),
        ('data-science', 'Data Science & Analytics'),
        ('other', 'Other'),
    ]

    PROFICIENCY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
        ('master', 'Master'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS)
    experience = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    certifications = models.CharField(max_length=255, blank=True, null=True)
    currently_learning = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.skill_name}"


# ----------------------
# UserProfile Model
# ----------------------

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_submitted_skills = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# ----------------------
# Auto-create UserProfile on User creation
# ----------------------

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

class SkillRoadmap(models.Model):
    skill_name = models.CharField(max_length=100)
    stage = models.PositiveIntegerField()  # Step number
    title = models.CharField(max_length=200)
    description = models.TextField()
    resource_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['stage']  # Ensures steps are shown in order

    def __str__(self):
        return f"{self.skill_name} - Step {self.stage}: {self.title}"

from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class CourseCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    platform = models.CharField(max_length=100, blank=True)
    completed_on = models.DateField()

    def __str__(self):
        return f"{self.course_name} - {self.user.username}"


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255, blank=True)
    certificate_link = models.URLField(blank=True)
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.course_name
