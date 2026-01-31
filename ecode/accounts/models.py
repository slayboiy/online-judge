from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICE = [
        ('student', 'Cтудент: '),
        ('teacher', 'Преподаватель: '),
        ('admin', 'Администратор: ')
        
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    
    role = models.CharField(max_length=15, choices=ROLE_CHOICE, default='student')
    
    def __str__(self):
        return f"Profile for {self.user.username}"
    
    
    
