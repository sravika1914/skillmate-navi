from django import forms
from .models import Skill
from .models import Goal

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            'skill_name',
            'category',
            'proficiency',
            'experience',
            'description',
            'certifications',
            'currently_learning',
        ]
        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'proficiency': forms.RadioSelect(),
            'experience': forms.NumberInput(attrs={'step': '0.5', 'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'certifications': forms.TextInput(attrs={'class': 'form-input'}),
        }

from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded-lg',
                'placeholder': 'Enter your goal title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-lg',
                'rows': 4,
                'placeholder': 'Describe your goal'
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-2 border rounded-lg'
            }),
        }


from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'platform', 'certificate_link', 'completed_date']
        widgets = {
            'completed_date': forms.DateInput(attrs={'type': 'date'}),
        }
