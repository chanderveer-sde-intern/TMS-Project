from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):

    ROLE_CHOICES = [
        ('mentor', 'Mentor'),
        ('intern', 'Intern'),
    ]

   
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

  
    mentor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='intern_profiles'
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Task(models.Model):

    intern = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    due_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default='assigned'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Submission(models.Model):

  
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    github_link = models.URLField(max_length=500)

    note = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    
    score = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(10),  
        ]
    )


    feedback = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Submission for {self.task.title}"

